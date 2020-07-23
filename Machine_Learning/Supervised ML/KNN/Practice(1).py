# Exploratory Data Analysis(EDA)
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

# Find the Shape of the Dataset
print(iris.data.shape)

# Find out Target_names
print(iris.target_names)

df = pd.DataFrame(X, columns=iris.feature_names)
print(df.head())

# Scatter Plot for Plot the sample Dataset
pd.plotting.scatter_matrix(df, c=Y, figsize=[8, 4], s=50, marker='G')
plt.show()




