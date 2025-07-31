import pandas as pd
import joblib
import yaml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

with open("params.yaml") as f:
    params = yaml.safe_load(f)["train"]

def train(input_path, model_path):
    df = pd.read_csv(input_path)

    X = df.drop(columns=["customerID", "Churn"])
    y = df["Churn"]

    X_train, _, y_train, _ = train_test_split(
        X, y, test_size=params["test_size"], random_state=params["random_state"]
    )

    model = LogisticRegression(max_iter=params["max_iter"])
    model.fit(X_train, y_train)

    joblib.dump(model, model_path)

if __name__ == "__main__":
    train("data/preprocessed.csv", "models/model.pkl")
