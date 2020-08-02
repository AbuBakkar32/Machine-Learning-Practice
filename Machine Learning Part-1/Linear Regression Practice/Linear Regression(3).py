# Car Driving Analysis Using linear Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('car driving risk analysis.csv')
# df['meter'] = df['speed'].astype(str)+','+df['risk'].astype(str)
X = df[['speed']]
Y = df['risk']

xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size=.4)

reg = LinearRegression()
fitData = reg.fit(xtrain, ytrain)
score = reg.score(xtest, ytest)
print(score)

n = input('Enter your car speed:')
array = np.array(n)
array2 = array.astype(np.float)
value = ([[array2]])

result = reg.predict(value)
risk = np.array(result)
risk = risk.item()
print('Prediction how risk will be: ', risk)

