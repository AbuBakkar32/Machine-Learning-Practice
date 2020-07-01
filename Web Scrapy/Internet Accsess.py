import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.cia.gov/library/publications/the-world-factbook/fields/204.html#AF')
c = r.content
soup = BeautifulSoup(c, parser='html_parser')
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