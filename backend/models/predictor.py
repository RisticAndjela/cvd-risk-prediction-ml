import joblib
import pandas as pd
from .patient_model import Patient

class Predictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, patient: Patient):
        # pretvaranje pacijenta u DataFrame
        data = pd.DataFrame([patient.dict(exclude={"id", "cardio"})])
        pred = self.model.predict(data)[0]
        prob = self.model.predict_proba(data)[0,1]
        return {"prediction": int(pred), "probability": float(prob)}
