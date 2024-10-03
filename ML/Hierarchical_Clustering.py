# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch

# Step 1: Load the Wholesale Customers dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/wholesale-customers-data.csv'
data = pd.read_csv(url)

# Display the first few rows of the dataset
print("Dataset Head:\n", data.head())

# Step 2: Preprocess the dataset
# The dataset does not have labels, so we will focus on feature scaling.
# Check for missing values
print("\nMissing values in the dataset:\n", data.isnull().sum())

# Step 3: Feature scaling (Standardization)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Step 4: Apply Hierarchical Clustering using Agglomerative Clustering
# Create the linkage matrix using scipy
dendrogram = sch.dendrogram(sch.linkage(data_scaled, method='ward'))

# Step 5: Create the Agglomerative Clustering model
# Let's assume we want to create 5 clusters (you can change this based on your dendrogram)
model = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')

# Fit the model and get the cluster labels
cluster_labels = model.fit_predict(data_scaled)

# Step 6: Add the cluster labels to the original dataset
data['Cluster'] = cluster_labels

# Display the dataset with cluster labels
print("\nDataset with Cluster Labels:\n", data.head())

# Step 7: Visualize the clusters (for simplicity, we will visualize the first two features)
plt.figure(figsize=(10, 6))
plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=cluster_labels, cmap='viridis')
plt.title('Hierarchical Clustering of Wholesale Customers')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()


