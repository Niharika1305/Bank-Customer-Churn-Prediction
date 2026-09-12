// ==========================================================
// ChurnSense AI
// Frontend JavaScript
// ==========================================================

document.addEventListener("DOMContentLoaded", function () {

    // ======================================================
    // MODEL COMPARISON PROBABILITY BARS
    // ======================================================

    const probabilityCells = document.querySelectorAll(
        ".probability-cell"
    );

    probabilityCells.forEach(function (cell) {

        const valueElement = cell.querySelector("strong");
        const bar = cell.querySelector(
            ".probability-bar span"
        );

        if (!valueElement || !bar) {
            return;
        }

        // Get percentage from text such as "65.74%"
        const text = valueElement.textContent.trim();

        const probability = parseFloat(
            text.replace("%", "")
        );

        // Make sure the value is valid
        if (!isNaN(probability)) {

            // Keep value between 0 and 100
            const safeProbability = Math.min(
                Math.max(probability, 0),
                100
            );

            // Set the progress bar width
            bar.style.width = safeProbability + "%";
        }

    });


    // ======================================================
    // SINGLE MODEL PROBABILITY BAR
    // ======================================================

    const singleProbabilityValue =
        document.querySelector(".probability-value");

    const singleProbabilityBar =
        document.querySelector(
            ".main-probability-bar span"
        );

    if (
        singleProbabilityValue &&
        singleProbabilityBar
    ) {

        // Get percentage from text such as "65.74%"
        const text =
            singleProbabilityValue.textContent.trim();

        const probability =
            parseFloat(
                text.replace("%", "")
            );

        if (!isNaN(probability)) {

            const safeProbability = Math.min(
                Math.max(probability, 0),
                100
            );

            singleProbabilityBar.style.width =
                safeProbability + "%";
        }
    }


    // ======================================================
    // BUTTON LOADING EFFECT
    // ======================================================

    const predictionForm =
        document.querySelector(".prediction-form");

    const predictButton =
        document.querySelector(".predict-button");

    if (predictionForm && predictButton) {

        predictionForm.addEventListener(
            "submit",
            function () {

                const buttonText =
                    predictButton.querySelector(
                        "span:first-child"
                    );

                if (buttonText) {
                    buttonText.textContent =
                        "Generating Prediction...";
                }

                predictButton.style.pointerEvents =
                    "none";

                predictButton.style.opacity =
                    "0.7";
            }
        );
    }

});