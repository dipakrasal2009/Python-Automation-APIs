# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

# Step 1: Load the Iris dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
data = pd.read_csv(url, header=None, names=column_names)

# Display first few rows of the dataset
print("Dataset:\n", data.head())

# Step 2: Preprocess the dataset for Apriori (OneHotEncoding)
# We are focusing on the 'class' column (i.e., target column) for simplicity.

# Convert class labels into one-hot encoding
encoder = OneHotEncoder(sparse=False)
encoded_class = encoder.fit_transform(data[['class']])

# Convert the encoded class data back to a DataFrame and add feature names
encoded_class_df = pd.DataFrame(encoded_class, columns=encoder.categories_[0])

# Concatenate the features with the encoded class labels
data_encoded = pd.concat([data.drop(columns=['class']), encoded_class_df], axis=1)

# Display the preprocessed data
print("\nPreprocessed Data:\n", data_encoded.head())

# Step 3: Apply the Apriori algorithm to find frequent item sets
# We use a threshold of min_support (you can adjust this value)
frequent_itemsets = apriori(data_encoded, min_support=0.2, use_colnames=True)

# Step 4: Generate Association Rules
# We can extract the rules with a minimum confidence threshold
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Display the generated rules
print("\nGenerated Association Rules:\n", rules)

# Optional: Visualize the frequent itemsets (optional)
import matplotlib.pyplot as plt
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
plt.figure(figsize=(10, 6))
frequent_itemsets.groupby('length').size().plot(kind='bar')
plt.title('Frequent Itemsets Length Distribution')
plt.xlabel('Length of Itemsets')
plt.ylabel('Count of Itemsets')
plt.show()

