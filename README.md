# Car Price Prediction

A simple end-to-end project demonstrating data loading, cleaning, exploratory analysis, statistical testing, and modeling for used car price prediction.

## Project Structure
```
car-price-prediction/
│
├─ data/
│   └─ car_data.csv         # Downloaded from Kaggle
│
├─ notebooks/
│   └─ car_price_exploration.ipynb  # EDA notebook
│
├─ src/
│   ├─ data_processing.py   # Data loading & stats
│   └─ model.py             # Training & evaluation
│
├─ LICENSE
├─ .gitignore
├─ README.md
└─ requirements.txt
```

## Setup
```bash
git clone https://github.com/yourusername/car-price-prediction.git
cd car-price-prediction
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Usage
- **Notebook:** Open `notebooks/car_price_exploration.ipynb` to run EDA and visualizations.
- **Scripts:**  
  ```bash
  python -c "from src.data_processing import load_data, mileage_price_correlation; df = load_data(); mileage_price_correlation(df)"
  python -c "from src.model import train_and_evaluate; train_and_evaluate()"
  ```

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
