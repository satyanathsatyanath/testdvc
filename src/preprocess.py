import pandas as pd
import os

def preprocess(input_path, output_path):
    df = pd.read_csv(input_path)

    # Simple processing: drop rows with missing values
    df = df.dropna()

    # Convert categorical columns to numeric (simplified)
    df['gender'] = df['gender'].map({'Male': 0, 'Female': 1})
    df['Partner'] = df['Partner'].map({'No': 0, 'Yes': 1})
    df['Dependents'] = df['Dependents'].map({'No': 0, 'Yes': 1})
    df['PhoneService'] = df['PhoneService'].map({'No': 0, 'Yes': 1})
    df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})

    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess("data/churn.csv", "data/preprocessed.csv")

