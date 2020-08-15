import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)


df = pd.read_csv('exercise_course.csv', sep=',', header=0)
# print(df.head())

### GroupBy Url And Sum Bytes
df2 = df.groupby('url')['bytes'].sum().reset_index()
# print(df2)

### Sort Values
df2 = df2.sort_values('bytes', ascending=True)
# print(df2)


######## TOTAL BYTES PER DOMAIN, SPLIT BY MALE OR FEMALE ###########

# define a function to calculate total Female bytes
def female_bytes(row):
    if row['gender'] == 'Female':
        return row['bytes']


# define a function to calculate total Male bytes
def male_bytes(row):
    if row['gender'] == 'Male':
        return row['bytes']


# Create new column populated by the Function
df['female_bytes'] = df.apply(female_bytes, axis=1)
df['male_bytes'] = df.apply(male_bytes, axis=1)
# print(df['female_bytes'])

# Group By URL and sum male_bytes and Female_bytes
df3 = df.groupby('url')['male_bytes', 'female_bytes'].sum()
#print(df3)

# sum bytes by male/female and group by URL and Country
df4 = df.groupby(['url', 'country'])['male_bytes', 'female_bytes'].sum()
# print(df4)
