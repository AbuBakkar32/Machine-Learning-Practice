import pandas as pd
import matplotlib.pyplot as plt
import sklearn.model_selection

df = pd.read_csv('mental_disorder_substance_use.csv')
dataa = df.iloc[:, 4:6]
print(df.iloc[:50,:])
dataa.plot(subplots=True)
dataa.plot(kind='hist')

plt.title('Group Off Albania Disorder (%)')
plt.grid()
plt.show()

# -------------------------------------------------------------------------------

# print(df['Depression (%)'].min())
# print(df['Depression (%)'].max())
# mean = df.mean(axis='columns')
# mean.plot()
# df.plot()
# plt.show()

# -------------------------------------------------------------------------------

# print(df['Depression (%)'].describe())
# df['Depression (%)'].plot(kind='box')
# plt.show()

# -------------------------------------------------------------------------------

# # Print the number of countries reported in 2015
# print(df['Depression (%)'].count())
#
# # Print the 5th and 95th percentiles
# print(df.quantile([0.05, 0.95]))
#
# # Generate a box plot
# years = ['Depression (%)', 'Drug use disorders (%)', 'Alcohol use disorders (%)', 'Anxiety disorders (%)', 'Eating disorders (%)']
# df[years].plot(kind='box')
# plt.show()

# -------------------------------------------------------------------------------
