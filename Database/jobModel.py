from app import db
from datetime import datetime
import pytz

UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')

class JobModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=False)
    scam = db.Column(db.Boolean, default=False)
    confidence = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))

    def serialize(self):
        ist_time = self.created_at.replace(tzinfo=UTC).astimezone(IST)
        return {
            "id": self.id,
            "description": self.description,
            "scam": self.scam,
            "confidence": self.confidence,
            "created_at": ist_time.strftime("%I:%M %p, %d-%m-%Y")
        }

    def __repr__(self):
        return f"<Job {self.id} - Scam: {self.scam}, Confidence: {self.confidence}>"
