import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), "..", "..", "model", "scam_detector.joblib")
model = joblib.load(model_path)

def predict_scam(text):
    prediction = model.predict([text])[0]                
    proba = model.predict_proba([text])[0][1]             
    return {
        "scam": bool(prediction),
        "confidence": round(proba, 2)
    }
