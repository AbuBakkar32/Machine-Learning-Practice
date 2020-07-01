from numpy.random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# from google.colab import files
# upload = files.upload()
#
# for fn in upload.keys():
#     print('User uploaded file "{name}" with length "{length}" bytes'. format(name=fn, length=len(upload[fn])))

# ................Pandas Series...................

# labels = 'A B C D'.split()
# my_data = [1, 2, 3, 4]
# arr = np.array(my_data)
# dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
# dic2 = {'A': 1, 'B': 2, 'C': 3, 'E': 4}
#
# sr = pd.Series(dic)
# sr2 = pd.Series(dic2)
# print(sr+sr2)


# ...............Pandas DataFrame Tutorial..............

# arr = randint(0, 100, 16).reshape(4, 4)
#
# row = 'A B C D'.split()
# col = 'E F G H'.split()
#
# df = pd.DataFrame(data=arr, index=row, columns=col)
# print(df)


# ...............Pandas DataFrame Selection Index and Missing data ..............

# arr = randint(-100, 100, 16).reshape(4, 4)
#
# row = 'A B C D'.split()
# col = 'E F G H'.split()
#
# df = pd.DataFrame(data=arr, index=row, columns=col)

# print(df.iloc[1]) # Integer Location index wish will be print
# print(df.T) # travers index to columns, columns to index
# df['SUM(G & H)'] = df['G']+df['H'] # Create new Column doing sum G and H Column
# df.loc['SUM(C & D)'] = df.loc['C']+df.loc['D'] # Create new Row doing sum C and D Row
# df.drop('SUM(G & H)', axis=1, inplace=True) # Delete single Column
# df.drop('D', axis=1, inplace=True)  # Delete single Row  {Notes: axis '1' means Column axis '0' means Row}


# df = df[df > 0]  # check the value which number is positive
# df = df.dropna() #row wise dekbe kun row te kono null nai
# df = df.dropna(axis=1) #Column wise dekbe kun Column te kono null nai
# df = df.dropna(thresh= 2, axis=1) #at list column e 2 ta value thakte hobe
# df = df.fillna(10)  # jei khane null thakbe, sei khane 10 diye fill up kore dibe
# print(df['E'].fillna(df['E'].mean()))


# ...............Pandas DataFrame GroupBy ..............

# data = {
#     'Dept': ['CSE', 'SWE', 'CSE', 'EEE', 'SWE', 'ETE'],
#     'Student_Name': ['Rakib', 'Abu', 'Bakkar', 'Siddik', 'Prious', 'Sarkar'],
#     'Totall_marks': [100, 200, 120, 230, 88, 180]
# }
# index = 'A B C D E F'.split()
# df = pd.DataFrame(data, index=index)
# df = df.groupby('Dept').describe().T
# print(df)


# ...............Pandas Marge concat ..............

# arr = randint(0, 100, 16).reshape(4, 4)
# arr1 = randint(0, 100, 16).reshape(4, 4)
# arr2 = randint(0, 100, 16).reshape(4, 4)
#
# row = 'A B C H'.split()
# col = 'E F G H'.split()
#
# df = pd.DataFrame(data=arr, index=row, columns=col)
# df1 = pd.DataFrame(data=arr1, index=row, columns=col)
# df2 = pd.DataFrame(data=arr2, index=row, columns=col)
# #print(pd.concat([df, df1, df2]))
# #print(pd.merge(df, df1, how='inner', on='H'))
# df.join(df1, how='right')
# df.join(df1, how='left')
# df.join(df1, how='inner')
# df.join(df1, how='outer')

# ...............Pandas Operations..............

#
# arr = randint(0, 100, 16).reshape(4, 4)
# row = 'A B C H'.split()
# col = 'E F G H'.split()
#
# df = pd.DataFrame(data=arr, index=row, columns=col)
# print(df)
# df = df['F'].value_counts()
# df = df['F'].unique()
# print(df)


# d = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4
# }
# d.get('three')


# my_dict = { num: num ** 2 for num in range(10) if num%2 == 0 }
# my_dict



# class Cat:
#     def meow(self):
#         return 'meow!'
#
# s = Cat()
# s.meow()




# class GenericClass:
#     version = 1
#     def __init__(self):
#         pass
# class CompositeClass:
#     def __init__(self):
#         self.generic = GenericClass()
#         self.version = self.generic.version
# c = CompositeClass()
# print(c.version)


# x = (i for i in range(5))
# next(x)


# [i for i in range(5) if i > 2]
# output: [3, 4]


# def make_dict(**kwargs):
#     return kwargs
#
# make_dict(a = 1, b = 2)



