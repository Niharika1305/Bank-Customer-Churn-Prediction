# ==========================================================
# ChurnSense AI
# Model Loading & Prediction Utilities
# ==========================================================

import os
import joblib
import pandas as pd


# ----------------------------------------------------------
# Models Directory
# ----------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODELS_PATH = os.path.join(BASE_DIR, "..", "models")


# ----------------------------------------------------------
# Load Trained Models
# ----------------------------------------------------------

MODELS = {

    "logistic_regression": joblib.load(
        os.path.join(MODELS_PATH, "logistic_regression.pkl")
    ),

    "knn": joblib.load(
        os.path.join(MODELS_PATH, "knn.pkl")
    ),

    "decision_tree": joblib.load(
        os.path.join(MODELS_PATH, "decision_tree.pkl")
    ),

    "random_forest": joblib.load(
        os.path.join(MODELS_PATH, "random_forest.pkl")
    ),

    "svm": joblib.load(
        os.path.join(MODELS_PATH, "svm.pkl")
    )
}


# ----------------------------------------------------------
# Load Scaler
# ----------------------------------------------------------

scaler = joblib.load(
    os.path.join(MODELS_PATH, "scaler.pkl")
)


# ----------------------------------------------------------
# Load Feature Names
# ----------------------------------------------------------

feature_names = joblib.load(
    os.path.join(MODELS_PATH, "feature_names.pkl")
)


# ----------------------------------------------------------
# Model Display Names
# ----------------------------------------------------------

MODEL_DISPLAY_NAMES = {

    "logistic_regression": "Logistic Regression",

    "knn": "K-Nearest Neighbors (KNN)",

    "decision_tree": "Decision Tree",

    "random_forest": "Random Forest",

    "svm": "Support Vector Machine (SVM)"
}


# ----------------------------------------------------------
# Features Used by the Scaler
# ----------------------------------------------------------

SCALER_FEATURES = [
    "CreditScore",
    "Age",
    "Tenure",
    "Balance",
    "NumOfProducts",
    "EstimatedSalary"
]


# ----------------------------------------------------------
# Prediction Function
# ----------------------------------------------------------

def predict_customer(data, model_name):

    """
    Make a churn prediction using the selected model.
    """

    # ------------------------------------------------------
    # Check Model
    # ------------------------------------------------------

    if model_name not in MODELS:

        raise ValueError(
            "Invalid model selected."
        )

    model = MODELS[model_name]


    # ------------------------------------------------------
    # Check Input Length
    # ------------------------------------------------------

    if len(data) != 11:

        raise ValueError(
            f"Expected 11 input features, but received {len(data)}."
        )


    # ------------------------------------------------------
    # Create DataFrame
    # ------------------------------------------------------

    input_df = pd.DataFrame(
        [data],
        columns=feature_names,
        dtype=float
    )


    # ------------------------------------------------------
    # Extract Six Features Used by Scaler
    # ------------------------------------------------------

    numerical_data = input_df[
        SCALER_FEATURES
    ]


    # ------------------------------------------------------
    # Scale Six Features
    # ------------------------------------------------------

    scaled_values = scaler.transform(
        numerical_data
    )


    # ------------------------------------------------------
    # Put Scaled Values Back
    # ------------------------------------------------------

    input_df[SCALER_FEATURES] = scaled_values


    # ------------------------------------------------------
    # Ensure Correct Feature Order
    # ------------------------------------------------------

    input_df = input_df[
        feature_names
    ]


    # ------------------------------------------------------
    # Make Prediction
    # ------------------------------------------------------

    prediction = model.predict(
        input_df
    )[0]


    # ------------------------------------------------------
    # Calculate Probability
    # ------------------------------------------------------

    probability = None

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            input_df
        )

        probability = float(
            probabilities[0][1]
        )


    # ------------------------------------------------------
    # Return Result
    # ------------------------------------------------------

    return int(prediction), probability