import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('sample.csv', sep=',', header=0)


def Clean_salary(row):
    salary = row['Salary'].replace('$', '')
    salary = float(salary)
    return salary


df['clean_salary'] = df.apply(Clean_salary, axis=1)
group = df.groupby('gender')['Salary'].sum()


######################## Part-II (Initial insight from the data)##############################


def female_salary(row):
    if row['gender'] == 'Female':
        return row['clean_salary']


df['Female_salary_avf'] = df.apply(female_salary, axis=1)


# print(df['Female_salary_avf'])

###############################################################

def male_salary(row):
    if row['gender'] == 'Male':
        return row['clean_salary']


df['Male_salary_avf'] = df.apply(male_salary, axis=1)
# print(df['Male_salary_avf'])

################################################################


Group_data = df.groupby('Job Title')['clean_salary', 'Male_salary_avf', 'Female_salary_avf'].mean()
# print(Group_data)

###################### Extracting a little more insight ##################


pd.set_option('display.max_columns', None)
Group_data = df.groupby(['Job Title', 'City'])['clean_salary', 'Male_salary_avf', 'Female_salary_avf'].mean()
# print(Group_data)


###################### The Pandas Essentials ##################

median = df['Latitude'].median()
df['Latitude'].fillna(median, inplace=True)
# df.dropna()
# print(df.head(6))


## Remove duplicated row
df1 = df.drop_duplicates()
df2 = df.drop_duplicates(['first_name'], keep='last')
# print(df1.shape)
# print(df2.shape)


## conditional Operation
condition = df.loc[(df['clean_salary'] > 60000) & (df['clean_salary'] < 70000)]
df.sort_values('clean_salary', ascending=False)
# print(condition)


## Replace Value in Dataframe
df_male_replase = df[['first_name', 'last_name', 'gender']]
df_male_replase = df.replace(['Male', 'Female'], ['M', 'F'])


# print(df_male_replase)


## Rank our Salary into DataFrames and Apply Function

def Clean_salary(row):
    salary = row['Salary'].replace('$', '')
    salary = float(salary)
    return salary


df['clean_salary'] = df.apply(Clean_salary, axis=1)
df['rank'] = df['clean_salary'].rank(ascending=False)
# print(df.sort_values('rank'))
