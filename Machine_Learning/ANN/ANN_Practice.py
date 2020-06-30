from keras.models import *
from keras.layers import *

model = Sequential()
model.add(Dense(32, input_shape=(12,), activation='relu'))
model.add(Dense(2, activation='softmax'))
model.summary()