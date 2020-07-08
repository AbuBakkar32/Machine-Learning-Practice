from sklearn.datasets import load_iris
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# print('DESCR : ', iris.DESCR)
# print('DATA : ', iris.data)
# print('TARGET : ', iris.target)
# print('FEATURE_NAMES : ', iris.feature_names)
# print('FILENAME : ', iris.filename)
# print('FRAME : ', iris.frame)
# print('TARGET_NAMES : ', iris.target_names)

# Load Datasets from Sklearn Dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()

# Find Out Target of Dataset
df['target'] = iris.target
df.head()

# Apply All Flower name associate of the target
df['flower_name'] = df.target.apply(lambda x: iris.target_names[x])
df.head()

# Aggregate Dataset Find out all possible vergenica flower
df[df.target == 2].head()

# Separate Data into 3 categories
df1 = df[:50]
df2 = df[50:100]
df3 = df[100:]

# Plot data from sepal length & width
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'], color='g')
plt.scatter(df2['sepal length (cm)'], df2['sepal width (cm)'], color='y')
plt.scatter(df3['sepal length (cm)'], df3['sepal width (cm)'], color='r')
plt.show()

# Plot data from petal length & width
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'], color='g')
plt.scatter(df2['petal length (cm)'], df2['petal width (cm)'], color='y')
plt.scatter(df3['petal length (cm)'], df3['petal width (cm)'], color='r')
plt.show()

# Separate dataset into Target data and Feature data for prediction
X = df.drop(['target', 'flower_name'], axis=1)
y = df.target

# train Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create object of SVC for Default prediction
model = SVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(model.score(X_test, y_test))

# Create object of SVC for using kernel prediction
model_k = SVC(kernel='linear')
model_k.fit(X_train, y_train)
print(model_k.score(X_test, y_test))

# Create object of SVC for using C prediction
model_c = SVC(C=10)
model_c.fit(X_train, y_train)
print(model_c.score(X_test, y_test))

# Create object of SVC for using Gamma prediction
model_g = SVC(gamma=3)
model_g.fit(X_train, y_train)
print(model_g.score(X_test, y_test))

print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
