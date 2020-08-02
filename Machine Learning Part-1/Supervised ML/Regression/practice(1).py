from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Read the CSV Dataset
df = pd.read_csv('boston.csv')
# df.set_index('CHAS', inplace=True)
# (df.head())

# slice data which we want to predict
X = df.drop('MEDV', axis=1).values
y = df['MEDV'].values
X_rooms = X[:, 5]

# Reshape the Array Data
y = y.reshape(-1, 1)
X_rooms = X_rooms.reshape(-1, 1)

# Create a object of Linear Regression and predict it
reg = LinearRegression()
reg.fit(X_rooms, y)
prediction_shape = np.linspace(min(X_rooms), max(X_rooms)).reshape(-1, 1)
print(prediction_shape)

# Show or view in Graph using Matplotlib package
plt.scatter(X_rooms, y, color='blue')
plt.scatter(prediction_shape, reg.predict(prediction_shape), marker='o', linewidths=3)
plt.show()







