import pandas as pd
from scipy.stats import pearsonr

def load_data(path="data/car_data.csv"):
    """Load and clean the car dataset."""
    df = pd.read_csv(path)
    # Drop rows with missing critical values
    df = df.dropna(subset=["price", "year", "mileage"])
    # Convert types
    df["price"] = df["price"].astype(float)
    df["year"] = df["year"].astype(int)
    df["mileage"] = df["mileage"].astype(float)
    return df

def mileage_price_correlation(df):
    """Compute Pearson correlation between mileage and price."""
    corr, pval = pearsonr(df["mileage"], df["price"])
    print(f"Pearson r={corr:.2f}, p={pval:.3e}")
