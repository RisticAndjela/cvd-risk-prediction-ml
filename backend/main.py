import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.patient_model import Patient
from models.predictor import Predictor

app = FastAPI(title="Cardiovascular Risk Predictor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BodyRequest(BaseModel):
    model: str
    patient: Patient

models = {}

@app.get("/")
def home():
    return {"message": "Cardio predictor API is running!"}

@app.post("/predict")
def predict(body: BodyRequest):
    try:
        model_name = body.model or "random_forest"
        if model_name not in ["random_forest", "xgboost", "logistic_regression"]:
            return {"error": f"Model {model_name} not found."}

        # 🔹 Lazy loading — učitaj model samo prvi put
        if model_name not in models:
            print(f"🧠 Učitavam model: {model_name}")
            models[model_name] = Predictor(model_path=f"./models/{model_name}.joblib")

        predictor = models[model_name]
        print("🧩 Primljen pacijent:", body.patient.dict())

        prediction, probability = predictor.predict(body.patient)
        probability *= 100

        return {
            "model": model_name,
            "prediction": "Most likely to have CVD" if prediction == 1 else "Most likely not to have CVD",
            "probability": f"Chances are: {probability:.2f}%"
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}

@app.get("/evaluate")
def evaluate(model: str = "random_forest", dataset: str = "test"):
    try:
        from models.predictor import Predictor
        if model not in models:
            model_path = f"./models/{model}.joblib"
            if not os.path.exists(model_path):
                return {"error": f"Model {model} file not found."}
            models[model] = Predictor(model_path=model_path)

        from models.dataset_loader import DatasetLoader
        from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score

        from sklearn.impute import SimpleImputer
        import joblib

        loader = DatasetLoader()
        df = loader.load_data(dataset)

        numeric_features = ["age", "height", "weight", "ap_hi", "ap_lo", "gluc"]
        categorical_features = ["gender", "cholesterol", "smoke", "alco", "active"]

        num_imputer = SimpleImputer(strategy="median")
        cat_imputer = SimpleImputer(strategy="most_frequent")

        df[numeric_features] = num_imputer.fit_transform(df[numeric_features])
        df[categorical_features] = cat_imputer.fit_transform(df[categorical_features])

        scaler = joblib.load("./models/scaler.joblib")
        df[numeric_features] = scaler.transform(df[numeric_features])

        X = df.drop(columns=["id", "cardio"])
        y = df["cardio"]


        predictor = models[model]
        preds = predictor.model.predict(X)
        probas = predictor.model.predict_proba(X)[:, 1]

        metrics = {
            "accuracy": accuracy_score(y, preds),
            "f1_score": f1_score(y, preds),
            "precision": precision_score(y, preds),
            "recall": recall_score(y, preds),
            "roc_auc": roc_auc_score(y, probas),
        }

        return {
            "model": model,
            "dataset": dataset,
            "metrics": metrics
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}
