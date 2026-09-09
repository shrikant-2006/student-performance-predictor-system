

from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model once, when the server starts (not on every request)
model = joblib.load("model/student_model.pkl")

FEATURES = [
    "study_hours_per_day",
    "attendance_percentage",
    "previous_exam_score",
    "sleep_hours_per_day",
    "assignments_completed_percentage",
]


def get_performance_label(score):
    """Turn a numeric score into a friendly category, like a teacher would."""
    if score >= 85:
        return "Excellent", "excellent"
    elif score >= 70:
        return "Good", "good"
    elif score >= 50:
        return "Needs Improvement", "average"
    else:
        return "At Risk", "risk"


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    label = None
    label_class = None
    form_values = {
        "study_hours_per_day": 4,
        "attendance_percentage": 80,
        "previous_exam_score": 65,
        "sleep_hours_per_day": 7,
        "assignments_completed_percentage": 75,
    }

    if request.method == "POST":
        try:
            # Read the numbers the user typed into the form
            input_data = {}
            for feature in FEATURES:
                value = float(request.form.get(feature))
                input_data[feature] = value
            form_values.update(input_data)

            # The model expects a table (DataFrame) with the same
            # column names it was trained on
            input_df = pd.DataFrame([input_data], columns=FEATURES)

            # Ask the model to predict
            raw_prediction = model.predict(input_df)[0]
            raw_prediction = max(0, min(100, raw_prediction))  # keep 0-100
            prediction = round(raw_prediction, 1)
            label, label_class = get_performance_label(prediction)

        except (TypeError, ValueError):
            prediction = None
            label = "Please enter valid numbers in every field."
            label_class = "risk"

    return render_template(
        "index.html",
        prediction=prediction,
        label=label,
        label_class=label_class,
        form_values=form_values,
    )


if __name__ == "__main__":
    app.run(debug=True)
