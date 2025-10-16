import pandas as pd
from sklearn.impute import SimpleImputer
import os

class DatasetLoader:
    def __init__(self, data_dir="./data"):
        self.data_dir = data_dir

    def load_data(self, subset="train"):
        path = os.path.join(self.data_dir, f"{subset}_data.csv")
        df = pd.read_csv(path, sep=",")
        return df

    def preprocess(self, df):
        numeric_features = ["age", "height", "weight", "ap_hi", "ap_lo", "gluc", "BMI", "ap_ratio"]
        categorical_features = ["gender", "cholesterol", "smoke", "alco", "active"]

        num_imputer = SimpleImputer(strategy="median")
        cat_imputer = SimpleImputer(strategy="most_frequent")

        df[numeric_features] = num_imputer.fit_transform(df[numeric_features])
        df[categorical_features] = cat_imputer.fit_transform(df[categorical_features])

        return df

    def get_datasets(self):
        train = self.load_data("train")
        val = self.load_data("validation")
        test = self.load_data("test")

        train = self.preprocess(train)
        val = self.preprocess(val)
        test = self.preprocess(test)

        return train, val, test
