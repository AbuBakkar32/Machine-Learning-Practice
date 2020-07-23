from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV Dataset
df = pd.read_csv('boston.csv')

# slice data which we want to predict
X = df.drop('MEDV', axis=1).values
y = df['MEDV'].values

reg = LinearRegression()

# 5 flod cv generate
cv_result = cross_val_score(reg, X, y, cv=5)
print(cv_result)
print(np.mean(cv_result))