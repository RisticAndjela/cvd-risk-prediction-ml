import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import os

class DatasetLoader:
    def __init__(self, data_dir="./data"):
        self.data_dir = data_dir
        self.scaler = StandardScaler()

    def load_data(self, subset="train"):
        path = os.path.join(self.data_dir, f"{subset}_data.csv")
        df = pd.read_csv(path, sep=",")
        return df

    def preprocess(self, df, fit_scaler=False):
        # numeričke kolone za skaliranje i imputaciju
        numeric_features = ["age", "height", "weight", "ap_hi", "ap_lo", "gluc"]
        # kategorijske kolone su numeričke, samo imputacija
        categorical_features = ["gender", "cholesterol", "smoke", "alco", "active"]

        # imputacija numeričkih
        num_imputer = SimpleImputer(strategy="median")
        df[numeric_features] = num_imputer.fit_transform(df[numeric_features])

        # imputacija "kategorijskih" koje su numeričke
        cat_imputer = SimpleImputer(strategy="most_frequent")
        df[categorical_features] = cat_imputer.fit_transform(df[categorical_features])

        # skaliranje samo numeričkih
        if fit_scaler:
            df[numeric_features] = self.scaler.fit_transform(df[numeric_features])
        else:
            df[numeric_features] = self.scaler.transform(df[numeric_features])

        return df

    def get_datasets(self):
        train = self.load_data("train")
        val = self.load_data("validation")
        test = self.load_data("test")

        train = self.preprocess(train, fit_scaler=True)
        val = self.preprocess(val)
        test = self.preprocess(test)

        return train, val, test
