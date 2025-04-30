import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from src.data_processing import load_data

def train_and_evaluate():
    """Train a linear regression model and print RMSE."""
    df = load_data()
    X = df[["year", "mileage"]]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    preds = model.predict(X_test)
    rmse = mean_squared_error(y_test, preds, squared=False)
    print(f"Test RMSE: ${rmse:,.0f}")
