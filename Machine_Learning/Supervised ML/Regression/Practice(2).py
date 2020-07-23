from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


# Read the CSV Dataset
df = pd.read_csv('boston.csv')

# slice data which we want to predict
X = df.drop('MEDV', axis=1).values
y = df['MEDV'].values

# separate Data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

reg = LinearRegression()
reg.fit(X_train, y_train)
y_perd = reg.predict(X_test)
print(reg.score(X_test, y_test))

plt.plot(X, reg.predict([y_perd]), color='red')
plt.show()