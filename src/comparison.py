class Comparison:

    # This class will go through the uploaded folders / information you put into the box

    def __init__(self):
        self.ingredientSets = []

    def processIngredients(self, ingredients):
        ingredientList = ingredients.split(",")
        self.ingredientSets.append(ingredientList)

    # For now, we will only match two ingredient lists to make it a lot easier
    def matchIngredients(self):
        matchedIngredients = [value.strip() for value in self.ingredientSets[0] if value in self.ingredientSets[1]]
        return matchedIngredients




