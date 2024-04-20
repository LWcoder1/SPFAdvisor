class suspectedIngredient:

    def __init__(self):
        self.possibleOffenders =  [
    "Benzophenone", "Benzophenone-2", "Benzophenone-3", "Benzophenone-4",
    "Octinoxate", "Oxybenzone", "Homosalate", "Avobenzone", "Octocrylene",
    "Fragrance", "Retinyl palmitate", "Octyl methoxycinnamate", "Nano Zinc oxide",
    "Butyloctyl Salicylate", "Cylcopentasiloxane / Cyclomethicone",
    "Formaldehyde", "Diazolidinyl urea", "DMDM Hydantoin", "Hydroxymethylglycinate",
    "Methylisothiazolinone", "Sodium lauryl sulfate", "Sodium laureth sulfate",
    "Quaternium-15", "Para-aminobenzoic acid", "Isopropyl Myristate", "Alcohol"
]

    def matchPotentialOffenders(self, comparedList):
        potentialOffenders = []
        for a in self.possibleOffenders:
            for b in comparedList:
                if a in b:
                    potentialOffenders.append(a)
        return potentialOffenders
