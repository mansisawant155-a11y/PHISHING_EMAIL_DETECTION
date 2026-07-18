from flask import Flask, render_template, request, jsonify
import joblib

# -----------------------------
# Flask App
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Load Trained Model
# -----------------------------
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Predict Email
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    email = data.get("email", "")

    if email.strip() == "":
        return jsonify({
            "prediction": "No Email Entered",
            "confidence": 0
        })

    # Convert email into TF-IDF features
    email_vector = vectorizer.transform([email])

    # Prediction
    prediction = model.predict(email_vector)[0]

    # Probability
    probability = model.predict_proba(email_vector)[0]

    confidence = round(max(probability) * 100, 2)

    # Convert numeric label to text
    if prediction == 1:
        result = "Phishing"
    else:
        result = "Safe"

    return jsonify({
        "prediction": result,
        "confidence": confidence
    })


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)