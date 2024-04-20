from PIL import Image
import pytesseract

# Create a function using this scanner that will allow us to scan extra stuff

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'



class Scanner():

    def __init__(self):
        pass
        # self.allPhotos = []

    def pyScan(self, file):
        if file == "uploads/None":
            return
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        ingredientList = [value.strip().replace("\n", " ") for value in text.split(",")]

        return ingredientList

    def textAreaScan(self, data):
        ingredientList = [value.strip().replace("\n", " ") for value in data.split(",")]
        return ingredientList
        # self.allPhotos.append(ingredientList)
