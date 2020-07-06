import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('auto.csv')
# df_origin = pd.get_dummies(df)
# df_region = pd.get_dummies(df, drop_first=True)
# df_origin = df_origin.drop('origin_Asia', axis=1)
# print(df_origin.head())

df = pd.read_csv('gapminder_all.csv')
df.boxplot('life', 'Region', rot=60)

plt.show()
