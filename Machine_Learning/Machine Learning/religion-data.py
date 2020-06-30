#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


r = requests.get('https://rationalwiki.org/wiki/Importance_of_religion_by_country')
c = r.content
soup = BeautifulSoup(c)


# In[25]:


data = soup.findAll('table', {'class': 'wikitable'})


# In[26]:


data = data[0].findAll('td')


# In[22]:


countries_list = []
religion_list = []
for i in range(len(data)):
   if i % 2 == 0:
       country = abc[i].text
       countries_list.append(country)
   else:
       religions = abc[i].text.split()
       religion = religions[0]
       religion_list.append(religion)
religion_table = [dict(Country = item[0], Religion = item[1]) for item in list(zip(countries_list, religion_list))]
religion_table

religion_df = pd.DataFrame(religion_table)
religion_df.Religion.value_counts()


# In[41]:


data[7].text


# In[34]:


list(range(1, len(data), 3))


# In[46]:


religous_stats = []
for i in range(len(data)):
    if i == 0 or i % 3 == 0:
        country = data[i].text.strip()
    elif i in list(range(1, len(data), 3)):
        percentage_religious = float(data[i].text.replace("%", ""))
        religous_stats.append({'Country Name': country, "% Religious": percentage_religious})


# In[47]:


religous_stats


# In[48]:


religious_df = pd.DataFrame.from_dict(religous_stats)


# In[50]:


religious_df.set_index(['Country Name'], inplace=True)


# In[51]:


religious_df


# In[ ]:




