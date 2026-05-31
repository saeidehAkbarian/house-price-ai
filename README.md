#  House Price Prediction (Machine Learning Project)

## 📌 Overview
This project is a simple Machine Learning model that predicts house prices based on house size using Linear Regression.

The goal of this project is to demonstrate basic Machine Learning workflow including data preparation, model training, and prediction.

---

## 📊 Dataset

The dataset is manually created based on approximate real-world market values in Central Tehran  Iran for residential new apartments.

- **Input (X):** House size in square meters (sqm)
- **Output (y):** Price in billion Toman

### Sample Data:

50 sqm → 7500 billion Toman  
70 sqm → 10500 billion Toman  
100 sqm → 15000 billion Toman  
120 sqm → 18000 billion Toman  
150 sqm → 22500 billion Toman  

---

## 🤖 Model Used

- Algorithm: Linear Regression  
- Library: scikit-learn  

The model learns a linear relationship between house size and price and uses it to make predictions for unseen data.

---

## ⚙️ How It Works

1. Define dataset (house size and price)
2. Train Linear Regression model using `fit()`
3. Input a new house size
4. Predict price using trained model

---

## ▶️ Example Output

When running the program:

Input: 110 sqm  
📌 Output: 16500.0 billion Toman

---

##  Key Concepts Demonstrated

- Machine Learning basics
- Regression model (Linear Regression)
- Data representation (X and y)
- Model training process
- Prediction workflow

---

##  Purpose

This project was built for learning and portfolio purposes to demonstrate understanding of basic Machine Learning concepts and Python implementation.

---

##  Tech Stack

- Python
- scikit-learn
