from flask import Flask, request, render_template
import numpy as np
from tensorflow.keras.models import load_model

# Create flask app
flask_app = Flask(__name__)
model = load_model('model.h5')

@flask_app.route("/")
def Home():
    return render_template("home.html", form_data={})

@flask_app.route("/predict", methods=["POST"])
def predict():
    # Define all conditions
    conditions = ['Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring', 'Itching', 'Irritability', 'delayed healing', 'partial paresis', 'muscle stiffness', 'Alopecia', 'Obesity']

    # Extract features from request form
    form_data = request.form

    # Extract age and gender
    age = form_data.get('age')
    gender = form_data.get('gender')

    # Print age and gender
    print(f"User selected age: {age}")
    print(f"User selected gender: {gender}")

    # Encode gender
    gender = 1 if gender == 'male' else 0

    # Encode conditions
    encoded_conditions = [1 if form_data.get(condition) else 0 for condition in conditions]

    # Print conditions
    for condition, encoded in zip(conditions, encoded_conditions):
        if encoded:
            print(f"User selected condition: {condition}")

    # Combine all features
    features = [age, gender] + encoded_conditions

    # Convert features to numerical array
    float_features = [float(x) for x in features]
    features = np.array(float_features).reshape(1, -1)

    # Make prediction using the model
    prediction_proba = model.predict(features)

    # Convert prediction to a readable format (if necessary)
    if prediction_proba[0][0] > 0.5:
        prediction_text = "Diabetes: Positive, Probability: {:.2f}".format(prediction_proba[0][0])
    else:
        prediction_text = "Diabetes: Negative, Probability: {:.2f}".format(1 - prediction_proba[0][0])

    # Pass the prediction, raw prediction value, and form data back to the template
    return render_template("home.html", prediction=prediction_text, prediction_value=prediction_proba[0][0], form_data=form_data)

if __name__ == "__main__":
    flask_app.run(debug=True)
