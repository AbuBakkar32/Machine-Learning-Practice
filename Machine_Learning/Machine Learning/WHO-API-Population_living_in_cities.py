#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json


# In[28]:


r = requests.get('http://apps.who.int/gho/athena/api/GHO/AIR_3/?format=json')


# In[29]:


data = r.json()


# In[30]:


data


# In[41]:


data['fact'][0]


# In[42]:


data_dictionary = []
for country in data['fact']:
    for category in country['Dim']:
        if category['category'] == "COUNTRY":
            countrycode = category['code']
    data_dictionary.append({"Country Code": countrycode, "Percent Living in Cities > 100k": country['value']['numeric']})


# In[43]:


data_dictionary


# In[44]:


import pandas as pd


# In[45]:


percent_living_in_cities = pd.DataFrame.from_dict(data_dictionary)


# In[46]:


percent_living_in_cities


# In[ ]:




