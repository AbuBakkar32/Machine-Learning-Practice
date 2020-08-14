import pandas as pd
data = {
'country': ['United States', 'The Netherlands', 'Spain', 'Mexico', 'Australia'],
'capital': ['Washington D.C.', 'Amsterdam', 'Madrid', 'Mexico City', 'Canberra'],
'continent': ['North America', 'Europe', 'Europe', 'North America', 'Australia'],
'language': ['English', 'Dutch', 'Spanish', 'Spanish', 'English']}

countries = pd.DataFrame(data)

countries.loc[:, 'country':'continent']
countries.loc[0:2, 'country':'continent']
countries.loc[[0, 4], ['country', 'language']]

# Filter DataFrames by category
countries[countries.continent == 'Europe']
countries[countries.language.isin(['Dutch', 'English'])]

# Filter DataFrames by excluding categories
countries[~countries.continent.isin(['Europe'])]
countries[~countries.language.isin(['Dutch', 'English'])]

# Rename columns
countries.rename({'capital': 'capital_city', 'language': 'most_spoken_language'}, axis='columns')  # or
countries.columns = ['country', 'capital_city', 'continent', 'most_spoken_language']

# Reverse row order
countries.loc[::-1].reset_index(drop=True)

# Reverse column order
countries.loc[:, ::-1]

# Split a DataFrame into two random subsets
countries_1 = countries.sample(frac=0.6, random_state=50)
countries_2 = countries.drop(countries_1.index)

##############################Create dummy variables#########################################

students = pd.DataFrame({
'name': ['Ben', 'Tina', 'John', 'Eric'],
'gender': ['male', 'female', 'male', 'male']})

pd.get_dummies(students) # all value assign as a numeric value
pd.get_dummies(students, drop_first=True) # To get rid of the redundant columns

##############################Check equality of columns#########################################

df = pd.DataFrame({'col_1': [1, 0], 'col_2': [0, 1], 'col_3': [1, 0]})
df['col_1'].equals(df['col_2'])
df['col_1'].equals(df['col_3'])


# Concatenate DataFrames
df_1 = pd.DataFrame({'col_1': [6, 7, 8], 'col_2': [1, 2, 3], 'col_3': [5, 6, 7]})
df_2 = pd.concat([df, df_1]).reset_index(drop=True)

