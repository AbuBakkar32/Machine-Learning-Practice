import pandas as pd                 # pandas is a dataframe library
import matplotlib.pyplot as plt


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

from sklearn.preprocessing import StandardScaler
ss_X = StandardScaler()
X_train = ss_X.fit_transform(X_train)
X_test = ss_X.transform(X_test)

#Applying LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components=1)
X_train = lda.fit_transform(X_train, y_train)
X_test = lda.transform(X_test)
explain_var = lda.explained_variance_ratio_
print(explain_var)

from sklearn.naive_bayes import GaussianNB

nb_model = GaussianNB()
nb_model.fit(X_train, y_train.ravel())

nb_predict_train = nb_model.predict(X_train)

from sklearn import metrics
print(metrics.accuracy_score(y_train, nb_predict_train))



nb_predict_test = nb_model.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, nb_predict_test))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, nb_predict_test)
print(cm)




