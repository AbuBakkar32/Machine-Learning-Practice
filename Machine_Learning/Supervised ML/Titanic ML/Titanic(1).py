import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Fill all NaN value into Train Dataset
train = pd.read_csv('train.csv')
train = train.fillna(train.median().iloc[0])
# print(train.isna().sum())

# Fill all NaN value into Test Dataset
test = pd.read_csv('test.csv')
test = test.fillna(test.median().iloc[0])
# print(test.isna().sum())

train.plot(kind='box')
plt.show()

# print(train.describe(include='all'))
del train['Name']
train.head()

# how many Female and Male were in Ship
sns.countplot(train["Sex"])
plt.show()

# how many female and male according to there Age
# sns.barplot(x=train["Sex"], y=train["Age"])
# plt.show()
#
# # Who maximum Survived female or male according to there Survived list
# sns.barplot(x=train["Sex"], y=train["Survived"])
# plt.show()
#
# # Show which age person survived most
# plt.figure('Age vs Survived', figsize=(15, 6))
# sns.lineplot(x=train["Age"], y=train["Survived"])
# plt.show()

#
# plot = sns.jointplot(x=train["Age"], y=train["Survived"], kind='reg')
#
# plot = sns.barplot(x=train["Parch"], y=train["Survived"])
#
# plot = sns.barplot(x=train["Pclass"], y=train["Survived"])
#
# plot = sns.barplot(x=train["Embarked"], y=train["Survived"])
#
# corr_mtx = train.corr()
# print(corr_mtx)


