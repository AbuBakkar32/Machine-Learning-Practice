import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# Load Datasets from Sklearn Dataset
digits = load_digits()
dir(digits)

# plot the imgaes using number of Range
plt.gray()
for i in range(3):
    plt.matshow(digits.images[i])

# create DataFrame to visualize data in a table
df = pd.DataFrame(digits.data)
df.head()

# Separate dataset into Feature and Target Data
df['target'] = digits.target
X = df.drop('target', axis=1)
y = df.target

# Make Datasets into Train And Test separantly
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create object of RF for Default prediction
rf = RandomForestClassifier(n_estimators=20)
rf.fit(X_train, y_train)
rf.score(X_test, y_test)

y_pred = rf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

# Show Prediction using Seaborn packages
plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()
