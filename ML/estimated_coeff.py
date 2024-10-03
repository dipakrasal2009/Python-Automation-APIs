# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Given data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)  # Reshape for sklearn
y = np.array([7, 14, 15, 18, 19, 21, 26, 23])

# Create the Linear Regression model
model = LinearRegression()

# Fit the model with the data
model.fit(x, y)

# Make predictions
y_pred = model.predict(x)

# Estimated coefficients
b0 = model.intercept_   # Intercept (b0)
b1 = model.coef_[0]     # Slope (b1)

# Output the coefficients
print(f"Estimated Coefficients:\nIntercept (b0): {b0}\nSlope (b1): {b1}")

# Model performance
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"\nModel Performance:\nMean Squared Error: {mse}\nR-squared: {r2}")

# Visualize the regression line
plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x, y_pred, color='red', label='Regression line')
plt.title('Simple Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

