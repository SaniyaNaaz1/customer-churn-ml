import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")
features_path =os.path.join(BASE_DIR,"features.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
features = joblib.load(features_path)

st.title("Customer Churn Prediction")

# Create empty dataframe with all features
input_df = pd.DataFrame(columns=features)
input_df.loc[0] = 0

# Example important inputs
tenure = st.number_input("Tenure", min_value=0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)

# Assign values to correct columns
if "tenure" in input_df.columns:
    input_df["tenure"] = tenure

if "MonthlyCharges" in input_df.columns:
    input_df["MonthlyCharges"] = monthly_charges

if st.button("Predict"):
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("High Risk of Churn")
    else:
        st.success("Low Risk of Churn")
