import json
import joblib
from sklearn.preprocessing import StandardScaler
from models.dataset_loader import DatasetLoader
from models.model_trainer import ModelTrainer

def main():
    loader = DatasetLoader()
    train, val, test = loader.get_datasets()

    X_train = train.drop(columns=["id", "cardio"])
    y_train = train["cardio"]
    X_val = val.drop(columns=["id", "cardio"])
    y_val = val["cardio"]

    print("🔧 Skaliranje numeričkih kolona...")
    numeric_features = ["age", "height", "weight", "ap_hi", "ap_lo", "gluc"]
    scaler = StandardScaler()
    X_train[numeric_features] = scaler.fit_transform(X_train[numeric_features])
    X_val[numeric_features] = scaler.transform(X_val[numeric_features])

    joblib.dump(scaler, "./models/scaler.joblib")

    print("🔧 Trening modela...")
    trainer = ModelTrainer()

    results = {}

    for model_name in ["logistic_regression", "random_forest", "xgboost"]:
        print(f"\n🧠 Treniram model: {model_name}")
        model, metrics = trainer.train_and_evaluate(model_name, X_train, y_train, X_val, y_val)
        trainer.save_model(model, f"./models/{model_name}.joblib")
        results[model_name] = metrics

    with open("./models/train_columns.json", "w") as f:
        json.dump(list(X_train.columns), f)

    print("\n✅ Trening završen. Rezultati:")
    for name, metrics in results.items():
        print(f"\nModel: {name}")
        for m, v in metrics.items():
            print(f"  {m}: {v:.4f}")

if __name__ == "__main__":
    main()
