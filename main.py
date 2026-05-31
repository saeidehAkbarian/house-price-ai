from sklearn.linear_model import LinearRegression

# X = house size (square meters)
X = [
    [50],
    [70],
    [100],
    [120],
    [150]
]

# y = price in billion Toman
y = [
    7500,
    10500,
    15000,
    18000,
    22500
]

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction (test input)
house_size = 110
predicted_price = model.predict([[house_size]])

print("Predicted price for", house_size, "sqm:", predicted_price[0], "billion Toman")
