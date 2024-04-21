from flask import Flask, render_template, url_for, request, jsonify, send_from_directory
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from src.scanner import Scanner
from src.suspect import suspectedIngredient
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["UPLOADED_PHOTOS_DEST"] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
imageScanner = Scanner()
susIngredients = suspectedIngredient()


class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, "Only images are allowed"),
            FileRequired("File field should not be empty")
        ]
    )
    submit = SubmitField("Upload")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/uploads/<filename>")
def getFile(filename):
    return send_from_directory(app.config["UPLOADED_PHOTOS_DEST"], filename)


@app.route("/form", methods=['GET', 'POST'])
def uploadImage():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('getFile', filename=filename)
    else:
        file_url = None
        filename = None

    # return render_template("form.html", form=form, file_url=file_url,
    #                        filename=imageScanner.pyScan(f"uploads/{filename}"))

    apple = imageScanner.pyScan(f"uploads/{filename}")
    if apple is not None:
        print(apple)
        return render_template("results.html", possibleOffenderList=susIngredients.matchPotentialOffenders(apple))
    else:
        return render_template("form.html", form=form, file_url=file_url)
    #

# ['Active Ingredients Purpose Avobenzone 2.5%', 'octocrylene 8.0%', 'oxybenzone 3.5% Sunscreen Inactive Ingredients: Water', 'aluminum starch octenylsuccinate', 'styrene/ pagans epard g eolagerw tarran agemenare ary ane', 'arachidy! beeswax', 'ethythexyiglycerin', 'neopenty! glycol dihep- tanoate', 'acrylates/C10-30 alkyl acrylate crosspolymer', 'behenyl alcohol', 'to- caer (ten gen iy sven Fb so assium hydraxide', 'disodium EDTA', 'sodium ascorbyl phosphate', 'fragrance']


@app.route("/addItem", methods=['GET', 'POST'])
def addItem():
    if request.method == "POST":
        currItems = request.form['addText']
        offenderList = imageScanner.textAreaScan(currItems)
        susIngred = susIngredients.matchPotentialOffenders(offenderList)

    return render_template("results.html",
                           possibleOffenderList=susIngred)


@app.route("/textUpload", methods=['GET', 'POST'])
def textUpload():
    return render_template("textUpload.html")


@app.route("/info")
def info():
    return render_template("info.html")

# Active Ingredients: Avobenzone 3%, Octisalate 5%, Octocrylene 10%, Inactive Ingredients: Water, Glycerin, Butyloctyl Salicylate, C12-15 Alkyl Benzoate, Cetearyl Alcohol, Propanediol, Glyceryl Stearate Citrate, Cocoglycerides, Isododecane, Cetyl Esters, Cetyl Phosphate, Diisopropyl Sebacate, Isodecyl Neopentanoate, Lauryl Lactate, Arginine, 1,2-Hexanediol, Caprylyl Glycol, Hydroxyacetophenone, Polymethylsilsesquioxane, Raphanus Sativus (Radish) Seed Oil, Diethylhexyl Syringylidenemalonate, Helianthus Annuus (Sunflower) Seed Wax, Limnanthes Alba (Meadowfoam) Seed Oil, Acrylates/C10-30 Alkyl Acrylate Crosspolymer, Chlorphenesin, Xanthan Gum, Trisodium Ethylenediamine Disuccinate, Argania Spinosa Kernel Oil, Caprylic/Capric Triglyceride, Citrus Nobilis (Mandarin Orange) Peel Oil, Plantago Lanceolata Leaf Extract, Glycine Soja (Soybean) Oil, Tocopherol, Cymbopogon Schoenanthus Oil, Hippophae Rhamnoides Fruit Oil, Elettaria Cardamomum Seed Oil, Eugenia Caryophyllus (Clove) Leaf Oil, Cinnamomum Cassia Leaf Oil, Vanillin, Eucalyptus Globulus Leaf Oil, Lavandula Hybrida Grosso Herb Oil

if __name__ == "__main__":
    app.run(debug=True)
