import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

r = requests.get('https://www.cia.gov/library/publications/the-world-factbook/fields/204.html#AF')
c = r.content
soup = BeautifulSoup(c, 'html.parser')
data = soup.findAll('tr')[1:]

data_dictionary = []
for country in data:
    try:
        country_name = country.findAll('td', {'class': 'country'})[0].text
        country_name_formatted = country_name.replace('\n', "")
        internet_percentage = country.findAll('span', {'class': 'subfield-number'})[1].text
        internet_percentage_formatted = float(internet_percentage.replace("%", ""))
        data_dictionary.append({'country': country_name_formatted, "percentage of population with internet access": internet_percentage_formatted})
    except:
        pass
print(data_dictionary)

internet_stats = pd.DataFrame.from_dict(data_dictionary)
dataMarge = internet_stats.iloc[0:10, 0:]

sns.pairplot(dataMarge, x_vars=dataMarge.columns[0], y_vars=dataMarge.columns[1])
plt.show()