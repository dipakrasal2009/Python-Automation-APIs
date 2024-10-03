import numpy as np

# Given data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12, 16, 18])

# Number of observations
n = len(x)

# Calculating the means of x and y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Calculating the coefficients b1 and b0
numerator = np.sum((x - mean_x) * (y - mean_y))
denominator = np.sum((x - mean_x)**2)
b1 = numerator / denominator
b0 = mean_y - b1 * mean_x

# Display the results
print(f"Estimated coefficients:\n b0 (intercept) = {b0:.4f}\n b1 (slope) = {b1:.4f}")

