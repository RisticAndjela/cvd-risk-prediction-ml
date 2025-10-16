import pandas as pd
from sklearn.model_selection import train_test_split

# load dataset
df = pd.read_csv("./data/cardio_dataset.csv", sep=";")

# create new features
df["BMI"] = df["weight"] / (df["height"]/100)**2
df["ap_lo"] = df["ap_lo"].replace(0, df["ap_lo"].median())
df["ap_ratio"] = df["ap_hi"] / df["ap_lo"]

# fill NaNs
df.fillna(df.median(numeric_only=True), inplace=True)
for col in ["gender", "cholesterol", "smoke", "alco", "active"]:
    df[col] = df[col].fillna(df[col].mode()[0])

# features and target
X = df.drop(columns=["cardio"])
y = df["cardio"]

# split into train / validation / test
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42
)

# save CSVs
train_data = X_train.copy()
train_data["cardio"] = y_train.values
train_data.to_csv("./data/train_data.csv", index=False)

val_data = X_val.copy()
val_data["cardio"] = y_val.values
val_data.to_csv("./data/validation_data.csv", index=False)

test_data = X_test.copy()
test_data["cardio"] = y_test.values
test_data.to_csv("./data/test_data.csv", index=False)