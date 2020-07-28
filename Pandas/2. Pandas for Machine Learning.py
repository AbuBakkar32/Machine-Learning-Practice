#!/usr/bin/env python
# coding: utf-8

# ## Essential Pandas for Machine Learning
# 
# <hr>
# 
# ### Agenda
# 1. Introduction to Pandas
# 2. Understanding Series & DataFrames
# 3. Loading CSV,JSON
# 4. Connecting databases
# 5. Descriptive Statistics
# 6. Accessing subsets of data - Rows, Columns, Filters
# 7. Handling Missing Data
# 8. Dropping rows & columns
# 9. Handling Duplicates
# 10. Function Application - map, apply, groupby, rolling, str
# 11. Merge, Join & Concatenate
# 12. Pivot-tables
# 13. Normalizing JSON
# 
# <hr>

# ### 1. Introduction to Pandas
# * High Performance, Easy-to-use open source library for Data Analysis
# * Creates tabular format of data from different sources like csv, json, database.
# * Have utilities for descriptive statistics, aggregation, handling missing data
# * Database utilities like merge, join are available
# * Fast, Programmable & Easy alternative to spreadsheets

# In[2]:


import pandas as pd
import numpy as np

# ### 2. Understanding Series & DataFrames
# * Series represents one column
# * Combine multiple columns to create a table ( .i.e DataFrame )

# In[4]:


ser1 = pd.Series(data=[1, 2, 3, 4, 5], index=list('abcde'))
ser1

# In[5]:


ser2 = pd.Series(data=[11, 22, 33, 44, 55], index=list('abcde'))
ser2

# * Creating DataFrame from above two series
# * Data corresponding to same index belongs to same row

# In[7]:


df = pd.DataFrame({'A': ser1, 'B': ser2})
df

# * Creating a random dataframe of 10 X 10

# In[10]:


pd.DataFrame(data=np.random.randint(1, 10, size=(10, 10)), index=list('ABCDEFGHIJ'), columns=list('abcdefghij'))

# ### 3. Loading CSV,JSON

# In[19]:


hr_data = pd.read_csv(
    'https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/HR_comma_sep.csv.txt')

# In[24]:


hr_data.info()

# In[27]:


hr_data_itr = pd.read_csv(
    'https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/HR_comma_sep.csv.txt',
    chunksize=5000)

# In[28]:


for hr_data in hr_data_itr:
    print(hr_data.info())

# In[29]:


pd.read_json('https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/movie.json.txt')

# ### 4. Connecting Databases

# In[32]:


# get_ipython().system('pip install pysqlite3')


# In[33]:


import sqlite3

# In[35]:


con = sqlite3.connect('Data/database.sqlite')

# In[39]:


pd.read_sql_query("SELECT * FROM Reviews LIMIT 5", con)

# * import MySQLdb
# * mysql_cn= MySQLdb.connect(host='myhost', 
#                 port=3306,user='myusername', passwd='mypassword', 
#                 db='information_schema')
# * df_mysql = pd.read_sql('select * from VIEWS;', con=mysql_cn)

# ### 5. Descriptive Statistics
# * Pandas api's for understanding data

# In[47]:


hr_data = pd.read_csv(
    'https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/HR_comma_sep.csv.txt')

# In[48]:


hr_data.head()

# In[49]:


hr_data.tail()

# In[50]:


hr_data.info()

# In[51]:


hr_data.describe()

# In[54]:


hr_data.salary.value_counts()

# ### 6. Accessing subset of data - rows, columns, filters
# * Get all columns with categorical values

# In[56]:


cat_cols_data = hr_data.select_dtypes('object')

# In[57]:


cat_cols_data.head()

# * Rename columns names

# In[58]:


hr_data.rename(columns={'sales': 'department'}, inplace=True)

# In[59]:


hr_data.head()

# * Select column by column names

# In[60]:


hr_data.columns

# In[61]:


hr_data[['satisfaction_level', 'last_evaluation', 'number_project']].head()

# In[63]:


hr_data.satisfaction_level[:5]

# In[65]:


hr_data['satisfaction_level'][:5]

# In[66]:


movie_data = pd.read_json(
    'https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/movie.json.txt')

# In[67]:


movie_data

# * Access data by index values

# In[68]:


movie_data.loc['Scarface']

# In[69]:


movie_data.loc['Scarface':'Vertigo']

# In[70]:


movie_data['Scarface':'Vertigo']

# In[71]:


movie_data.iloc[1]

# In[72]:


movie_data.iloc[1:4]

# In[73]:


movie_data[1:4]

# * Filtering rows based on conditions

# In[87]:


movie_data[(movie_data['Adam Cohen'] > 3)]

# In[89]:


movie_data[((movie_data['Adam Cohen'] > 3) & (movie_data['David Smith'] > 4))]

# ### 7. Handling missing data
# * Machine Learning algorithms don't expect data missing
# * If there is a columns with more than 40% data missing, we may drop the column
# * Fow rows with, important column values missing. Drop the rows

# In[74]:


movie_data

# * Get all the rows for which column 'Bill Duffy' is missing

# In[77]:


movie_data['Bill Duffy'].notnull()

# In[78]:


movie_data[movie_data['Bill Duffy'].notnull()]

# * Get all the rows for which 'Bill Duffy' is null

# In[80]:


movie_data[movie_data['Bill Duffy'].isnull()]

# ### 8. Dropping Rows & Columns

# In[91]:


titanic_data = pd.read_csv(
    'https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/titanic-train.csv.txt')

# In[92]:


titanic_data.info()

# * Dropping 'Cabin' column as it has only 204 data present in 891 rows

# In[93]:


titanic_data.drop(['Cabin'], axis=1, inplace=True)

# In[94]:


titanic_data.info()

# * Now, drop all rows with missing values
# * We don't have inplace = True, so doesn't modify the dataframe

# In[96]:


titanic_data.dropna().info()

# * Consider only selected columns to check if they contain NA

# In[98]:


titanic_data.info()

# In[97]:


titanic_data.dropna(subset=['Embarked', 'Age']).info()

# * Another approach of handling missing data is filling the missing ones

# In[106]:


titanic_data.info()

# In[108]:


titanic_data.fillna({'Age': 0, 'Embarked': 'Unknown'}).info()

# In[113]:


titanic_data.Age.fillna(method='ffill')[:5]
# Other options are 'bfill'


# ### 9. Handling Duplicates
# * Sometimes, it difficult to ensure that data is not duplicated.
# * This becomes responsibility in Data cleaning step to make sure duplicated data is deleted

# In[99]:


df = pd.DataFrame({'A': [1, 1, 3, 4, 5, 1], 'B': [1, 1, 3, 7, 8, 1], 'C': [3, 1, 1, 6, 7, 1]})

# In[100]:


df

# In[104]:


df.duplicated()

# In[102]:


df[df.duplicated()]

# In[105]:


df[df.duplicated(subset=['A', 'B'])]

# ### 10. Function Application
# * map for transforming one column to another
# * Can be applied only to series

# In[118]:


titanic_data_age = titanic_data[titanic_data.Age.notnull()]

# In[128]:


titanic_data['age_category'] = titanic_data.Age.map(lambda age: 'Kid' if age < 18 else 'Adult')

# In[129]:


titanic_data.head()

# * apply function can be done to Series as well as DataFrames

# In[124]:


titanic_data.Age.apply('sum')

# In[132]:


titanic_data.Age.apply(lambda age: 'Kid' if age < 18 else 'Adult')[:10]


# * apply on dataframes helps us dealing with multiple columns
# * func will receive all the rows

# In[135]:


# e will be each row
def func(e):
    if e.Sex == 'male':
        return e.Fare * 2
    else:
        return e.Fare


# In[137]:


titanic_data.apply(func, axis=1)[:5]

# * groupby - It splits data into groups, a function is applied to each groups separately, combine results into a data structure

# In[139]:


titanic_data.groupby(['Sex']).Age.mean()

# In[144]:


titanic_data.groupby(['Sex']).Age.agg(['mean', 'min', 'max'])

# * Rolling for window based operation

# In[2]:


titanic_data.Age.rolling(window=5, min_periods=1).agg(['sum', 'min'])

# * For columns containing string, we have str utilities

# In[150]:


titanic_data[titanic_data.Name.str.contains('Mr')]

# ### 11. Append,Merge, Join & Concatenate
# * Append for stacking dataframe

# In[151]:


df1 = pd.DataFrame(data=np.random.randint(1, 10, size=(10, 3)), columns=list('ABC'))

# In[160]:


df2 = pd.DataFrame(data=np.random.randint(1, 10, size=(10, 3)), columns=list('ABC'))

# In[154]:


df1

# In[161]:


df2

# In[163]:


df1.append(df2, ignore_index=True)

# In[164]:


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                     'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5'],
                     'B': ['B0', 'B1', 'B2', 'B3', 'B4', 'B5']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K6', 'K7'],
                      'C': ['C0', 'C1', 'C2', 'C3', 'C6', 'C7'],
                      'D': ['D0', 'D1', 'D2', 'D3', 'D6', 'D7']})

# In[166]:


left.merge(right, on='key')

# In[168]:


left.merge(right, on='key', how='left')

# * join for combining data based on index values

# In[169]:


left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

# In[170]:


left.join(right)

# ### 12. Pivot Tables
# * An useful way to get important information from data

# In[175]:


sales_data = pd.read_excel(
    'https://github.com/zekelabs/data-science-complete-tutorial/blob/master/Data/sales-funnel.xlsx?raw=true')

# In[188]:


sales_data

# In[189]:


pd.pivot_table(sales_data, index=['Manager', 'Rep'], values=['Account', 'Price'], aggfunc=[np.sum, np.mean])

# ### 13. Normalizing JSON
# * JSON data will not always be of flat but can be hierchial

# In[190]:


data = [{'state': 'Florida',
         'shortname': 'FL',
         'info': {
             'governor': 'Rick Scott'
         },
         'counties': [{'name': 'Dade', 'population': 12345},
                      {'name': 'Broward', 'population': 40000},
                      {'name': 'Palm Beach', 'population': 60000}]},
        {'state': 'Ohio',
         'shortname': 'OH',
         'info': {
             'governor': 'John Kasich'
         },
         'counties': [{'name': 'Summit', 'population': 1234},
                      {'name': 'Cuyahoga', 'population': 1337}]}]

# In[191]:


from pandas.io.json import json_normalize

# In[192]:


json_normalize(data)

# In[199]:


json_normalize(data, 'counties', ['state', ['info', 'governor']])

# In[ ]:
