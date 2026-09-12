# ChurnSense AI

### Predict. Prevent. Retain.

A Machine Learning-based Bank Customer Churn Prediction platform built with Python and Flask.

---

## 📌 Project Overview

**ChurnSense AI** is a Machine Learning web application designed to predict whether a bank customer is likely to leave the bank.

The application takes customer demographic and banking information as input and uses trained Machine Learning models to predict customer churn risk.

The project includes multiple classification models and provides both individual model predictions and an **All Models** comparison for a broader view of the prediction.

---

## 🎯 Objectives

- Predict whether a customer is likely to churn.
- Compare multiple Machine Learning classification algorithms.
- Provide customer churn probability and risk classification.
- Present prediction results through a professional Flask web application.
- Make Machine Learning predictions understandable to both technical and non-technical users.
- Prepare the application for production deployment.

---

## 📊 Dataset

**Dataset:** `Churn_Modelling.csv`

The dataset contains customer demographic and banking information.

### Input Features

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary

### Target Variable

**`Exited`**

- `0` = Customer did not churn
- `1` = Customer churned

---

## 🤖 Machine Learning Models

ChurnSense AI uses five Machine Learning classification models:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Decision Tree
4. Random Forest
5. Support Vector Machine (SVM)

The application allows users to select an individual model or compare all five models together.

---

## 📈 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

### Model Performance

| Model | Accuracy | ROC-AUC | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 80.80% | 77.48% | 19% | 28% |
| KNN | 85.35% | 84.41% | 35% | 49% |
| Decision Tree | 85.45% | 83.04% | 48% | 58% |
| Random Forest | 86.40% | 85.65% | 45% | 57% |
| SVM | 86.40% | 82.62% | 43% | 57% |

### Recommended Model

**Random Forest** achieved the highest ROC-AUC score of **85.65%** and is therefore highlighted as the recommended model for the application.

Random Forest and SVM both achieved the highest accuracy of **86.40%**.

---

## 🔄 Machine Learning Workflow

The project follows a complete Machine Learning workflow:

```text
Data Collection
       ↓
Data Preprocessing
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Feature Scaling
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Comparison
       ↓
Flask Web Application
       ↓
Customer Churn Prediction
```

---

## 🔍 Explainability

The project includes explainability-related Machine Learning work using **SHAP (SHapley Additive exPlanations)** to support understanding of feature contributions.

SHAP is used as part of the Machine Learning workflow to help analyze how different customer features can influence model predictions.

---

## 🌐 Web Application

The final application is built using **Flask**.

### Main Features

- Professional responsive user interface
- Customer information input form
- Input validation
- Individual model prediction
- All Models comparison
- Churn probability
- Risk classification
- Model comparison results
- Responsive design for desktop, tablet, and mobile
- Contact form
- Professional ChurnSense AI branding

---

## 🏗️ Project Structure

```text
Bank-Customer-Churn-Prediction/
│
├── data/
│   ├── Churn_Modelling.csv
│   └── cleaned_data.csv
│
├── models/
│   ├── logistic_regression.pkl
│   ├── knn.pkl
│   ├── decision_tree.pkl
│   ├── random_forest.pkl
│   ├── svm.pkl
│   ├── scaler.pkl
│   └── feature_names.pkl
│
├── notebooks/
│   ├── 00_Project_Setup.ipynb
│   └── Bank_Customer_Churn_Prediction.ipynb
│
├── reports/
│
├── flask_app/
│   ├── app.py
│   ├── utils.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── predict.html
│   │   └── result.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       │
│       ├── js/
│       │   └── script.js
│       │
│       └── images/
│           ├── logo.png
│           └── favicon.ico
│
├── requirements.txt
├── README.md
├── BRAND_GUIDELINES.md
├── brand.md
└── .gitignore
```

---

## 🛠️ Technologies Used

### 1. Programming Language

- Python

### 2. Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib

### 3. Explainable AI

- SHAP

### 4. Web Development

- Flask
- HTML
- CSS
- JavaScript

### 5. Data Visualization

- Matplotlib
- Seaborn

### 6. Deployment Preparation

- Gunicorn

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Niharika1305/Bank-Customer-Churn-Prediction.git
```

### 2. Open the Project

```bash
cd Bank-Customer-Churn-Prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Navigate to the Flask application directory:

```bash
cd flask_app
```

Run the application:

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000
```

For access from another device on the same network, use the host machine's local IP address.

---

## 🧪 Model Prediction

The application accepts the following customer information:

- Credit Score
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Estimated Salary
- Geography
- Credit Card Status
- Active Member Status

The selected Machine Learning model produces:

- Churn / No Churn prediction
- Churn probability
- Risk classification

The **All Models** option compares predictions from all five trained models.

---

## 📌 Important Note

Churn prediction is a Machine Learning-based estimation and should be treated as a **decision-support tool** rather than a guarantee of future customer behavior.

---

## 🚀 Future Improvements

Possible future improvements include:

- Cloud deployment
- Downloadable prediction reports
- Additional model explainability visualizations
- Advanced customer-level analytics
- Model monitoring and performance tracking
- Automated model retraining

---

## 👩‍💻 Author

**Niharika Chatrath**

B.Tech — Artificial Intelligence & Machine Learning

Data Science & Artificial Intelligence Enthusiast

---

## 🏷️ Project Tagline

**Predict. Prevent. Retain.**