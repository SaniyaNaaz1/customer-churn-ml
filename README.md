Customer Churn Prediction – Machine Learning Project
🚀 Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses.
This project predicts whether a customer is likely to churn using Machine Learning models.

The goal is to help businesses:

Identify high-risk customers

Improve retention strategies

Reduce revenue loss

📂 Dataset

Dataset: Telco Customer Churn Dataset

Features include:

Customer demographics

Account information

Contract type

Monthly charges

Tenure

Target Variable:

Churn (Yes / No)

🔍 Exploratory Data Analysis (EDA)

Performed detailed analysis including:

Churn distribution analysis

Correlation heatmap

Tenure vs Churn visualization

Monthly Charges vs Churn

Contract type impact on churn

Key Insights:

Customers with month-to-month contracts churn more

Higher monthly charges increase churn probability

Short tenure customers are more likely to churn

🤖 Machine Learning Models Used

Logistic Regression

Random Forest Classifier

XGBoost Classifier

📈 Model Evaluation Metrics

Models evaluated using:

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

🏆 Best Model: Random Forest / XGBoost (whichever is best)
Metric	Score
Accuracy	XX%
Precision	XX%
Recall	XX%
F1 Score	XX%
🔥 Feature Importance

Top features influencing churn:

Contract Type

Tenure

Monthly Charges

Total Charges

Feature importance visualization included.

🌐 Deployment

The model is deployed using Streamlit.

Users can:

Enter customer details

Predict churn probability

View prediction instantly

🛠 Tech Stack

Python

Pandas

NumPy

Matplotlib / Seaborn

Scikit-learn

XGBoost

Streamlit

📦 Project Structure
customer-churn-ml/
│
├── app.py
├── train_model.py
├── model.pkl
├── customer_churn.csv
├── requirements.txt
├── README.md
└── assets/

▶ How to Run Locally

1️⃣ Clone the repository

git clone https://github.com/yourusername/customer-churn-ml.git
cd customer-churn-ml


2️⃣ Create virtual environment

python -m venv venv
source venv/bin/activate


3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Run the app

streamlit run app.py

Screenshots

![alt text](image.png)
![alt text](image-1.png)

![App Screenshot]
![alt text](image-2.png)

🔮 Future Improvements

Add Hyperparameter Tuning (GridSearchCV)

Deploy on Streamlit Cloud

Add SHAP explainability

Improve UI design

Use advanced ensemble models

💡 Business Impact

This model can help businesses:

Proactively retain customers

Reduce churn by targeted marketing

Improve customer lifetime value
