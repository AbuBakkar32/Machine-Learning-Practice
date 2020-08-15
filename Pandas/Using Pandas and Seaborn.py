import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

people = pd.read_csv('Health.csv')


def Age_groups(age):
    if age <= 35:
        return 'Young'
    elif 35 <= age <= 60:
        return 'Middle Aged'
    else:
        return 'Old'


people['Age Groupe'] = people['Age'].apply(Age_groups)
people['Activity Level'] = people['Miles'].apply(lambda x: 'active' if x > 1 else 'inactive')
print(people)

sns.countplot(x='Age Groupe', hue='Activity Level', data=people)
plt.show()
