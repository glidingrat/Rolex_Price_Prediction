import os
import pickle
import pandas as pd

MODEL_PATH = os.path.join("app", "model", "random_forest_model.pkl")
TRANSFORMER_PATH = os.path.join("app", "model", "column_transformer.pkl")

with open(MODEL_PATH, "rb") as f:
    rf_model = pickle.load(f)

with open(TRANSFORMER_PATH, "rb") as f:
    column_trans = pickle.load(f)


def validate_attribute(attribute, value, valid_values):
    if not isinstance(value, str):
        raise ValueError(f"{attribute} musí být typu {str.__name__}, zadaná hodnota: {value}")
    if value not in valid_values:
        raise ValueError(f"Neplatná hodnota pro {attribute}: {value}")


def predict_price(size, material, bezel, bracelet, dial, papers):
    valid_sizes = ["31", "36", "41"]
    validate_attribute("Size", size, valid_sizes)

    valid_materials = ["Stainless Steel", "Gold", "Stainless Steel + Gold"]
    validate_attribute("Material", material, valid_materials)

    valid_bezels = ["Smooth", "Fluted", "Diamond"]
    validate_attribute("Bezel", bezel, valid_bezels)

    valid_bracelets = ["Jubilee", "Oyster"]
    validate_attribute("Bracelet", bracelet, valid_bracelets)

    valid_dials = ["Black", "Silver", "Champagne", "Green", "Blue", "White"]
    validate_attribute("Dial", dial, valid_dials)

    valid_papers = ["Yes", "No"]
    validate_attribute("Papers", papers, valid_papers)

    data = pd.DataFrame([[size, material, bezel, bracelet, dial, papers]],
                        columns=["Size", "Material", "Bezel", "Bracelet", "Dial Color", "With Papers"])
    data_transformed = column_trans.transform(data)

    cena_predikce = rf_model.predict(data_transformed)
    return round(cena_predikce[0], 2)
