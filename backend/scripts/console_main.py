from models.dataset_loader import DatasetLoader
from models.model_trainer import ModelTrainer

def main():
    loader = DatasetLoader()
    train, val, test = loader.get_datasets()

    X_train = train.drop(columns=["id","cardio"])
    y_train = train["cardio"]
    X_val = val.drop(columns=["id","cardio"])
    y_val = val["cardio"]

    print("Trening modela...")
    trainer = ModelTrainer()
    model, metrics = trainer.train_and_evaluate("random_forest", X_train, y_train, X_val, y_val)
    trainer.save_model(model, "./models/random_forest.joblib")
    print(metrics)
    
if __name__ == "__main__":
    main()
