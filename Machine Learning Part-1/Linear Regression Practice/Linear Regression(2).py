# Male Or Female Analysis Using linear Regression based on Height, Height and Shoe size

import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 63, 39],
     [171, 75, 42], [181, 85, 43]]

# female=0 and male=1
Y = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1]

# DecisionTree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
p_tree = clf.predict([[190, 70, 43]])
print('Decision Tree', p_tree)

# LinearRegression
linear = linear_model.LinearRegression()
linFit = linear.fit(X, Y)
p_lir = linear.predict([[190, 70, 43]])
print('Linear Regression Practice', p_lir)

# Logistic Regression

model = LogisticRegression()
model.fit(X, Y)
p_LoR = model.predict([[190, 70, 43]])
print('Logistic Regression', p_LoR)
