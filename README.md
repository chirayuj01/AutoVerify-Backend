# 🛡️ AutoVerify – Scam Job & Internship Detector API
AutoVerify is a Flask-based REST API that uses machine learning to detect fake job or internship descriptions. It helps users verify suspicious offers, store predictions, and view past results — all with Indian Standard Time timestamps.
## 📦 Features
- 🔍 Detect fake job/internship descriptions
- 🧠 Powered by ML (TF-IDF + Logistic Regression)
- 🕒 Timestamps in IST (Indian Standard Time)
- 🗂️ Stores every verification in a database
- 🔔 Optional Windows desktop notification for scams
## 📁 File Structure
```
AutoVerify/
├── app.py
├── train_model.py
├── scam_detector.joblib
├── requirements.txt
├── README.md
├── Database/
│   └── jobModel.py
└── app/
    ├── __init__.py
    └── utils/
        ├── nlp_model.py
        └── scam_features.py
```
## 🌐 API Usage
### `GET /`
Returns a welcome message.
```json
{ "message": "Welcome to AutoVerify API" }
```
### `GET /verify?description=...`
Submits a job description and receives prediction. If not already present, stores it.
```json
{
  "scam": true,
  "confidence": 0.94
}
```
### `GET /show-data`
Returns all stored records of verified job descriptions.
```json
[
  {
    "id": 1,
    "description": "Earn ₹5000/day, no experience needed!",
    "scam": true,
    "confidence": 0.94,
    "created_at": "01:39 PM, 05-07-2025"
  }
]
```
### `GET /get-by-id/<int:id>`
Fetch a specific record by ID.
```json
{
  "id": 1,
  "description": "...",
  "scam": false,
  "confidence": 0.72,
  "created_at": "02:00 PM, 05-07-2025"
}
```
### `GET /delete/<int:id>`
Deletes a record by ID.
```json
{ "message": "Deleted successfully" }
```
## 📌 Notes
- Uses SQLite via SQLAlchemy.
- Model predictions stored with IST timestamp.
- Python 3.10+ recommended.
