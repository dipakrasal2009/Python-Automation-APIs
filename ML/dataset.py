from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB
import numpy as np

# Given dataset
weather = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

# Encoding the categorical variables into numeric values
le_weather = LabelEncoder()
le_temp = LabelEncoder()
le_play = LabelEncoder()

weather_encoded = le_weather.fit_transform(weather)
temp_encoded = le_temp.fit_transform(temp)
play_encoded = le_play.fit_transform(play)

# Combining features
features = np.array(list(zip(weather_encoded, temp_encoded)))

# Creating Naive Bayes model
model = CategoricalNB()
model.fit(features, play_encoded)

# Test data: [0: Overcast, 2: Mild]
test_data = np.array([[0, 2]])  # [Overcast, Mild] as per encoded values

# Prediction
predicted = model.predict(test_data)

# Output the prediction result
result = le_play.inverse_transform(predicted)
print(f"The predicted class for [Overcast, Mild] is: {result[0]}")

