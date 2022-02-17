# Support Vector Machine (SVM)

# Importing the libraries
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
from sklearn.svm import SVC

classifier = SVC(kernel='linear', random_state=0)
classifier.fit(X_train, y_train)

# Predicting the test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score

cs = accuracy_score(y_test, y_pred)
print(cs)

cm = confusion_matrix(y_test, y_pred)
print(cm)


# decision Tree12 Classification

# from sklearn.tree import DecisionTreeClassifier
#
# dt = DecisionTreeClassifier()
# dt.fit(X_train, y_train)
#
# dt_predit = dt.predict(X_test)
# print("This is for the Decision Tree classification")
# print(dt_predit)
# print(confusion_matrix(y_test, y_pred))
# print(dt.score(X_test, y_test))
