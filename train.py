import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv('data/housing.csv')

X = df[['area', 'bedrooms']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'model.pkl')
print("Model trained and saved.")
