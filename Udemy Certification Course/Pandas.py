import pandas as pd
import numpy as np

data_dict = {
    'company': ['Amazon', 'Microsoft', 'Facebook'],
    'price': [2375.00, 178.6, 179.2],
    'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']
}

companies = pd.DataFrame(data=data_dict)
companies = companies.set_index('company')
# print(companies)

#################################################### 00002 ###############################################

date_range = pd.date_range(start='2020-01-01', periods=31)
# print(date_range)

#################################################### 00003 ###############################################

date_range = pd.date_range(start='2020-01-01', periods=52, freq='W-MON')
date_range = pd.date_range(start='2020-01-01', end='2020-12-31', freq='W-MON')
# print(date_range)

#################################################### 00004 ###############################################

date_range = pd.date_range(start='2021-01-01', periods=24, freq='H')
# print(date_range)

#################################################### 00005 ###############################################

date_range = pd.date_range(start='2021-03-01', periods=31)
df = pd.DataFrame(data=date_range, columns=['day'])
df['day_of_year'] = df['day'].dt.dayofyear
# print(df)

#################################################### 00006 ###############################################

np.random.seed(42)
data_dict = {
    'normal': np.random.normal(loc=0, scale=1, size=1000),
    'uniform': np.random.uniform(low=0, high=1, size=1000),
    'binomial': np.random.binomial(n=1, p=0.2, size=1000)
}

df = pd.DataFrame(data=data_dict, index=pd.date_range('2020-01-01', periods=1000))
print(df)

#################################################### 00007 ###############################################

np.random.seed(42)
data_dict = {
    'normal': np.random.normal(loc=0, scale=1, size=1000),
    'uniform': np.random.uniform(low=0, high=1, size=1000),
    'binomial': np.random.binomial(n=1, p=0.2, size=1000)
}

df = pd.DataFrame(data=data_dict, index=pd.date_range('2020-01-01', periods=1000))
print(df.head(10))
print()
print(df.tail())

#################################################### 00008 ###############################################

np.random.seed(42)
data_dict = {
    'normal': np.random.normal(loc=0, scale=1, size=1000),
    'uniform': np.random.uniform(low=0, high=1, size=1000),
    'binomial': np.random.binomial(n=1, p=0.2, size=1000)
}

df = pd.DataFrame(data=data_dict, index=pd.date_range('2020-01-01', periods=1000))
print(df.info())
print()
print(df.describe())

#################################################### 00009 ###############################################

np.random.seed(42)
data_dict = {
    'normal': np.random.normal(loc=0, scale=1, size=1000),
    'uniform': np.random.uniform(low=0, high=1, size=1000),
    'binomial': np.random.binomial(n=1, p=0.2, size=1000)
}

df = pd.DataFrame(data=data_dict, index=pd.date_range('2020-01-01', periods=1000))
print(df['binomial'].value_counts())

#################################################### 00010 ###############################################

np.random.seed(42)
data_dict = {
    'normal': np.random.normal(loc=0, scale=1, size=1000),
    'uniform': np.random.uniform(low=0, high=1, size=1000),
    'binomial': np.random.binomial(n=1, p=0.2, size=1000)
}

df = pd.DataFrame(data=data_dict, index=pd.date_range('2020-01-01', periods=1000))
df[:50].to_csv('dataframe50.csv', sep=',')

#################################################### 00012 ###############################################

google = pd.read_csv('google.csv', index_col=0)
google = google.reset_index()
print(google)

#################################################### 00013 ###############################################
google = pd.read_csv('google.csv', index_col=0)
google = google.reset_index()
google['Date'] = pd.to_datetime(google['Date'])
google['Year'] = google['Date'].dt.year
google['Month'] = google['Date'].dt.month
print(google)
#################################################### 00014 ###############################################

google = pd.read_csv('google.csv', index_col=0)
google = google.reset_index()
google['Date'] = pd.to_datetime(google['Date'])
google['Year'] = google['Date'].dt.year
google['Month'] = google['Date'].dt.month
print(google.groupby('Month')['Close'].mean())

#################################################### 00015 ###############################################

google = pd.read_csv('google.csv', index_col=0)
google = google.reset_index()
idx_min = google['Close'].argmin()
print(google.iloc[[idx_min]])

#################################################### 00016 ###############################################

google = pd.read_csv('google.csv', index_col=0)
google = google.reset_index()
print(google[['Date', 'Open', 'Close', 'Volume']])

#################################################### 00017 ###############################################

google = pd.read_csv('google.csv')
google = google.set_index('Date')
print(google)

#################################################### 00018 ###############################################

google = pd.read_csv('google.csv')
google['Date'] = pd.to_datetime(google['Date'])
google['Year'] = google['Date'].dt.year
google['Month'] = google['Date'].dt.month
google = google.drop(columns=['Year', 'Month'])
print(google)

#################################################### 00019 ###############################################

google = pd.read_csv('google.csv', index_col=0)
google.columns = ['O', 'H', 'L', 'C', 'V']
print(google)

#################################################### 00020 ###############################################

url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url)
print(df.head())

#################################################### 00021 ###############################################

url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url)
print(df.isnull().sum())

#################################################### 00022 ###############################################

url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url)

# Calculation of the median for the TotalCharges column
TotalChargesMedian = df['TotalCharges'][df['TotalCharges'] != ' '].median()

# Fill the missing values with median
df.loc[df['TotalCharges'] == ' ', 'TotalCharges'] = TotalChargesMedian

# Convert TotalCharges column to float type
df['TotalCharges'] = df['TotalCharges'].astype('float')

print(df['TotalCharges'].value_counts())

#################################################### 00023 ###############################################

url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url, index_col=0)
TotalChargesMedian = df['TotalCharges'][df['TotalCharges'] != ' '].median()
df.loc[df['TotalCharges'] == ' ', 'TotalCharges'] = TotalChargesMedian
df['TotalCharges'] = df['TotalCharges'].astype('float')

categorical = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
               'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
               'StreamingTV', 'Contract', 'StreamingMovies', 'PaperlessBilling', 'PaymentMethod', 'Churn']

numerical = ['tenure', 'MonthlyCharges']

#################################################### 00024 ###############################################

url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url, index_col=0)
TotalChargesMedian = df['TotalCharges'][df['TotalCharges'] != ' '].median()
df.loc[df['TotalCharges'] == ' ', 'TotalCharges'] = TotalChargesMedian
df['TotalCharges'] = df['TotalCharges'].astype('float')

categorical = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
               'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
               'StreamingTV', 'Contract', 'StreamingMovies', 'PaperlessBilling', 'PaymentMethod', 'Churn']

numerical = ['tenure', 'MonthlyCharges']

for col in categorical:
    df[col] = pd.Categorical(df[col])

for col in numerical:
    df[col] = df[col].astype(float)

print(df.describe(include=['category']))

#################################################### 00025 ###############################################

url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url, index_col=0)
print(df['Churn'].value_counts())

#################################################### 00026 ###############################################

url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url, index_col=0)
print(df.groupby(['Churn', 'PaymentMethod'])['MonthlyCharges'].mean())

#################################################### 00027 ###############################################

url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url, index_col=0)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

#################################################### 00028 ###############################################

url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url, index_col=0)
print(df.corr())

#################################################### 00029 ###############################################

np.random.seed(42)

url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv'
df = pd.read_csv(url, index_col=0)
df.sample(10).to_csv('sample_10.csv')

#################################################### 00030 ###############################################

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df)

#################################################### 00031 ###############################################

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

#################################################### 00032 ###############################################

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
df['col3'] = df['col2'].map(lambda x: 1 if x >= 0 else -1)
print(df)

#################################################### 00033 ###############################################

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
df['col3'] = df['col2'].map(lambda x: 1 if x >= 0 else -1)
df['col4'] = df['col2'].clip(-1.0, 1.0)
print(df)

#################################################### 00034 ###############################################

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df['col2'].nlargest(5))
print()
print(df['col2'].nsmallest(5))

#################################################### 00035 ###############################################

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df.cumsum())

#################################################### 00036 ###############################################

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df['col2'].median())
# or
print(df['col2'].quantile())

#################################################### 00037 ###############################################

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df.query("col2 > 0"))
# or
print(df[df['col2'] > 0])

#################################################### 00038 ###############################################

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df.head().to_dict())
# or
print(df[:5].to_dict())

#################################################### 00039 ###############################################

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df.head().to_html())
# or
print(df[:5].to_html())

#################################################### 00040 ###############################################

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
print(df.loc[df['C'] > 0.8])

#################################################### 00041 ###############################################

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
print(df.loc[(df['C'] > 0.3) & (df['D'] < 0.7)])

#################################################### 00042 ###############################################

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
for index, row in df.head().iterrows():
    print(row)

#################################################### 00043 ###############################################

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan
print(df)

#################################################### 00044 ###############################################

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan
df1 = df.dropna()
print(df1)
#################################################### 00045 ###############################################

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan
df1 = df.dropna()
df1 = df1.reset_index(drop=True)
print(df1)

#################################################### 00046 ###############################################

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan
print(df.isnull().sum())

#################################################### 00047 ###############################################

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan
df = df.fillna(0)
print(df)

#################################################### 00048 ###############################################

df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df = df[['D', 'A', 'B', 'C']]
print(df)

#################################################### 00017 ###############################################

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df = df.drop('D', axis=1)
print(df)

#################################################### 00049 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
print(df)

#################################################### 00050 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
print(list(df.columns))

#################################################### 00051 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.drop('New_Price', axis=1, inplace=True)
print(df.head())

#################################################### 00052 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.drop('New_Price', axis=1, inplace=True)
print(df.isnull().sum())

#################################################### 00053 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.dropna(inplace=True)
df.info()

#################################################### 00054 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
print(df.head())

#################################################### 00055 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
print(df['owner_type'].value_counts())

#################################################### 00017 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
df.dropna(inplace=True)
df['engine'] = df['engine'].map(lambda x: int(x[:-3]))
print(df[['name', 'engine']].head())
#################################################### 00056 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
df['power'] = np.where(df['power'] == 'null bhp', np.nan, df['power'])
print(df['power'].value_counts()[:5])

#################################################### 00057 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
print(df.groupby('year').size())

#################################################### 00058 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
print(df.groupby('year').size())

#################################################### 00059 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
df['transmission'] = df['transmission'].map({'Manual': 0, 'Automatic': 1})
print(df['transmission'].head())

#################################################### 00060 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
df.to_csv('cars.csv', index=False)

#################################################### 00061 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url, index_col=0)
df.info()

#################################################### 00062 ###############################################

pd.set_option('max_columns', 9)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url, index_col=0)
print(df.head())
print(df.tail())

#################################################### 00063 ###############################################

pd.set_option('max_columns', 9)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.info()

#################################################### 00064 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
print(df.head())

#################################################### 00065 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['month'] = df['timestamp'].dt.month
print(df.head())

#################################################### 00066 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['month'] = df['timestamp'].dt.month
humidity_by_month = df.groupby('month')['hum'].mean().reset_index()
print(humidity_by_month)

#################################################### 00067 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
cnt_by_hour = df.groupby('hour')['cnt'].mean().reset_index()
print(cnt_by_hour)

#################################################### 00068 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
cnt_by_weekend_hour = df.groupby(['is_weekend', 'hour'])['cnt'].mean().reset_index()
print(cnt_by_weekend_hour)

#################################################### 00069 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
print(df.query("wind_speed < 10.0 and hum > 90.0"))

#################################################### 00070 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df_weekend = df.query("is_weekend == 1.0").copy()
print(df_weekend)

#################################################### 00071 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df_weekend = df.query("is_weekend == 1.0").copy()
df_weekend.to_csv('weekend.txt', index=False)

#################################################### 00072 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
print(df.head())

#################################################### 00073 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
print(df[df.duplicated()])

#################################################### 00074 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
df = df.drop_duplicates()
df.info()

#################################################### 00075 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
print(df.select_dtypes(include=['object']))

#################################################### 00076 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
cat_vars = ['sex', 'smoker', 'region']

for col in cat_vars:
    df[col] = df[col].astype('category')

df.info()

#################################################### 00077 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
num_vars = list(df.select_dtypes(include=['float', 'int']).columns)
print(num_vars)

#################################################### 00078 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
for col in list(df.select_dtypes(include=['object']).columns):
    df[col] = df[col].astype('category')
df_cat = df.select_dtypes(include=['category']).copy()
df_num = df.select_dtypes(include=['float', 'int']).copy()
print(df_cat.head())
print(df_num.head())

#################################################### 00079 ###############################################
url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
for col in list(df.select_dtypes(include=['object']).columns):
    df[col] = df[col].astype('category')
df_cat = df.select_dtypes(include=['category']).copy()
print(df_cat.describe())
#################################################### 00080 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
for col in list(df.select_dtypes(include=['object']).columns):
    df[col] = df[col].astype('category')
df_num = df.select_dtypes(include=['float', 'int']).copy()
print(df_num.describe())

#################################################### 00081 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
print(df.describe().T[['mean', 'std']])

#################################################### 00082 ###############################################

url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
print(df.isnull().sum())

#################################################### 00083 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
for col in list(df.select_dtypes(include=['object']).columns):
    df[col] = df[col].astype('category')
df_dummies = pd.get_dummies(df, drop_first=True)
print(df_dummies.head())

#################################################### 00084 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
for col in list(df.select_dtypes(include=['object']).columns):
    df[col] = df[col].astype('category')
df_dummies = pd.get_dummies(df, drop_first=True)
corr = df_dummies.corr()

#################################################### 00085 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
for col in list(df.select_dtypes(include=['object']).columns):
    df[col] = df[col].astype('category')
df_dummies = pd.get_dummies(df, drop_first=True)
corr = df_dummies.corr()
print(corr[['charges']].sort_values(by='charges', ascending=False))

#################################################### 00086 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = 'https://storage.googleapis.com/esmartdata-courses-files/ml-course/insurance.csv'
df = pd.read_csv(url)
for col in list(df.select_dtypes(include=['object']).columns):
    df[col] = df[col].astype('category')
df_dummies = pd.get_dummies(df, drop_first=True)
data = df_dummies.copy()
target = data.pop('charges')
print(data.head())
print()
print(target.head())

#################################################### 00087 ###############################################

data = {
    'size': ['XL', 'L', 'M', 'L', 'M'],
    'color': ['red', 'green', 'blue', 'green', 'red'],
    'gender': ['female', 'male', 'male', 'female', 'female'],
    'price': [199.0, 89.0, 99.0, 129.0, 79.0],
    'weight': [500, 450, 300, 380, 410],
    'bought': ['yes', 'no', 'yes', 'no', 'yes']
}

df = pd.DataFrame(data)
print(df)

#################################################### 00088 ###############################################

data = {
    'size': ['XL', 'L', 'M', 'L', 'M'],
    'color': ['red', 'green', 'blue', 'green', 'red'],
    'gender': ['female', 'male', 'male', 'female', 'female'],
    'price': [199.0, 89.0, 99.0, 129.0, 79.0],
    'weight': [500, 450, 300, 380, 410],
    'bought': ['yes', 'no', 'yes', 'no', 'yes']
}

df = pd.DataFrame(data)
df.info()
for col in ['size', 'color', 'gender', 'bought']:
    df[col] = df[col].astype('category')

df['weight'] = df['weight'].astype('float')
print()
df.info()

#################################################### 00089 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
data = {
    'size': ['XL', 'L', 'M', 'L', 'M'],
    'color': ['red', 'green', 'blue', 'green', 'red'],
    'gender': ['female', 'male', 'male', 'female', 'female'],
    'price': [199.0, 89.0, 99.0, 129.0, 79.0],
    'weight': [500, 450, 300, 380, 410],
    'bought': ['yes', 'no', 'yes', 'no', 'yes']
}

df = pd.DataFrame(data)
for col in ['size', 'color', 'gender', 'bought']:
    df[col] = df[col].astype('category')

df['weight'] = df['weight'].astype('float')
print(pd.get_dummies(df))

#################################################### 00090 ###############################################

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
data = {
    'size': ['XL', 'L', 'M', 'L', 'M'],
    'color': ['red', 'green', 'blue', 'green', 'red'],
    'gender': ['female', 'male', 'male', 'female', 'female'],
    'price': [199.0, 89.0, 99.0, 129.0, 79.0],
    'weight': [500, 450, 300, 380, 410],
    'bought': ['yes', 'no', 'yes', 'no', 'yes']
}

df = pd.DataFrame(data)
for col in ['size', 'color', 'gender', 'bought']:
    df[col] = df[col].astype('category')

df['weight'] = df['weight'].astype('float')
print(pd.get_dummies(df, drop_first=True))




