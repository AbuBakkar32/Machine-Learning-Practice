from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Load Iris Data From Sklearn Datasets
iris = datasets.load_iris()
X = iris.data  # Feature Data
Y = iris.target # Target Data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=21, stratify=Y)

# Train Data fit it over train data and find out score
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=21, stratify=Y)
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train, Y_train)
knn.predict(X_test)
knn.score(X_test, Y_test)