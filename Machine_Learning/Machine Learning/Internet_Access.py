#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


r = requests.get('https://www.cia.gov/library/publications/the-world-factbook/fields/204.html#AF')
c = r.content
soup = BeautifulSoup(c)


# In[7]:


soup


# In[4]:


data = soup.findAll('tr')[1:]


# In[9]:


a = soup.findAll('tr')[1].findAll('td', {'class': 'country'})[0].text


# In[10]:


b = a.replace('\n', '')


# In[14]:


soup.findAll('tr')[1].findAll('span', {'class': 'subfield-number'})[1].text


# In[110]:


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


# In[113]:


import pandas as pd


# In[114]:


internet_stats_df = pd.DataFrame.from_dict(data_dictionary)


# In[115]:


internet_stats_df


# In[ ]:




