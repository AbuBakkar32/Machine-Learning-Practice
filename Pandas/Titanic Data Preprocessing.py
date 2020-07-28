import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

training_set = pd.read_csv('train.csv')
# print(training_set.head(n=5))
# print(training_set.shape)
# print(training_set.isna().sum())
# print(training_set.columns)
#################################################################################
# dropping ticket column
training_set.drop(['Ticket', 'PassengerId'], 1, inplace=True)


# print(training_set.head(n=5))
# print(training_set.info())

#################################################################################
# user defined function
def assignDeckValue(CabinCode):
    if pd.isnull(CabinCode):
        category = 'Unknown'
    else:
        category = CabinCode[0]
    return category


Deck = np.array([assignDeckValue(cabin) for cabin in training_set['Cabin'].values])
training_set = training_set.assign(Deck=Deck)
# print(training_set.head(5))

#################################################################################

training_set['FamilySize'] = training_set['SibSp'] + training_set['Parch'] + 1
# print(training_set.head(5))

#################################################################################

# Using expression pattern to extract the Title of the passenger
training_set['Title'] = training_set.Name.str.extract('([A-Za-z]+)\.', expand=False)
# print(training_set['Title'])

# Changing to common category
training_set['Title'] = training_set['Title'].replace(
    ['Dr', 'Rev', 'Col', 'Major', 'Countess', 'Sir', 'Jonkheer', 'Lady', 'Capt', 'Don'], 'Others')
training_set['Title'] = training_set['Title'].replace('Ms', 'Miss')
training_set['Title'] = training_set['Title'].replace('Mme', 'Mrs')
training_set['Title'] = training_set['Title'].replace('Mlle', 'Miss')
# print(training_set['Title'])

#################################################################################

training_set.drop(['Cabin', 'Name'], 1, inplace=True)
# print(training_set.head())

#################################################################################

# Returns count for each category
training_set['Embarked'].value_counts()

# Fills null values with 'S'-most common occurence
training_set['Embarked'] = training_set['Embarked'].fillna('S')

# Checking the no of null values now
training_set['Embarked'].isnull().sum()

#################################################################################

means = training_set.groupby('Title')['Age'].mean()
title_list = ['Master', 'Miss', 'Mr', 'Mrs', 'Others']


def age_missing_replace(means, dframe, title_list):
    for title in title_list:
        temp = dframe['Title'] == title
        dframe.loc[temp, 'Age'] = dframe.loc[temp, 'Age'].fillna(means[title])


age_missing_replace(means, training_set, title_list)

#################################################################################

training_set['Embarked'] = training_set['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
training_set['Sex'] = training_set['Sex'].map({'male': 0, 'female': 1})
training_set['Title'] = training_set['Title'].map({'Master': 0, 'Miss': 1, 'Mr': 2, 'Mrs': 3, 'Others': 4})

#################################################################################

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
training_set['Deck'] = le.fit_transform(training_set['Deck'])

#################################################################################

print(training_set)

#################################################################################
