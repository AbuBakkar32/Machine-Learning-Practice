#Feature Selection
#Import Libraries
import pandas as pd                 # pandas is a dataframe library
import matplotlib.pyplot as plt      # matplotlib.pyplot plots data

#Read the data
df = pd.read_csv("pima-data.csv")

#Check the Correlation
#df.corr()
#Delete the correlated feature
del df['skin']

#Data Molding
diabetes_map = {True : 1, False : 0}
df['diabetes'] = df['diabetes'].map(diabetes_map)

#Splitting the data
from sklearn.model_selection import train_test_split

#This will copy all columns from 0 to 7(8 - second place counts from 1)
X = df.iloc[:, 0:8]
y = df.iloc[:, 8]

split_test_size = 0.30

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_test_size, random_state=42) 

#Imputing
from sklearn.impute import SimpleImputer 

#Impute with mean all 0 readings
fill_0 = SimpleImputer(missing_values=0, strategy="mean")

X_train = fill_0.fit_transform(X_train)
X_test = fill_0.transform(X_test)

#Naive Bayes
from sklearn.naive_bayes import GaussianNB
nb_model = GaussianNB()

from mlxtend.feature_selection import SequentialFeatureSelector as sfs

sfs_c = sfs(nb_model, k_features = 6, forward = True, floating=False, verbose=3, scoring = 'accuracy', cv=4)

sfs_c = sfs_c.fit(X_train, y_train)

feature_select = list(sfs_c.k_feature_idx_)
print(feature_select)

nb_model = GaussianNB()
nb_model.fit(X_train[:, feature_select], y_train)

y_train_pred = nb_model.predict(X_train[:, feature_select])


from sklearn.metrics import accuracy_score

print("Accuracy: %s" % accuracy_score(y_train, y_train_pred) )


y_test_pred = nb_model.predict(X_test[:, feature_select])
print("Accuracy: %s" % accuracy_score(y_test, y_test_pred) )

















