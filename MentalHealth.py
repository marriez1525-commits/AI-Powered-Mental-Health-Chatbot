from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("models/mental_health_model.joblib")
vectorizer = joblib.load("models/tfidf_vectorizer (2).joblib")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    text = data.get("message", "")

    if not text.strip():
        return jsonify({"error": "Empty input"})

    # preprocess
    clean_text = text.lower()

    # vectorize
    vec = vectorizer.transform([clean_text])

    # predict
    pred = model.predict(vec)[0]
    proba = model.predict_proba(vec)[0]

    confidence = round(max(proba) * 100, 2)

    # response
    response = str(pred)

    # mental health advice layer
    advice = ""
    if "depress" in response.lower():
        advice = "You may be experiencing depression. Please talk to someone you trust ❤️"
        color = "#ff0033"
    elif "anxiety" in response.lower():
        advice = "Signs of anxiety detected. Try deep breathing 🧘"
        color = "#ffcc00"
    elif "stress" in response.lower():
        advice = "Stress detected. Take a short break 😌"
        color = "#ff6600"
    else:
        advice = "Your mental state seems stable 👍"
        color = "#00ff88"

    return jsonify({
        "response": response,
        "confidence": confidence,
        "advice": advice,
        "color": color
    })


if __name__ == "__main__":
    app.run(debug=True)