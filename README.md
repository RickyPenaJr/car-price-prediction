# Car Price Prediction 🚗💰

A simple end-to-end project demonstrating data loading, cleaning, exploratory analysis, statistical testing, and modeling for used car price prediction.

---

## 📥 Dataset

1. Download the **Used Car Price Prediction** CSV from Kaggle:  
   https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset  
2. Rename it to `used_cars.csv` and place it in:  
   ```
   car-price-prediction/
   └─ data/used_cars.csv
   ```

---

## 📂 Project Structure

```
car-price-prediction/
│
├─ data/
│   └─ used_cars.csv               # Your Kaggle download
│
├─ notebooks/
│   └─ car_price_exploration.ipynb # EDA & visualizations
│
├─ src/
│   ├─ data_processing.py          # Load + stats functions
│   └─ model.py                    # Train & evaluate
│
├─ LICENSE                        # MIT License
├─ .gitignore                     # Ignore venv, caches, CSV
├─ README.md                      # You’re looking at it!
└─ requirements.txt               # pip install -r requirements.txt
```

---

## 🛠️ Setup

```bash
git clone https://github.com/<your-username>/car-price-prediction.git
cd car-price-prediction

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```



## 🚀 Usage

- **Notebook:**  
  Open and run  
  ```
  notebooks/car_price_exploration.ipynb
  ```  
  to explore the data, view histograms, scatter plots, etc.

- **Quick Stats & Correlation:**  
  ```bash
  python -c "from src.data_processing import load_data, mileage_price_correlation; df = load_data(); mileage_price_correlation(df)"
  ```

- **Train & Evaluate Model:**  
  ```bash
  python -c "from src.model import train_and_evaluate; train_and_evaluate()"
  ```
  Prints RMSE on the test split.



## 🤝 Contributing

Feel free to open issues or PRs to:  
- Add more features or predictors  
- Try different models 
- Write unit tests or improve docs
<br>
<br>



## ⚖️ License

This project is MIT-licensed. See [LICENSE](LICENSE) for details.


## 🏷️ GitHub Topics
`#python` `#data-analysis` `#data-visualization` `#machine-learning` `#regression` `#linear-regression` `#pandas` `#numpy` `#scipy` `#matplotlib` `#scikit-learn` `#jupyter-notebook` `#exploratory-data-analysis` `#car-price-prediction`
<br>


## 👤 Author

**Ricky Peña Jr.**  
🌐 [rickypenajr.github.io](https://rickypenajr.github.io)  
🔗 [GitHub](https://github.com/rickypenajr) • [LinkedIn](https://linkedin.com/in/rickypenajr)
