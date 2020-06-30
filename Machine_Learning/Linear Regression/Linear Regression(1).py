# Home Price Prediction Using linear Regression based on Area of the house

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns

df = pd.read_csv('home_prices.csv')
x = df[['area']]
y = df['price']
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.3)

# Linear Regression Object creation
reg = LinearRegression()

# Fit the train Data
regFit = reg.fit(xtrain, ytrain)

# See Score for the test Data
score = reg.score(xtest, ytest)
print(score)

n = input('Enter any area:')
array = np.array(n)
array2 = array.astype(np.float)
value = ([[array2]])
result = reg.predict(value)

home_price = np.array(result)
home_price = home_price.item()

print('Prediction Home Price: ', home_price)

# plt.scatter(df['area'], df['price'], marker=r'$\clubsuit$', edgecolors='black', linewidths=5, label='Data Area')
# plt.plot(df.area, reg.predict(df[['area']]))
#
# plt.legend()
# plt.xlabel('Area measure')
# plt.ylabel('Price of Area')
# plt.title('Home Price and Area')
# plt.show()
