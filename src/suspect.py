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
        potentialOffenders = []
        for a in self.possibleOffenders:
            for b in comparedList:
                if a in b:
                    potentialOffenders.append(a)
        return potentialOffenders
