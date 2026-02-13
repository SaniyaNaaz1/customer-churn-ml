# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details on the left and click Predict. Model expects the same features used during training.")

# Helper to load artifacts safely
def load_artifact(path, name):
    if not os.path.exists(path):
        st.error(f"Required file missing: {name} ({path}).\nPlease ensure it's in the project root.")
        st.stop()
    with open(path, "rb") as f:
        return pickle.load(f)

# Try to load model and feature list
try:
    model = load_artifact("model.pkl", "Trained Model")
    features = load_artifact("features.pkl", "Feature columns list")
except Exception as e:
    st.stop()

# Optional scaler
use_scaler = False
scaler = None
if os.path.exists("scaler.pkl"):
    try:
        scaler = load_artifact("scaler.pkl", "Scaler")
        use_scaler = True
    except Exception:
        use_scaler = False

# Sidebar inputs for every feature used in training
st.sidebar.header("Customer details")

age = st.sidebar.slider("Age", 16, 90, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
tenure = st.sidebar.slider("Tenure (months)", 0, 120, 12)
usage = st.sidebar.slider("Usage Frequency (per month)", 0, 500, 20)
support_calls = st.sidebar.slider("Support Calls (last 3 months)", 0, 50, 2)
payment_delay = st.sidebar.slider("Payment Delay (days)", 0, 365, 0)

subscription = st.sidebar.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
contract = st.sidebar.selectbox("Contract Length", ["Monthly", "Quarterly", "Yearly"])
total_spend = st.sidebar.number_input("Total Spend (lifetime)", min_value=0.0, value=500.0, step=1.0, format="%.2f")
last_interaction = st.sidebar.slider("Last Interaction (days ago)", 0, 365, 10)

# Build a dataframe from inputs
input_df = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "Tenure": [tenure],
    "Usage Frequency": [usage],
    "Support Calls": [support_calls],
    "Payment Delay": [payment_delay],
    "Subscription Type": [subscription],
    "Contract Length": [contract],
    "Total Spend": [total_spend],
    "Last Interaction": [last_interaction]
})

st.write("### Preview of input data")
st.dataframe(input_df.T, height=300)

# Encode categorical variables exactly the same way we usually do in notebooks
input_encoded = pd.get_dummies(input_df)

# Align with training features (missing columns -> fill 0)
# features is expected to be a list-like of column names used in training after get_dummies
try:
    input_aligned = input_encoded.reindex(columns=features, fill_value=0)
except Exception as e:
    st.error("Failed to align input with trained features. Please ensure features.pkl contains a list of training feature column names.")
    st.exception(e)
    st.stop()

# Apply scaler if available
if use_scaler:
    try:
        input_aligned_scaled = scaler.transform(input_aligned)
    except Exception as e:
        st.error("Scaler exists but failed to transform input. Check that scaler was fitted on the same columns and order as features.pkl")
        st.exception(e)
        st.stop()
    final_input = input_aligned_scaled
else:
    final_input = input_aligned

# Prediction
if st.button("Predict"):
    try:
        # Some models (e.g. from sklearn) have predict_proba; handle when missing
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(final_input)[0][1]
        else:
            # fallback: if model doesn't support predict_proba, use predict and set proba as 0/1
            pred_label = model.predict(final_input)[0]
            proba = float(pred_label)

        pred = 1 if proba >= 0.5 else 0

        # Pretty display
        st.subheader("🔍 Prediction Result")
        if pred == 1:
            st.error(f"⚠️ Predicted: CHURN (probability = {proba:.2f})")
        else:
            st.success(f"✅ Predicted: STAY (probability = {proba:.2f})")

        # Business insight box
        st.subheader("📈 Business Insight")
        if proba > 0.8:
            st.write("High risk of churn — consider immediate retention (discounts, personalized outreach).")
        elif proba > 0.5:
            st.write("Moderate risk — monitor and apply targeted engagement.")
        else:
            st.write("Low risk — maintain normal engagement.")

        # Show top contributing features if model has feature_importances_
        if hasattr(model, "feature_importances_"):
            importances = model.feature_importances_
            # create series only for present features
            feat_series = pd.Series(importances, index=features).sort_values(ascending=False).head(8)
            st.subheader("🔥 Top features (model importance)")
            st.table(feat_series)
        else:
            st.info("Model does not provide feature importances.")
    except Exception as e:
        st.error("Model prediction failed. See details below:")
        st.exception(e)