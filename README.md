# 💎 Diamond Final Weight Prediction using Machine Learning

A Machine Learning web application built with **Python**, **Random Forest Regression**, and **Streamlit** to predict the **final polished diamond weight (carats)** from rough diamond characteristics.

---

## 📌 Project Overview

The diamond manufacturing process involves cutting and polishing rough diamonds, which reduces their original weight. Predicting the final polished weight helps manufacturers estimate yield, pricing, and production planning.

This project uses a **Random Forest Regression** model trained on diamond attributes to accurately predict the **Final Weight (ct)**.

---

## 🚀 Features

- Predict final polished diamond weight
- User-friendly Streamlit interface
- Machine Learning using Random Forest Regression
- Automatic preprocessing with Pipeline
- One-Hot Encoding for categorical features
- Model saved using Joblib
- Recovery Percentage Calculation
- Fast and accurate predictions

---

## 🛠️ Tech Stack

- Python 3.x
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Joblib

---

## 📂 Project Structure

```
Diamond_Weight_Prediction/
│
├── app.py
├── train_model.py
├── diamond_data.csv
├── diamond_weight_model.pkl
├── requirements.txt
├── README.md
└── images/
    └── screenshot.png
```

---

## 📊 Dataset

The dataset contains approximately **5000 diamond records**.

### Features

| Feature | Description |
|----------|-------------|
| Rough_Weight | Rough diamond weight (ct) |
| Shape | Diamond shape |
| Length_mm | Length in millimeters |
| Width_mm | Width in millimeters |
| Height_mm | Height in millimeters |
| Color | Diamond color grade |
| Clarity | Diamond clarity grade |
| Crack_Level | Crack severity |
| Cut_Type | Cut type |
| Final_Weight_ct | Target variable |

---

## 🤖 Machine Learning Model

This project uses:

**Random Forest Regressor**

Why Random Forest?

- Handles nonlinear relationships
- High prediction accuracy
- Works well with mixed data types
- Robust against overfitting
- No feature scaling required

---

## 📈 Model Evaluation

The model is evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

Example:

```
MAE   : 0.03
RMSE  : 0.05
R²    : 0.98
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Diamond-Weight-Prediction.git
```

Move into the project

```bash
cd Diamond-Weight-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
python train_model.py
```

This creates

```
diamond_weight_model.pkl
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💻 Application Preview

The application allows users to:

- Enter rough diamond details
- Select shape
- Select color
- Select clarity
- Select crack level
- Select cut type
- Predict final polished weight
- View recovery percentage

---

## 📌 Example Prediction

### Input

| Feature | Value |
|----------|-------|
| Rough Weight | 3.50 ct |
| Shape | Round |
| Length | 8.90 mm |
| Width | 8.55 mm |
| Height | 5.95 mm |
| Color | F |
| Clarity | VS1 |
| Crack Level | Low |
| Cut Type | Brilliant |

### Output

```
Predicted Final Weight

1.54 ct

Recovery Percentage

44.00%
```

---

## 📊 Workflow

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
One-Hot Encoding
   │
   ▼
Train-Test Split
   │
   ▼
Random Forest Regression
   │
   ▼
Model Evaluation
   │
   ▼
Save Model (.pkl)
   │
   ▼
Streamlit Web App
```

---

## 📦 Dependencies

```
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## 📈 Future Improvements

- XGBoost Regressor
- CatBoost Regressor
- Hyperparameter Tuning
- SHAP Feature Importance
- Model Comparison Dashboard
- CSV Batch Prediction
- Export Prediction Report
- Database Integration

---

## 👨‍💻 Author

**Raval Pratik**

BCA (Artificial Intelligence)

Vivekanand College

---

## 📄 License

This project is created for educational and research purposes.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

### Made with ❤️ using Python, Scikit-Learn, and Streamlit.
