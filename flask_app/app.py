from flask import Flask, render_template, request
from utils import predict_customer

app = Flask(__name__)


# ==========================================================
# AVAILABLE MACHINE LEARNING MODELS
# ==========================================================

models = {
    "all_models": "All Models",
    "logistic_regression": "Logistic Regression",
    "knn": "K-Nearest Neighbors (KNN)",
    "decision_tree": "Decision Tree",
    "random_forest": "Random Forest",
    "svm": "Support Vector Machine (SVM)"
}


# ==========================================================
# HOME PAGE
# ==========================================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================================
# CONTACT FORM
# ==========================================================

@app.route("/contact", methods=["POST"])
def contact():

    try:

        # --------------------------------------------------
        # GET CONTACT FORM DATA
        # --------------------------------------------------

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()


        # --------------------------------------------------
        # VALIDATE CONTACT FORM
        # --------------------------------------------------

        if not name or not email or not subject or not message:

            return """
            <h2>Missing Information</h2>

            <p>
                Please fill in all contact form fields.
            </p>

            <a href="/#contact">
                Go back to Contact
            </a>
            """, 400


        # --------------------------------------------------
        # PRINT MESSAGE IN TERMINAL
        # --------------------------------------------------

        print("\n========== CONTACT MESSAGE ==========")

        print("Name:", name)
        print("Email:", email)
        print("Subject:", subject)
        print("Message:", message)

        print("=====================================\n")


        # --------------------------------------------------
        # SUCCESS RESPONSE
        # --------------------------------------------------

        return """
        <!DOCTYPE html>

        <html lang="en">

        <head>

            <meta charset="UTF-8">

            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            >

            <title>
                Message Sent | ChurnSense AI
            </title>

            <style>

                body {

                    margin: 0;

                    font-family: Arial, sans-serif;

                    background: #f5f8fc;

                    display: flex;

                    justify-content: center;

                    align-items: center;

                    min-height: 100vh;

                }


                .success-box {

                    background: white;

                    padding: 45px;

                    border-radius: 16px;

                    text-align: center;

                    box-shadow:
                        0 10px 35px
                        rgba(0, 0, 0, 0.08);

                    max-width: 500px;

                    width: 90%;

                }


                .success-icon {

                    font-size: 50px;

                    margin-bottom: 15px;

                }


                h2 {

                    color: #12213f;

                    margin-bottom: 12px;

                }


                p {

                    color: #5f718d;

                    line-height: 1.6;

                }


                a {

                    display: inline-block;

                    margin-top: 20px;

                    padding: 12px 24px;

                    background: #2563eb;

                    color: white;

                    text-decoration: none;

                    border-radius: 8px;

                    font-weight: 600;

                }


                a:hover {

                    background: #1d4ed8;

                }

            </style>

        </head>


        <body>

            <div class="success-box">

                <div class="success-icon">
                    ✓
                </div>

                <h2>
                    Message Sent Successfully!
                </h2>

                <p>
                    Thank you for contacting ChurnSense AI.
                    Your message has been received successfully.
                </p>

                <a href="/#contact">
                    Back to Contact
                </a>

            </div>

        </body>

        </html>
        """


    except Exception as e:

        print("\n========== CONTACT ERROR ==========")

        print("Contact Error:", str(e))

        print("===================================\n")


        return """
        <h2>
            Something went wrong
        </h2>

        <p>
            We could not process your message.
            Please try again.
        </p>

        <a href="/#contact">
            Go back to Contact
        </a>
        """, 500



# ==========================================================
# PREDICTION PAGE
# ==========================================================

@app.route("/predict", methods=["GET", "POST"])
def predict():

    # ------------------------------------------------------
    # GET REQUEST
    # ------------------------------------------------------

    if request.method == "GET":

        return render_template(
            "predict.html",
            models=models
        )


    # ------------------------------------------------------
    # POST REQUEST
    # ------------------------------------------------------

    try:

        # ==================================================
        # GET SELECTED MODEL
        # ==================================================

        model_name = request.form.get("model")


        # --------------------------------------------------
        # Validate model selection
        # --------------------------------------------------

        if model_name is None or model_name.strip() == "":

            raise ValueError(
                "Please select a prediction model."
            )


        # Support both possible values
        if model_name == "all":

            model_name = "all_models"


        # ==================================================
        # GET RAW CUSTOMER INFORMATION
        # ==================================================

        credit_score_raw = request.form.get("credit_score")
        age_raw = request.form.get("age")
        tenure_raw = request.form.get("tenure")
        balance_raw = request.form.get("balance")
        num_products_raw = request.form.get("num_products")
        has_credit_card_raw = request.form.get("has_credit_card")
        active_member_raw = request.form.get("active_member")
        estimated_salary_raw = request.form.get("estimated_salary")

        gender = request.form.get("gender")
        geography = request.form.get("geography")


        # ==================================================
        # VALIDATE REQUIRED FIELDS
        # ==================================================

        required_fields = {

            "Credit Score": credit_score_raw,

            "Age": age_raw,

            "Tenure": tenure_raw,

            "Account Balance": balance_raw,

            "Number of Products": num_products_raw,

            "Has Credit Card": has_credit_card_raw,

            "Active Member": active_member_raw,

            "Estimated Salary": estimated_salary_raw,

            "Gender": gender,

            "Geography": geography

        }


        missing_fields = []


        for field_name, field_value in required_fields.items():

            if field_value is None or str(field_value).strip() == "":

                missing_fields.append(field_name)


        if missing_fields:

            raise ValueError(

                "Please fill/select the following fields: "
                + ", ".join(missing_fields)

            )


        # ==================================================
        # CONVERT NUMERIC VALUES
        # ==================================================

        try:

            credit_score = float(credit_score_raw)

            age = float(age_raw)

            tenure = float(tenure_raw)

            balance = float(balance_raw)

            num_products = float(num_products_raw)

            has_credit_card = float(has_credit_card_raw)

            active_member = float(active_member_raw)

            estimated_salary = float(estimated_salary_raw)


        except (ValueError, TypeError):

            raise ValueError(

                "Please enter valid numeric values in all "
                "numeric fields."

            )


        # ==================================================
        # GENDER ENCODING
        # ==================================================

        if gender == "Male":

            gender_value = 1

        elif gender == "Female":

            gender_value = 0

        else:

            raise ValueError(
                "Invalid gender selected."
            )


        # ==================================================
        # GEOGRAPHY ENCODING
        # ==================================================

        if geography == "France":

            geography_germany = 0

            geography_spain = 0

        elif geography == "Germany":

            geography_germany = 1

            geography_spain = 0

        elif geography == "Spain":

            geography_germany = 0

            geography_spain = 1

        else:

            raise ValueError(
                "Invalid geography selected."
            )


        # ==================================================
        # CREATE INPUT DATA
        # ==================================================

        data = [

            credit_score,

            gender_value,

            age,

            tenure,

            balance,

            num_products,

            has_credit_card,

            active_member,

            estimated_salary,

            geography_germany,

            geography_spain

        ]


        # ==================================================
        # DEBUG INFORMATION
        # ==================================================

        print("\n========== CUSTOMER INPUT ==========")

        print("Credit Score:", credit_score)

        print("Gender:", gender_value)

        print("Age:", age)

        print("Tenure:", tenure)

        print("Balance:", balance)

        print("Number of Products:", num_products)

        print("Has Credit Card:", has_credit_card)

        print("Active Member:", active_member)

        print("Estimated Salary:", estimated_salary)

        print("Germany:", geography_germany)

        print("Spain:", geography_spain)

        print("Selected Model:", model_name)

        print("====================================\n")


        # ==================================================
        # ALL MODELS PREDICTION
        # ==================================================

        if model_name == "all_models":

            model_list = [

                (
                    "logistic_regression",
                    "Logistic Regression"
                ),

                (
                    "knn",
                    "K-Nearest Neighbors (KNN)"
                ),

                (
                    "decision_tree",
                    "Decision Tree"
                ),

                (
                    "random_forest",
                    "Random Forest"
                ),

                (
                    "svm",
                    "Support Vector Machine (SVM)"
                )

            ]


            all_results = []

            high_risk_count = 0

            low_risk_count = 0


            # ----------------------------------------------
            # Run all models
            # ----------------------------------------------

            for model_key, model_display_name in model_list:

                prediction, probability = predict_customer(

                    data,

                    model_key

                )


                # ------------------------------------------
                # Count predictions
                # ------------------------------------------

                if prediction == 1:

                    high_risk_count += 1

                else:

                    low_risk_count += 1


                # ------------------------------------------
                # Store result
                # ------------------------------------------

                all_results.append({

                    "model": model_display_name,

                    "prediction": prediction,

                    "probability": probability

                })


            # ==================================================
            # MAJORITY VOTING
            # ==================================================

            if high_risk_count > low_risk_count:

                overall_result = "High Risk"

            else:

                overall_result = "Low Risk"


            # ==================================================
            # SEND RESULTS TO RESULT PAGE
            # ==================================================

            return render_template(

                "result.html",

                all_models=True,

                all_results=all_results,

                high_risk_count=high_risk_count,

                low_risk_count=low_risk_count,

                overall_result=overall_result

            )


        # ==================================================
        # SINGLE MODEL PREDICTION
        # ==================================================

        else:

            # ----------------------------------------------
            # Validate selected model
            # ----------------------------------------------

            if model_name not in models:

                raise ValueError(
                    "Invalid model selected."
                )


            # ----------------------------------------------
            # Run selected model
            # ----------------------------------------------

            prediction, probability = predict_customer(

                data,

                model_name

            )


            # ----------------------------------------------
            # Display result
            # ----------------------------------------------

            return render_template(

                "result.html",

                all_models=False,

                prediction=prediction,

                probability=probability,

                model_name=models[model_name]

            )


    # ======================================================
    # ERROR HANDLING
    # ======================================================

    except Exception as e:

        print("\n========== PREDICTION ERROR ==========")

        print(
            "Prediction Error:",
            str(e)
        )


        import traceback

        traceback.print_exc()


        print("======================================\n")


        return (

            f"""
            <h2>
                Prediction Error
            </h2>

            <p>
                {str(e)}
            </p>

            <p>
                <a href="/predict">
                    Go back to prediction page
                </a>
            </p>
            """,

            400

        )


# ==========================================================
# RUN FLASK APPLICATION
# ==========================================================

if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000

    )