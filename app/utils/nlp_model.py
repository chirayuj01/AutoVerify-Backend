import joblib
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "..", "..", "model", "scam_detector.joblib")
model = joblib.load(model_path)

# Predict scam or not
def predict_scam(text):
    prediction = model.predict([text])[0]                 # 0 or 1
    proba = model.predict_proba([text])[0][1]             # Probability of being scam
    return {
        "scam": bool(prediction),
        "confidence": round(proba, 2)
    }
