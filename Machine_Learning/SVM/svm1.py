# importing required libraries
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# read the train and test dataset
train_data = pd.read_csv('train-data.csv')
test_data = pd.read_csv('test-data.csv')

# shape of the dataset
print('Shape of training data :', train_data.shape)
print('Shape of testing data :', test_data.shape)

# Now, we need to predict the missing target variable in the test data
# target variable - Survived

# seperate the independent and target variable on training data
train_x = train_data.drop(columns=['Survived'], axis=1)
train_y = train_data['Survived']

# seperate the independent and target variable on testing data
test_x = test_data.drop(columns=['Survived'], axis=1)
test_y = test_data['Survived']


model = SVC()

# fit the model with the training data
model.fit(train_x, train_y)

# predict the target on the train dataset
predict_train = model.predict(train_x)
print('Target on train data', predict_train)

# Accuray Score on train dataset
accuracy_train = accuracy_score(train_y, predict_train)
print('accuracy_score on train dataset : ', accuracy_train)

# predict the target on the test dataset
predict_test = model.predict(test_x)
print('Target on test data', predict_test)

# Accuracy Score on test dataset
accuracy_test = accuracy_score(test_y, predict_test)
print('accuracy_score on test dataset : ', accuracy_test)
