import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
# to see all column Data
pd.set_option('display.max_columns', None)


df = pd.read_csv('winequality-red.csv', header=0)
# print(df.head())
# print(df.describe())

# Check where data in Null
# print(df.isnull().any())

# If you find null value than fill all null value using fillna method
# df = df.fillna(method='ffill')

X = df.drop('quality', axis=1).values
y = df['quality'].values

# check the average value of quality column
plt.figure(figsize=(8, 5))
plt.tight_layout()
sns.distplot(df['quality'])
# plt.show()

# split 80% of the data to the training set while 20% of the data to test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# For train Model and Fit data using Train Dataset
reg = LinearRegression()
reg.fit(X_train, y_train)


# corr = df.corr()
# plt.subplots(figsize=(8, 5))
# sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))
# plt.show()


# Find the Coefficient of regression model
coef_df = pd.DataFrame(reg.coef_, df.columns[:-1], columns=['Coefficient'])
# print(coef_df)

# find score Using Test Dataset
score = reg.score(X_test, y_test)
# print(score)

# Predict Data
y_pred = reg.predict(X_test)

# Check the difference between the actual value and predicted value.
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(25)

# Now let's plot the comparison of Actual and Predicted values
df1.plot(kind='bar', figsize=(10, 8))
plt.grid(which='major', linestyle='--', linewidth='0.5', color='green')
# plt.show()


# The final step is to evaluate the performance of the algorithm. We’ll do this by finding the values for MAE, MSE, and RMSE
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

