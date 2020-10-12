# for Data processing need Pandas package
import pandas as pd

import string
import nltk
from nltk import tokenize
from nltk.corpus import stopwords
from pandas_profiling import ProfileReport
from wordcloud import WordCloud
from sklearn.utils import shuffle

# Visualiation to your work 
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_precision_recall_curve
from sklearn.metrics import plot_roc_curve
from sklearn.metrics import classification_report

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import \
    TfidfVectorizer  # The number of times a word appears in a document is its Term Frequency
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier

pd.set_option('display.max_columns', None)
fake_data = pd.read_csv("Fake.csv")
true_data = pd.read_csv("True.csv")

fake_data['target'] = 'Fake'
true_data['target'] = 'True'

dataset = pd.concat([fake_data, true_data]).reset_index(drop=True)
# dataset.shape

dataset = shuffle(dataset).reset_index(drop=True)
dataset.head()
# dataset.to_csv('Fake_Real.csv')

dataset = pd.read_csv("Fake_Real.csv")

dataset = dataset.sample(frac=1)
# dataset

dataset.subject.value_counts().plot(kind="bar", color="m")

# dataset.notna().all(axis=0)
sns.heatmap(dataset.notna(), annot=True)
plt.show()

dataset.notna().all()

dataset.drop(['title', 'date'], axis=1, inplace=True)

dataset['text'] = dataset['text'].apply(lambda x: x.lower())
dataset.head()


def punctuation_removal(text):
    all_list = [char for char in text if char not in string.punctuation]
    clean_str = ''.join(all_list)
    return clean_str


dataset['text'] = dataset['text'].apply(punctuation_removal)
dataset.head()

stop = stopwords.words('english')
dataset['text'] = dataset['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
dataset.head()

dataset.groupby(['subject'])['text'].count()

dataset.groupby(['subject'])['text'].count().plot(kind="bar", color='r')
plt.show()

dataset.groupby(['target'])['text'].count()

dataset.groupby(['target'])['text'].count().plot(kind='bar', color='r')
plt.show()

# # Word Cloud for False news:
# select_fake_data = dataset[dataset['target']=='Fake']
# all_text = ' '.join([text for text in select_fake_data.text])
#
# wordcloud = WordCloud(width= 800, height= 500, max_font_size = 150, collocations = False).generate(all_text)
#
# plt.figure(figsize=(10,7))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
#
# # Word Cloud for real news:
# select_fake_data = dataset[dataset['target']=='True']
# all_text = ' '.join([text for text in select_fake_data.text])
#
# wordcloud = WordCloud(width= 800, height= 500, max_font_size = 150, collocations = False).generate(all_text)
#
# plt.figure(figsize=(10,7))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()

x = dataset['text']
y = dataset['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.35, random_state=45)

# Initialize a TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
# Fit and transform train set, transform test set
x_train = tfidf_vectorizer.fit_transform(x_train)
x_test = tfidf_vectorizer.transform(x_test)

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier(criterion='entropy', max_depth=20, splitter='best', random_state=87)
dtc.fit(x_train, y_train)
y_pred = dtc.predict(x_test)
print(accuracy_score(y_test, y_pred) * 100)
classification_report(y_test, y_pred)

# Check the difference between the actual value and predicted value.
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df['Actual'] = df['Actual'].map({'True': 1, 'Fake': 0})
df['Predicted'] = df['Predicted'].map({'True': 1, 'Fake': 0})

# Now let's plot the comparison of Actual and Predicted values
df.plot(kind='hist', figsize=(12, 5))
plt.grid(which='major', linestyle='--', linewidth='0.2', color='green')
plt.legend(loc="upper center")
plt.show()

plt.figure(figsize=(13, 5))
plt.tight_layout()
sns.distplot(df['Predicted'])
plt.show()

from sklearn.svm import SVC

# svm = SVC(C=1.0, break_ties=False, cache_size=200, class_weight=None, coef0=0.0,
#       decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
#       max_iter=-1, probability=False, random_state=None, shrinking=True,
#       tol=0.001, verbose=False)
svm = SVC(kernel='linear')
svm.fit(x_train, y_train)
predictions = svm.predict(x_test)
svm_score = accuracy_score(y_test, predictions)
print(f'Accuracy: {round(svm_score * 100, 2)}%')
classification_report(y_test, predictions)

rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)
rfc_predictions = rfc.predict(x_test)
rfc_score = accuracy_score(y_test, rfc_predictions)
print(f'Accuracy: {round(rfc_score * 100, 2)}%')
classification_report(y_test, rfc_predictions)

lrc = LogisticRegression()
lrc.fit(x_train, y_train)
lrc_predictions = lrc.predict(x_test)
lrc_score = accuracy_score(y_test, lrc_predictions)
print(f'Accuracy: {round(lrc_score * 100, 2)}%')
classification_report(y_test, lrc_predictions)

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
knn_pred = knn.predict(x_test)
knn_score = accuracy_score(y_test, knn_pred)
print(f'Accuracy: {round(knn_score * 100, 2)}%')
classification_report(y_test, knn_pred)
plot_precision_recall_curve(knn, x_test, y_test)
plot_roc_curve(knn, x_test, y_test)

import xgboost as xgb

xgbm = xgb.XGBClassifier(random_state=1)
xgbm.fit(x_train, y_train)
xgbm_pred = xgbm.predict(x_test)
xgbm_score = accuracy_score(y_test, xgbm_pred)
print(f'Accuracy: {round(xgbm_score * 100, 2)}%')
classification_report(y_test, xgbm_pred)

from sklearn.linear_model import PassiveAggressiveClassifier

pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(x_train, y_train)
# DataFlair - Predict on the test set and calculate accuracy
pac_pred = pac.predict(x_test)
pac_score = accuracy_score(y_test, pac_pred)
print(f'Accuracy: {round(pac_score * 100, 2)}%')
classification_report(y_test, pac_pred)
plot_roc_curve(pac, x_test, y_test)
plot_precision_recall_curve(pac, x_test, y_test)

from sklearn.naive_bayes import MultinomialNB

mnlb = MultinomialNB()
mnlb.fit(x_train, y_train)

# DataFlair - Predict on the test set and calculate accuracy
mnlb_pred = mnlb.predict(x_test)
mnlb_score = accuracy_score(y_test, mnlb_pred)
print(f'Accuracy: {round(mnlb_score * 100, 2)}%')
classification_report(y_test, mnlb_pred)
plot_precision_recall_curve(mnlb, x_test, y_test)
plot_roc_curve(mnlb, x_test, y_test)

profile = ProfileReport(pd.read_csv('Fake_Real.csv'), title='Fake And True Profiling Report', explorative=True)

# Saving results to a HTML file
profile.to_file("100%output.html")
