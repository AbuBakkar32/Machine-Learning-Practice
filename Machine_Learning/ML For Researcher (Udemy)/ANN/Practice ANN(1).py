import pandas as pd
import matplotlib.pyplot as plt
from keras import Sequential
from keras.layers import Dense

df = pd.read_csv('PIMA_Indians.csv')
df = df.drop('index', axis=1)
print(df.head())

X = df.iloc[:, :8].head()
y = df.iloc[:, -1].head()

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
_, Accuracy = model.evaluate(X,y)
print(Accuracy)
