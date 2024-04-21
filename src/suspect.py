class suspectedIngredient:

    def __init__(self):
        self.possibleOffenders = {
            "Benzophenone-2": "Can cause skin irritation, allergic reactions, and sensitization, particularly in individuals with sensitive skin or allergies to similar compounds. It may also have estrogenic effects, potentially disrupting hormone balance in the body.",
            "Benzophenone-3": "Known to be an endocrine disruptor, it can cause allergic reactions and may have harmful effects on marine ecosystems when washed off into water bodies. Prolonged or repeated exposure may lead to skin irritation and other adverse effects.",
            "Benzophenone-4": "Can cause skin irritation, allergic reactions, and sensitization, particularly in individuals with sensitive skin or allergies to similar compounds. It may also have estrogenic effects, potentially disrupting hormone balance in the body.",
            "Octinoxate": "May cause rash, itching/swelling (especially of the face/tongue/throat), severe dizziness, and trouble breathing.",
            "Oxybenzone": "Gets absorbed into the skin, which makes it last longer. Causes rashes, severe itching, dizziness, and difficulty breathing.",
            "Homosalate": "May cause skin irritation.",
            "Avobenzone": "May cause dermatitis.",
            "Octocrylene": "Increases the risk of melanoma.",
            "Fragrance": "May cause severe sunburn or eczema.",
            "Retinyl palmitate": "Increases skin sensitivity to sunlight, potentially leading to sunburn and skin damage.",
            "Octyl methoxycinnamate": "May disrupt endocrine functions, increase cell proliferation in response to estrogen exposure, and potentially lead to breast cancer with long exposure.",
            "Nano Zinc Oxide": "Can cause skin irritation or allergic reactions, especially if used in high concentrations or if not properly formulated.",
            "Butyloctyl Salicylate": "May cause irritation or allergic reactions in sensitive individuals, particularly those with salicylate allergies.",
            "Cylcopentasiloxane": "Can potentially clog pores and exacerbate acne in some individuals, especially if used in high concentrations or on oily skin types.",
            "Formaldehyde types": "Releases formaldehyde, which is associated with potential health risks such as carcinogenicity.",
            "Diazolidinyl urea": "May cause skin irritation, allergic reactions, and sensitization in some individuals, and it releases formaldehyde, which is associated with potential health risks such as carcinogenicity.",
            "Quaternium-15": "Known to release formaldehyde, it may cause skin irritation, allergic reactions, and sensitization, particularly in individuals with formaldehyde allergies or sensitivities.",
            "DMDM Hydantoin": "Releases formaldehyde, which can cause skin irritation, allergic reactions, and sensitization, especially in individuals with formaldehyde allergies or sensitivities.",
            "Hydroxymethylglycinate": "While generally considered a mild preservative, it may cause skin irritation and allergic reactions in some individuals, particularly those with sensitive skin or allergies to similar compounds.",
            "Methylisothiazolinone": "Known to cause allergic reactions, skin irritation, and sensitization in some individuals, particularly when used in high concentrations or on sensitive skin.",
            "Sodium Lauryl": "These surfactants can strip the skin of its natural oils, leading to dryness, irritation, and potential disruption of the skin barrier. They may also cause eye irritation and allergic reactions in some individuals.",
            "Laureth Sulfate": "These surfactants can strip the skin of its natural oils, leading to dryness, irritation, and potential disruption of the skin barrier. They may also cause eye irritation and allergic reactions in some individuals.",
            "Cyclomethicone": "Can potentially clog pores and exacerbate acne in some individuals, especially if used in high concentrations or on oily skin types."
        }

    # ADDED COMMENTS
    def matchPotentialOffenders(self, comparedList):
        potentialOffenders = {}
        for item in range(len(comparedList)):
            for key, value in self.possibleOffenders.items():
                if key in comparedList[item]:
                    potentialOffenders[key] = value

        return potentialOffenders
