import os
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score

class ModelTrainer:
    def __init__(self):
        self.models = {
            "logistic_regression": LogisticRegression(max_iter=5000),
            "random_forest": RandomForestClassifier(
                n_estimators=500, max_depth=None, random_state=42, n_jobs=-1
            ),
            "xgboost": XGBClassifier(
                n_estimators=500, max_depth=None, learning_rate=0.05, use_label_encoder=False, eval_metric="logloss", random_state=42, n_jobs=-1, tree_method="hist"
            ),
        }

    def train_and_evaluate(self, model_name, X_train, y_train, X_val, y_val):
        model = self.models[model_name]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        y_proba = model.predict_proba(X_val)[:, 1]

        metrics = {
            "accuracy": accuracy_score(y_val, y_pred),
            "f1_score": f1_score(y_val, y_pred),
            "precision": precision_score(y_val, y_pred),
            "recall": recall_score(y_val, y_pred),
            "roc_auc": roc_auc_score(y_val, y_proba),
        }

        return model, metrics

    def save_model(self, model, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(model, path)
