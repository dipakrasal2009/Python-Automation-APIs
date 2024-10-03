# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# Load dataset from GitHub (example raw link to Customer.csv)
url = 'https://github.com/tarunlnmiit/machine_learning/blob/master/DataPreprocessing.csv'
data = pd.read_csv(url,on_bad_lines='skip', sep=';', encoding='utf-8', nrows=10)
print(data)

# Display the first few rows of the dataset
print(data.head())

# Select the relevant columns for clustering (e.g., Annual Income and Spending Score)
X = data.iloc[:, [3, 4]].values  # Assuming 'Annual Income' and 'Spending Score' are the 3rd and 4th columns

# Visualize the dendrogram to find the optimal number of clusters
plt.figure(figsize=(10, 7))
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean distances")
plt.show()

# Fit the hierarchical clustering algorithm to the dataset
# The number of clusters can be chosen based on the dendrogram
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(X)

# Visualize the clusters
plt.figure(figsize=(10, 7))
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s=100, c='cyan', label='Cluster 4')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s=100, c='magenta', label='Cluster 5')

plt.title("Clusters of customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()

