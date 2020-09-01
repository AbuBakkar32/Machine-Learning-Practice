import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from category_encoders import BinaryEncoder
from category_encoders import TargetEncoder

# Label Encoder
le = LabelEncoder()
df['columnName'] = le.fit_transform(df['columnName'])

# Ordinal Encoder
ord = OrdinalEncoder()
df["columnName"] = ord.fit_transform(df["columnName"]

# Frequency Encoder
fq = df.groupby('columnName').size() / len(df)
df.loc[:, "{}_freq_encode".format('columnName')] = df['columnName'].map(fq)
df = df.drop(['columnName'], axis=1)

# Binary Encoder
encoder = BinaryEncoder(cols=['columnName'])
newdata = encoder.fit_transform(df['columnName'])

# One hot encoder                                
df = pd.get_dummies(df, prefix=['OneHot'], columns=['columnName'])

# Target Encoders
TargetEnc = TargetEncoder()
values = TargetEnc.fit_transform(X=df.columnName, y=df.Target)
df = pd.concat([df, values], axis=1) 