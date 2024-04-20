class suspectedIngredient:

    def __init__(self):
        self.possibleOffenders = [
            "Oxybenzone",
            "Avobenzone",
            "Octinoxate",
            "Homosalate",
            "Octocrylene",
            "Para-aminobenzoic acid",
            "Isopropyl Myristate",
            "Fragrance",
            "Alcohol"
        ]

    def matchPotentialOffenders(self, comparedList):
        potentialOffenders = [value for value in self.possibleOffenders if value in comparedList]
        return potentialOffenders
