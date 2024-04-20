from comparison import Comparison


class suspectedIngredient:

    def __init__(self):
        self.possibleOffenders = [
            "Benzophenone"
            "Benzophenone-2",
            "Benzophenone-3",
            "Benzophenone-4",
            "Octinoxate",
            "Oxybenzone",
            "Homosalate",
            "Avobenzone",
            "Octocrylene",
            "Fragrance",
            "Retinyl palmitate",
            "Octyl methoxycinnamate",
            "Nano Zinc oxide",
            "Butyloctyl Salicylate",
            "Cylcopentasiloxane / Cyclomethicone",
            "Formaldehyde",
            "Diazolidinyl urea",
            "DMDM Hydantoin",
            "Hydroxymethylglycinate",
            "Methylisothiazolinone",
            "Sodium lauryl sulfate",
            "Sodium laureth sulfate",
            "Retinyl Palmitate",
            "Quaternium-15"

        ]

    def matchPotentialOffenders(self, comparedList):
        potentialOffenders = [value for value in self.possibleOffenders if value in comparedList]
        return potentialOffenders


newComparison = Comparison()
# We might need to scrape the website we got this information from incidercoder
newComparison.processIngredients("Water, Cyclohexasiloxane, Zinc Oxide, Titanium Dioxide (Ci 77891), Propanediol, "
                                 "Polyglyceryl-3 Polydimethylsiloxyethyl Dimethicone, Dibutyl Adipate, Niacinamide, "
                                 "Caprylyl Methicone, 1,2-Hexanediol, Disteardimonium Hectorite, Betaine, "
                                 "Magnesium Sulfate, Hydrogen Dimethicone, Inositol, Aluminum Hydroxide, C30-45 Alkyl "
                                 "Cetearyl Dimethicone Crosspolymer, Polyglyceryl-2 Dipolyhydroxystearate, "
                                 "Styrene/​Acrylates Copolymer, Stearic Acid, Butylene Glycol, Pentylene Glycol, "
                                 "Ethylhexylglycerin, Octyldodecanol, Adenosine, Glycerin, Squalane, Allantoin, "
                                 "Anthemis Nobilis Flower Water, Echium Plantagineum Seed Oil, Artemisia Capillaris "
                                 "Extract (0.005%), Vitis Vinifera (Grape) Seed Extract, Calendula Officinalis Flower "
                                 "Extract, Camellia Sinensis Leaf Extract, Cardiospermum Halicacabum "
                                 "Flower/​Leaf/​Vine Extract, Helianthus Annuus (Sunflower) Seed Oil Unsaponifiables, "
                                 "Leuconostoc/​Radish Root Ferment Filtrate, Dicaprylyl Carbonate, "
                                 "Sorbitan Sesquioleate, Palmitoyl Tripeptide-5, Tocopherol, Alcohol")
newComparison.processIngredients("Zinc Oxide (20%), Titanium Dioxide (15.7%) Silica, Calcium Aluminum Borosilicate, "
                                 "Polymethyl Methacrylate, Lauroyl Lysine, Phenoxyethanol, Water (Aqua), "
                                 "Sodium Dehydroacetate, Ascorbyl Palmitate, Ceteareth-25, Glycerin, Cetyl Alcohol, "
                                 "Cholesterol, Ceramide Np, Behenic Acid, Ethylhexylglycerin, Ceramide Ns, "
                                 "Ceramide Ap, Ceramide Eop, Ceramide Eos, Caprooyl Phytosphingosine, "
                                 "Caprooyl Sphingosine, Tocopherol, Titanium Dioxide (Cl 77891), Iron Oxides (Cl "
                                 "77491), Alcohol")

susIngredients = suspectedIngredient()
apple = newComparison.matchIngredients()
print(apple)
print(susIngredients.possibleOffenders)
print(susIngredients.matchPotentialOffenders(apple))
