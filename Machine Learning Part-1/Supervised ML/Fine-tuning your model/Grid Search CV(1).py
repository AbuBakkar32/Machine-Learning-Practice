# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read the CSV Dataset
df = pd.read_csv('PIMA_Indians.csv')

# slice data which we want to predict
X = df.drop('diabetes', axis=1).values
y = df['diabetes'].values

param_grid = {'n_neighbors': np.arange(1, 50)}

knn = KNeighborsClassifier()
knn_cv = GridSearchCV(knn, param_grid, cv=5)
knn_cv.fit(X, y)

print(knn_cv.best_params_)
print(knn_cv.best_score_)
