## 🚀 Project Overview

An end-to-end Machine Learning project that predicts customer churn using behavioral and transactional data, helping businesses take proactive retention actions.

---

## 🎯 Problem Statement

Customer churn is a major challenge for subscription-based businesses, leading to revenue loss.
This project predicts whether a customer is likely to churn, enabling companies to take preventive measures.

---

## 💡 Business Impact

* Identify high-risk customers early
* Reduce customer loss through targeted retention strategies
* Improve customer lifetime value (CLV)
* Support data-driven decision making

---

## 📁 Dataset

The dataset includes the following features:

* Age
* Gender
* Tenure
* Usage Frequency
* Support Calls
* Payment Delay
* Subscription Type
* Contract Length
* Total Spend
* Last Interaction
* Churn (Target Variable)

---

## 🔍 Exploratory Data Analysis (EDA)

Performed analysis to understand churn patterns:

* Churn distribution
* Feature relationships
* Correlation heatmap
* Feature importance

### 📊 Key Insights:

* Low tenure customers are more likely to churn
* High support calls indicate dissatisfaction
* Subscription type impacts churn significantly
* Higher total spend → lower churn probability

---

## 🤖 Machine Learning Models

* Logistic Regression
* Random Forest ✅ (Best Model)
* XGBoost

---

## 📈 Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | XX%   |
| Precision | XX%   |
| Recall    | XX%   |
| F1 Score  | XX%   |

👉 Random Forest selected as final model due to best balance of metrics.

---

## ⚙️ How It Works

1. Data preprocessing (cleaning + encoding)
2. Feature engineering
3. Model training
4. Model evaluation
5. Prediction via Streamlit UI
6. Explainability using SHAP

---


## 💻 Web App (Streamlit)

Features:

* Input customer details
* Predict churn probability
* Show business insights
* Display feature importance

---

## 🌍 Live Demo

👉 [https://customer-churn-ml-a8xvkhqtdkksuaprn8v4i5.streamlit.app]

---

## 📸 Screenshots

### 🔹 App Interface

![App](assets/app.png)

### 🔹 Prediction Result

![Result](assets/result.png)

### 🔹 Feature Importance

![Feature Importance](assets/feature_importance.png)

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Matplotlib, Seaborn
* Streamlit
* SHAP

---


## ▶️ How to Run Locally

```bash
# Clone repository
git clone <your-repo-link>

# Go to project folder
cd customer-churn-ml

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
