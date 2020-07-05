from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV Dataset
df = pd.read_csv('PIMA_Indians.csv')

# slice data which we want to predict
X = df.drop('diabetes', axis=1).values
y = df['diabetes'].values

# separate Data into train and test
logreg = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

# AUC Curve Find Out
y_pred_prob = logreg.predict_proba(X_test)[:, 1]
print(roc_auc_score(y_test, y_pred_prob))

cv_scores = cross_val_score(logreg, X, y, cv=5, scoring='roc_auc')

# Print list of AUC scores
print("AUC scores computed using 5-fold cross-validation: {}".format(cv_scores))



