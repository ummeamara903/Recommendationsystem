import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
model_dir = os.path.join(BASE_DIR, "fashionscience", "models")

rf_product = joblib.load(os.path.join(model_dir, "product_model.pkl"))
rf_accessory = joblib.load(os.path.join(model_dir, "accessory_model.pkl"))
rf_shoes = joblib.load(os.path.join(model_dir, "shoes_model.pkl"))
rf_color = joblib.load(os.path.join(model_dir, "color_model.pkl"))

encoder = joblib.load(os.path.join(model_dir, "encoder.pkl"))
scaler = joblib.load(os.path.join(model_dir, "scaler.pkl"))

mlb_product = joblib.load(os.path.join(model_dir, "mlb_product.pkl"))
mlb_accessory = joblib.load(os.path.join(model_dir, "mlb_accessory.pkl"))
mlb_shoes = joblib.load(os.path.join(model_dir, "mlb_shoes.pkl"))
mlb_color = joblib.load(os.path.join(model_dir, "mlb_color.pkl"))



def recommend(data):
    # Prepare input
    cat_data = [[data.gender, data.season, data.occasion, data.dress_type]]
    budget_data = [[data.budget]]

    X_cat = encoder.transform(cat_data).toarray()
    budget_scaled = scaler.transform(budget_data)

    X = np.hstack((X_cat, budget_scaled))

    # Predictions
    product_pred = rf_product.predict(X)
    accessory_pred = rf_accessory.predict(X)
    shoes_pred = rf_shoes.predict(X)
    color_pred = rf_color.predict(X)

    # Decode
    product = mlb_product.inverse_transform(product_pred)[0]
    accessory = mlb_accessory.inverse_transform(accessory_pred)[0]
    shoes = mlb_shoes.inverse_transform(shoes_pred)[0]
    color = mlb_color.inverse_transform(color_pred)[0]

    return {
        "product": list(product),
        "accessory": list(accessory),
        "shoes": list(shoes),
        "color": list(color)
    }
