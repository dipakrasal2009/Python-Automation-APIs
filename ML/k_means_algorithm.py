# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the dataset (you can change the path as per your local file)
url = 'https://github.com/tarunlnmiit/machine_learning/blob/master/DataPreprocessing.csv'
data = pd.read_csv(url)

# Display the first few rows of the dataset
print(data.head())

# Preprocess the dataset
# Check for missing values
print(data.isnull().sum())

# Handle missing values (for simplicity, we will fill with mean for this example)
data.fillna(data.mean(), inplace=True)

# Drop the 'CUST_ID' column, as it is just an identifier
data = data.drop('CUST_ID', axis=1)

# Feature scaling: Standardize the data for better K-Means performance
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Choosing the optimal number of clusters using the Elbow Method
wcss = []  # Within-cluster sum of squares
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(data_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Method graph
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Applying K-Means to the dataset
# Let's assume the optimal number of clusters from the Elbow Method is 4 (you can adjust based on your plot)
kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=42)
y_kmeans = kmeans.fit_predict(data_scaled)

# Add the cluster labels to the original dataset
data['Cluster'] = y_kmeans

# Display the first few rows with the cluster labels
print(data.head())

# Evaluate the clustering with the silhouette score
sil_score = silhouette_score(data_scaled, y_kmeans)
print(f'Silhouette Score: {sil_score}')

# Visualizing the clusters (for simplicity, we will use the first two principal components)
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

plt.figure(figsize=(10, 6))
plt.scatter(data_pca[:, 0], data_pca[:, 1], c=y_kmeans, cmap='viridis', s=50)
plt.title('Clusters of Credit Card Customers')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.show()

