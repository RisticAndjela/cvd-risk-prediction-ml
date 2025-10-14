import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# load dataset
df = pd.read_csv("./backend/data/cardio_dataset.csv", sep=";")

# columns
numerical_cols = ["age", "height", "weight", "ap_hi", "ap_lo", "gluc"]
categorical_cols = ["gender", "cholesterol", "smoke", "alco", "active"]

# fill missing values
for col in numerical_cols:
    df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# features and target
X = df.drop(columns=["cardio"])
y = df["cardio"]

# scale num features
scaler = StandardScaler()
X[numerical_cols] = scaler.fit_transform(X[numerical_cols])

# split into train / validation / test
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42
)

# combine and save
train_data = X_train.copy()
train_data["cardio"] = y_train.values
train_data.to_csv("./backend/data/train_data.csv", index=False)

val_data = X_val.copy()
val_data["cardio"] = y_val.values
val_data.to_csv("./backend/data/validation_data.csv", index=False)

test_data = X_test.copy()
test_data["cardio"] = y_test.values
test_data.to_csv("./backend/data/test_data.csv", index=False)
