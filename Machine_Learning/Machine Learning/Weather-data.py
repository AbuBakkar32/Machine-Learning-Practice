#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json


# In[42]:


noaa_token = 'IKcIsYWSNDjAknPHhKjPeOlxothIJpBs'


# In[70]:


headers = {'token': 'IKcIsYWSNDjAknPHhKjPeOlxothIJpBs'}


# In[145]:



r = requests.get("https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CNTRY&begindate=2016-01-01&enddate=2016-12-31&limit=201", headers=headers)


# In[146]:


data = r.json()


# In[147]:


data


# In[148]:


country_ids = []
for country in data['results']:
    country_ids.append({country['name']: country['id']})


# In[150]:


country_ids[:2]


# In[ ]:


parameters = {'locationid'}


# In[216]:


r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/datacategories?locationid=FIPS:AR', headers=headers)


# In[217]:


data = r.json()


# In[218]:


data


# In[264]:


r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&locationid=FIPS:AR&startdate=2016-01-01&enddate=2016-12-31&limit=270', headers=headers)


# In[265]:


data = r.json()


# In[266]:


data


# In[ ]:




