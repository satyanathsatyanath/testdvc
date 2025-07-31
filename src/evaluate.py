import pandas as pd
import joblib
import json
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def evaluate(input_path, model_path, metrics_path):
    df = pd.read_csv(input_path)
    X = df.drop(columns=["customerID", "Churn"])
    y = df["Churn"]

    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = joblib.load(model_path)
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    with open(metrics_path, "w") as f:
        json.dump({"accuracy": acc}, f)

if __name__ == "__main__":
    evaluate("data/preprocessed.csv", "models/model.pkl", "metrics.json")

