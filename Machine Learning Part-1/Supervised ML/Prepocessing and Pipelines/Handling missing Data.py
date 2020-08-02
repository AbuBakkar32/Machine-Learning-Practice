import pandas as pd
import numpy as np


df = pd.read_csv('diabetes.csv')
print(df.head())
print(df.shape)

df.triceps.replace(0, np.nan,  inplace=True)
df.insulin.replace(0, np.nan,  inplace=True)
df.bmi.replace(0, np.nan,  inplace=True)

#print(df.isnull().sum())
# print(df.head())
# print(df.info())

df = df.dropna()
print(df.shape)