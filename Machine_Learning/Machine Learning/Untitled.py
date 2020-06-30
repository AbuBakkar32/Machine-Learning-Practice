#!/usr/bin/env python
# coding: utf-8

# In[126]:


gdp_url = "https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2004.txt"
unemp_url = "https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2129.txt"
econ_url = "https://data.theglobaleconomy.com/data_export_api.php?tp=1&ind=338,184,353,52,10,154,334,333,361,120&cnt=AF,AL,DZ,AD,AO,AG,AR,AM,AW,AU,AT,AZ,BS,BH,BD,BB,BY,BE,BZ,BJ,BM,BT,BO,BA,BW,BR,BN,BG,BF,MM,BI,KH,CM,CA,CV,CF,TD,CL,CN,CO,KM,CR,HR,CU,CY,CZ,CD,DK,DJ,DM,DO,EC,EG,SV,GQ,ER,EE,ET,FO,FJ,FI,FR,GA,GM,GE,DE,GH,GI,GR,GD,GT,GN,GW,GY,HT,VA,HN,HK,HU,IS,IN,ID,IR,IQ,IE,IL,IT,CI,JM,JP,JO,KZ,KE,KI,KW,KG,LA,LV,LB,LS,LR,LY,LI,LT,LU,MO,MK,MG,MW,MY,MV,ML,MT,MR,MU,MX,FM,MD,MC,MN,ME,MS,MA,MZ,NA,NP,NL,NC,NZ,NI,NE,NG,NF,KP,NO,OM,PK,PW,PS,PA,PG,PY,PE,PH,PL,PT,PR,QA,CG,RO,RU,RW,LC,VC,WS,SM,ST,SA,SN,RS,SC,SL,SG,SK,SI,SB,SO,ZA,KR,ES,LK,SD,SR,SZ,SE,CH,SY,TW,TJ,TZ,TH,TG,TO,TT,TN,TR,TM,TV,UG,UA,AE,GB,UY,US,UZ,VU,VE,VN,YE,ZM,ZW&prd=2014:2018&uid=52418&uidc=2c0f8f9fb939db747eb52f0b97a60b5e"
import urllib  # the lib that handles the url stuff
import json
import pandas as pd
import numpy as np
from xml.dom import minidom
from urllib.request import urlopen


GDP = pd.read_fwf('gdp_perca.txt', header = None, names = ['country', 'GDP']).astype(str)
Unemp = pd.read_fwf('unemp.txt', header = None, names = ['Unem_rate'])
mental = pd.read_csv('mental_disorder_substance_use.csv')
healthcare = pd.read_excel('NHA.xlsx')

      
index_list = [item[1] for item in Unemp.index]
Unemp.index = index_list
Unemp.head()

gdp = GDP.set_index('country')
health = healthcare[["Countries", '2016']]
nha = health.drop([0], axis = 0)


# In[127]:


mental1 = mental[mental.Year == 2016]


# In[128]:


mental1.dropna(axis = 0, inplace = True)
mental1.head()


# In[129]:


men_copy = mental1.set_index('Entity')


# In[130]:


Unemp.head()


# In[131]:


merged = men_copy.join(Unemp)


# In[132]:


merged.drop('Year', axis = 1, inplace = True)


# In[133]:


merged.head()


# In[134]:


import seaborn as sns


# In[135]:


sns.heatmap(merged.corr(), center = 0)


# In[136]:


merged = merged.join(gdp)


# In[137]:


merged.head()


# In[138]:


merged.dropna(inplace = True)


# In[139]:


merged.tail()


# In[140]:


gdps = [item.split(",") for item in merged.GDP]

def clean_gdp(data):
    empty = []
    for item in data:
        first = item[0].split("$")[1]
        second = item[1]
        total = first+second
        empty.append(total)
    return empty
        


# In[141]:


merged.GDP = clean_gdp(gdps)


# In[142]:


merged.sort_values(by = "Entity", ascending = False)
merged[merged.Code == "RUS"]


# In[143]:


nha.head()


# In[144]:


health = nha.set_index('Countries')
health.rename(columns = {'2016': 'health_spend_perca'}, inplace = True)
health.head()


# In[145]:


new = merged.join(health)
new.loc["Russia", 'health_spend_perca'] = 1414.12
new[new.index == "Russia"]
new.loc["United States", 'health_spend_perca'] = 9869.74


# In[146]:


new.sort_values(by ='health_spend_perca', ascending=False)


# In[147]:


final = new.dropna()


# In[148]:


int(final.GDP[1])


# In[149]:


test = [int(item) for item in final.GDP]


# In[150]:


final.info()


# In[151]:


pd.plotting.scatter_matrix(final, figsize = [12, 12])


# In[152]:


abs(final.corr()) > 0.75


# In[153]:


#Dropping multicorelated variable = Bipolar Disorder
final.drop("Bipolar disorder (%)", axis = 1, inplace = True)


# In[157]:


final.head()


# In[162]:


len(final)


# In[ ]:




