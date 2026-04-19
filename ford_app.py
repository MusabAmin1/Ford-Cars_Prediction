import streamlit as st
import numpy as np
import joblib

# =========================
# Load trained model
# =========================
model = joblib.load('ford_model.pkl')

# =========================
# Feature columns (from training)
# =========================
feature_columns = [
    'year', 'mileage', 'tax', 'mpg', 'engineSize',

    'model_ Mustang', 'model_ Edge', 'model_ Fusion', 'model_ Streetka',
    'model_ KA', 'model_ Puma', 'fuelType_Hybrid', 'model_ Galaxy',
    'model_ Tourneo Custom', 'model_ Fiesta', 'model_ Kuga',
    'model_ S-MAX', 'transmission_Manual', 'fuelType_Petrol',
    'fuelType_Electric', 'model_ Focus', 'transmission_Semi-Auto',
    'model_ Mondeo', 'model_ Ka+'
]

# =========================
# Mapping (IMPORTANT FIX for drop_first)
# =========================

# transmission (drop_first=True → assume AUTOMATIC as baseline)
def encode_transmission(input_array, value):
    if value == "Manual":
        if "transmission_Manual" in feature_columns:
            idx = feature_columns.index("transmission_Manual")
            input_array[idx] = 1

    elif value == "Semi-Auto":
        if "transmission_Semi-Auto" in feature_columns:
            idx = feature_columns.index("transmission_Semi-Auto")
            input_array[idx] = 1
    # Automatic = baseline (all 0)

# fuel type
def encode_fuel(input_array, value):
    col = f"fuelType_{value}"
    if col in feature_columns:
        idx = feature_columns.index(col)
        input_array[idx] = 1
    # baseline (likely Diesel or dropped) = all 0

# model encoding (safe for unseen categories too)
def encode_model(input_array, value):
    col = f"model_{value}"
    if col in feature_columns:
        idx = feature_columns.index(col)
        input_array[idx] = 1
    # unseen model → treated as baseline (all 0)

# =========================
# UI
# =========================
st.set_page_config(page_title="Car Price Predictor", layout="centered")

st.title("🚗 Ford Car Price Prediction App")
st.write("Fill details to predict car price")

# numeric inputs
# numeric inputs (SLIDERS / DRAGGABLE)

year = st.number_input("Year", min_value=1990, max_value=2026, value=2015, step=1)
mileage = st.number_input("Mileage", min_value=0, max_value=300000, value=50000, step=200)
tax = st.number_input("Tax", min_value=0, max_value=1000, value=150, step=10)
mpg = st.number_input("MPG", min_value=0.0, max_value=100.0, value=50.0, step=0.5)
engineSize = st.number_input("Engine Size", min_value=0.0, max_value=6.0, value=1.5, step=0.1)

# categorical inputs (FULL OPTIONS as you requested)
model_input = st.selectbox("Model", [
    "Fiesta","Focus","Kuga","EcoSport","C-MAX","Ka+","Mondeo","B-MAX",
    "S-MAX","Grand C-MAX","Galaxy","Edge","KA","Puma","Tourneo Custom",
    "Grand Tourneo Connect","Mustang","Tourneo Connect","Fusion",
    "Streetka","Ranger","Escort","Transit Tourneo"
])

fuel_input = st.selectbox("Fuel Type", [
    "Petrol","Hybrid","Electric"
])

transmission_input = st.selectbox("Transmission", [
    "Manual","Semi-Auto","Automatic"
])

# =========================
# Prediction
# =========================
if st.button("Predict Price"):

    input_data = np.zeros(len(feature_columns))

    # numeric
    input_data[0] = year
    input_data[1] = mileage
    input_data[2] = tax
    input_data[3] = mpg
    input_data[4] = engineSize

    # categorical encoding
    encode_model(input_data, model_input)
    encode_fuel(input_data, fuel_input)
    encode_transmission(input_data, transmission_input)

    # predict
    prediction = model.predict([input_data])

    st.success(f"💰 Predicted Price: {prediction[0]:,.2f}")
