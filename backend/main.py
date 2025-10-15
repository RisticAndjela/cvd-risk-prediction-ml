from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.patient_model import Patient
from models.predictor import Predictor

app = FastAPI(title="Cardiovascular Risk Predictor API")
predictor = Predictor(model_path="./models/random_forest.joblib")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:4200"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
def home():
    return {"message": "Cardio predictor API is running!"}

@app.post("/predict")
def predict(patient: Patient):
    try:
        result = predictor.predict(patient)
        return {
            "prediction": "Has cardiovascular disease" if result["prediction"] == 1 else "No cardiovascular disease",
            "probability": round(result["probability"], 4)
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}
