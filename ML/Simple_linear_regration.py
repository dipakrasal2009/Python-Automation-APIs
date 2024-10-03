# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Step 1: Load the dataset (assuming the file has been downloaded and saved locally)
# For Google Drive links, you'd normally need to download the file manually and load it here.
# Uncomment the code below if the dataset is locally available as a CSV file.

# dataset_url = "your_downloaded_file_path.csv" 
# df = pd.read_csv(dataset_url)

# Example dataset for demonstration purposes:
data = {
    'Hours_Studied': [2, 3, 5, 7, 9, 10, 4, 6, 1, 8],
    'Scores': [20, 25, 50, 65, 85, 90, 45, 60, 15, 80]
}
df = pd.DataFrame(data)

# Step 2: Split the dataset into features (X) and target (y)
X = df[['Hours_Studied']]  # Independent variable
y = df['Scores']  # Dependent variable

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 6: Calculate the evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Step 7: Print the results
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)

