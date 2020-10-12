import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# to see all column Data
pd.set_option('display.max_columns', None)

df = pd.read_csv('winequality-red.csv', header=0)
# print(df.head())

# Missing Values
# print(df.isna().sum())

# Show Data
plt.figure(figsize=(8, 5))
plt.tight_layout()
sns.distplot(df['quality'])
# plt.show()

# Show Data in Heatmap
corr = df.corr()
plt.subplots(figsize=(15, 10))
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True,
            cmap=sns.diverging_palette(220, 20, as_cmap=True))
plt.show()
# Create Classification version of target variable
df['goodquality'] = [1 if x >= 7 else 0 for x in df['quality']]

# Separate feature variables and target variable
X = df.drop(['quality', 'goodquality'], axis=1)
y = df['goodquality']

# See proportion of good vs bad wines
count = df['goodquality'].value_counts()

# Normalize feature variables
from sklearn.preprocessing import StandardScaler

X_features = X
X = StandardScaler().fit_transform(X)

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=0)

# For Decision Tree
from sklearn.tree import DecisionTreeClassifier

model1 = DecisionTreeClassifier(random_state=1)
model1.fit(X_train, y_train)
y_pred1 = model1.predict(X_test)
# print(classification_report(y_test, y_pred1))
print('Decision Tree Accuracy Score: ', accuracy_score(y_test, y_pred1))

# For Random Forest
from sklearn.ensemble import RandomForestClassifier

model2 = RandomForestClassifier(random_state=1)
model2.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)
# print(classification_report(y_test, y_pred2))
print('Random Forest Accuracy Score: ', accuracy_score(y_test, y_pred1))

feat_importances = pd.Series(model2.feature_importances_, index=X_features.columns)
feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 10))

# for AdaBoost
from sklearn.ensemble import AdaBoostClassifier

model3 = AdaBoostClassifier(random_state=1)
model3.fit(X_train, y_train)
y_pred3 = model3.predict(X_test)
# print(classification_report(y_test, y_pred3))
print('AdaBoost Accuracy Score: ', accuracy_score(y_test, y_pred1))

# for Gradient Boosting
from sklearn.ensemble import GradientBoostingClassifier

model4 = GradientBoostingClassifier(random_state=1)
model4.fit(X_train, y_train)
y_pred4 = model4.predict(X_test)
# print(classification_report(y_test, y_pred4))
print('Gradient Boosting Accuracy Score: ', accuracy_score(y_test, y_pred1))



# for XGBoost
import xgboost as xgb

model5 = xgb.XGBClassifier(random_state=1)
model5.fit(X_train, y_train)
y_pred5 = model5.predict(X_test)
# print(classification_report(y_test, y_pred5))
print('XGBoost Accuracy Score: ', accuracy_score(y_test, y_pred1))

feat_importances = pd.Series(model5.feature_importances_, index=X_features.columns)
feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 10))
plt.show()

# Filtering df for only good quality
good = df[df['goodquality'] == 1]

# Filtering df for only bad quality
bad = df[df['goodquality'] == 0]

