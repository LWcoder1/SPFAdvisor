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
    return render_template("form.html", form=form, file_url=file_url,
                           filename=imageScanner.pyScan(f"uploads/{filename}"))

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


@app.route("/about")
def about():
    return render_template("about.html")



# @app.route('/planner', methods=['GET', 'POST'])
# def planner():
#     if request.method == 'POST':
#         location = request.form['location']
#         ll = returnCoordinates(location)
#         radius = int(request.form['radius'])
#         days = int(request.form['totalDays'])
#         travelPlans = travelPlan(ll, radius, days)
#         travelPlans.dataPopulate()
#         totalDays = []
#         for day in range(days):
#             totalDays.append(day)
#         # we need for loop to solve this
#         # We need to do this for each additional div and change the lunch list
#         # (Basically use something like make it visible to make it work)
#         return render_template("itinerary.html",
#                                duration=totalDays,
#                                breakfastList=travelPlans.breakfastList,
#                                lunchList=travelPlans.lunchList,
#                                dinnerList=travelPlans.dinnerList,
#                                attractionsList=travelPlans.attractionList,
#                                parseString=parseObjectToString,
#                                )
#     else:
#         return render_template("planner.html")

if __name__ == "__main__":
    app.run(debug=True)
