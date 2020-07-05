from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV Dataset
df = pd.read_csv('boston.csv')

# slice data which we want to predict
X = df.drop('MEDV', axis=1).values
y = df['MEDV'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

ridge = Ridge(alpha=0.1, normalize=True)
ridge.fit(X_train, y_train)
ridge_pred = ridge.predict(X_test)
score = ridge.score(X_test, y_test)
print(ridge_pred)
print(score)