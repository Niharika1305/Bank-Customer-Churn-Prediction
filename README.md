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

**Exited**

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

## 🔍 Explainability

The project includes explainability-related Machine Learning work using SHAP (SHapley Additive exPlanations) to support understanding of feature contributions.

SHAP is used as part of the Machine Learning workflow to help analyze how different customer features can influence model predictions.