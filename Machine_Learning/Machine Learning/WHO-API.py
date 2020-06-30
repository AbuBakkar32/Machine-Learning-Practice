#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json


# In[43]:


r = requests.get('http://apps.who.int/gho/athena/api/GHO/.json?filter=Year:2016')
data = r.json()
data


# In[3]:


import pandas as pd
suicide_rates = pd.DataFrame(columns=['Country Code', 'Male Suicide Rate', 'Female Suicide Rate', 'Combined Suicide Rate'])


# In[4]:


list_of_data = []
for fact in data['fact']:
    for category in fact['Dim']:
        if category['category'] == 'COUNTRY':
            country_code = category['code']
        elif category['category'] == "SEX":
            sex = category['code']
    suicide_rate = fact['value']['numeric']
    list_of_data.append({'Country Code': country_code, 'Sex': sex, "Suicide Rate": suicide_rate})
    


# In[5]:


list_of_data


# In[6]:


country_codes = []
for country in list_of_data:
    country_codes.append(country['Country Code'])


# In[7]:


country_codes = set(country_codes)


# In[8]:


len(country_codes)


# In[9]:


data_dictionary = []
for country in country_codes:
    data_dictionary.append({'Country Code': country, 'Male Suicide Rate':'', 'Female Suicide Rate':'', 'Combined Suicide Rate':''})


# In[10]:


len(data_dictionary)


# In[11]:


for data in list_of_data:
    for country in data_dictionary:
        if data['Country Code'] == country['Country Code']:
            if data['Sex'] == 'MLE':
                country['Male Suicide Rate'] = data['Suicide Rate']
            elif data['Sex'] == "FMLE":
                country['Female Suicide Rate'] = data['Suicide Rate']
            elif data['Sex'] == 'BTSX':
                country['Combined Suicide Rate'] = data['Suicide Rate']
            


# In[12]:


data_dictionary


# In[13]:


suicide_rates = pd.DataFrame.from_dict(data_dictionary,)


# In[14]:


suicide_rates.set_index(['Country Code'], inplace=True)


# In[15]:


suicide_rates.sort_index(inplace=True)


# In[16]:


suicide_rates


# In[33]:


data['dimension'][4]['code'][0]


# In[34]:


country_names = []
for country in data['dimension'][4]['code']:
    country_names.append({'Country Code': country['label'], 'Country Name': country['display']})


# In[36]:


country_names_df = pd.DataFrame.from_dict(country_names)


# In[38]:


country_names_df.set_index(['Country Code'], inplace=True)


# In[39]:


suicide_rates = suicide_rates.join(country_names_df, on=['Country Code'], how='inner')


# In[41]:


suicide_rates = suicide_rates[['Country Name', 'Combined Suicide Rate', 'Male Suicide Rate', 'Female Suicide Rate']]


# In[42]:


suicide_rates


# In[ ]:




