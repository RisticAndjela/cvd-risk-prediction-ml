import joblib
import pandas as pd
import json
import os
from .patient_model import Patient

class Predictor:
    def __init__(self, model_path, scaler):
        self.model = joblib.load(model_path)
        self.scaler = scaler

        if os.path.exists("./models/trained/train_columns.json"):
            with open("./models/trained/train_columns.json", "r") as f:
                self.train_columns = json.load(f)
        else:
            self.train_columns = None

    def predict(self, patient: Patient | dict):
        if isinstance(patient, dict):
            data = pd.DataFrame([patient])
        else: 
            data = pd.DataFrame([patient.dict(exclude={"id", "cardio"})])

        if self.train_columns:
            data = data[self.train_columns]

        numeric_features = ["age", "height", "weight", "ap_hi", "ap_lo", "gluc", "BMI", "ap_ratio"]
        data[numeric_features] = self.scaler.transform(data[numeric_features])

        pred = self.model.predict(data)[0]
        prob = self.model.predict_proba(data)[0, 1]
        return int(pred), float(prob)
