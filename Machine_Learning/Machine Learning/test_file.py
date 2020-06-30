#!/usr/bin/env python
# coding: utf-8

# ##### Importing suicide statistics from WHO API

# In[65]:


import requests
import json
import pandas as pd
r = requests.get('http://apps.who.int/gho/athena/api/GHO/MH_12/.json?filter=Year:2016')
data = r.json()


# ##### Converting JSON data to Python List

# In[66]:


list_of_data = []
for fact in data['fact']:
    for category in fact['Dim']:
        if category['category'] == 'COUNTRY':
            country_code = category['code']
        elif category['category'] == "SEX":
            sex = category['code']
    suicide_rate = fact['value']['numeric']
    list_of_data.append({'Country Code': country_code, 'Sex': sex, "Suicide Rate": suicide_rate})

country_codes = []
for country in list_of_data:
    country_codes.append(country['Country Code'])

country_codes = set(country_codes)

data_dictionary = []
for country in country_codes:
    data_dictionary.append({'Country Code': country, 'Male Suicide Rate':'', 'Female Suicide Rate':'', 'Combined Suicide Rate':''})


# ##### creating Python list with dictionary for each country

# In[67]:


for data in list_of_data:
    for country in data_dictionary:
        if data['Country Code'] == country['Country Code']:
            if data['Sex'] == 'MLE':
                country['Male Suicide Rate'] = data['Suicide Rate']
            elif data['Sex'] == "FMLE":
                country['Female Suicide Rate'] = data['Suicide Rate']
            elif data['Sex'] == 'BTSX':
                country['Combined Suicide Rate'] = data['Suicide Rate']


# ###### Converting to Pandas DataFrame

# In[68]:


suicide_rates = pd.DataFrame.from_dict(data_dictionary,)
suicide_rates.set_index(['Country Code'], inplace=True)
suicide_rates.sort_index(inplace=True)


# In[69]:


suicide_rates.head()


# ##### Adding Country name Data and cleaning

# In[70]:


r = requests.get('http://apps.who.int/gho/athena/api/GHO/MH_12/.json?filter=Year:2016')
data = r.json()
country_names = []
for country in data['dimension'][4]['code']:
    country_names.append({'Country Code': country['label'], 'Country Name': country['display']})

country_names_df = pd.DataFrame.from_dict(country_names)
country_names_df.set_index('Country Code', inplace=True)

country_names_df.loc[country_names_df.index == "MLT"]

# clean Up Country Names
country_names_df.loc[country_names_df['Country Name'] == "Democratic People's Republic of Korea"] = "North Korea"
country_names_df.loc[country_names_df['Country Name'] == "The former Yugoslav republic of Macedonia"] = "Macedonia"
country_names_df.loc[country_names_df['Country Name'] == "Republic of Moldova"] = "Moldova"
country_names_df.loc[country_names_df['Country Name'] == "Iran (Islamic Republic of)"] = "Iran"
country_names_df.loc[country_names_df['Country Name'] == "Russian Federation"] = "Russia"
country_names_df.loc[country_names_df['Country Name'] == "United Kingdom of Great Britain and Northern Ireland"] = "United Kingdom"
country_names_df.loc[country_names_df['Country Name'] == "Venezuela (Bolivarian Republic of)"] = "Venezuela"
country_names_df.loc[country_names_df['Country Name'] == "United States of America"] = "United States"

country_names_df.tail(15)

suicide_rates = suicide_rates.join(country_names_df)
# suicide_rates


# ###### Adding country names

# In[71]:


suicide_rates = suicide_rates[['Country Name', 'Combined Suicide Rate', 'Male Suicide Rate', 'Female Suicide Rate']]
suicide_rates.head()


# In[72]:


suicide_rates.shape


# ##### importing percentage of population living in cities data from WHO API

# In[73]:


r = requests.get('http://apps.who.int/gho/athena/api/GHO/AIR_3/?format=json')
data = r.json()


# ###### Converting JSON data to Python list

# In[74]:


data_dictionary = []
for country in data['fact']:
    for category in country['Dim']:
        if category['category'] == "COUNTRY":
            countrycode = category['code']
    data_dictionary.append({"Country Code": countrycode, "% Living in Cities > 100k": country['value']['numeric']})


# In[75]:


data_dictionary[0]


# ###### Converting info to Pandas DataFrame

# In[76]:


percent_living_in_cities = pd.DataFrame(data_dictionary)
percent_living_in_cities.set_index(['Country Code'], inplace=True)


# ###### Combining with suicide stats DataFrame and Changing NaN values to Median

# In[77]:


suicide_rates = suicide_rates.join(percent_living_in_cities, on=['Country Code'], how='left')


# In[78]:


suicide_rates['% Living in Cities > 100k'].fillna(suicide_rates['% Living in Cities > 100k'].median(), inplace=True)
suicide_rates.isna().sum()


# ###### Scraping Internet Data from CIA World Fact Book using BeautifulSoup

# In[79]:


from bs4 import BeautifulSoup
r = requests.get('https://www.cia.gov/library/publications/the-world-factbook/fields/204.html#AF')
c = r.content
soup = BeautifulSoup(c)


# In[80]:


data = soup.findAll('tr')[1:]


# ##### Scraping country names and internet connectivity info

# In[81]:


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


# ##### Converting to Pandas DataFrame

# In[82]:


internet_stats_df = pd.DataFrame.from_dict(data_dictionary)


# In[83]:


internet_stats_df.columns= ['Country Name', "% of Population with Internet Access"]
internet_stats_df.set_index(['Country Name'], inplace=True)


# In[84]:


internet_stats_df.shape
internet_stats_df.head()


# ##### Combining with other data collected

# In[85]:


suicide_rates = suicide_rates.join(internet_stats_df, on=['Country Name'], how='inner')


# In[86]:


suicide_rates.sort_values(by = "Country Name", ascending = False)
suicide_rates.shape


# ###### Scraping Religous stats

# In[87]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
r = requests.get('https://rationalwiki.org/wiki/Importance_of_religion_by_country')
c = r.content
soup = BeautifulSoup(c)


# In[88]:


data = soup.findAll('table', {'class': 'wikitable'})
data = data[0].findAll('td')


# In[89]:


religous_stats = []
for i in range(len(data)):
    if i == 0 or i % 3 == 0:
        country = data[i].text.strip()
    elif i in list(range(1, len(data), 3)):
        percentage_religious = float(data[i].text.replace("%", ""))
        religous_stats.append({'Country Name': country, "% Religious": percentage_religious})


# In[90]:


religious_df = pd.DataFrame.from_dict(religous_stats)
religious_df.set_index(['Country Name'], inplace=True)
suicide_rates.set_index(['Country Name'], inplace=True)


# In[91]:


suicide_rates.head()
religious_df.head()


# ###### Combine with rest of data

# In[92]:


suicide_rates = suicide_rates.join(religious_df)


# In[93]:


suicide_rates.sort_values(by = "Country Name", ascending = False)
suicide_rates.head()


# ##### Getting Economic and Health Data

# In[94]:


gdp_url = "https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2004.txt"
unemp_url = "https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2129.txt"

import urllib  # the lib that handles the url stuff
import json
import pandas as pd
import numpy as np
from xml.dom import minidom
from urllib.request import urlopen
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


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


# ##### Cleaning data and putting it in Data Frame

# In[95]:


mental1 = mental[mental.Year == 2016]
mental1.dropna(axis = 0, inplace = True)
men_copy = mental1.set_index('Entity')


# ##### Mergin Tables and cleaning new data

# In[96]:


merged = men_copy.join(Unemp)
merged.drop('Year', axis = 1, inplace = True)
merged = merged.join(gdp)
merged.dropna(inplace = True)

#GDP per capita
gdps = [item.split(",") for item in merged.GDP]

def clean_gdp(data):
    empty = []
    for item in data:
        first = item[0].split("$")[1]
        second = item[1]
        total = int(first+second)
        empty.append(total)
    return empty

merged.GDP = clean_gdp(gdps)
merged.sort_values(by = "Entity", ascending = False)
merged[merged.Code == "RUS"]

#Health spending per capita
health = nha.set_index('Countries')
health.rename(columns = {'2016': 'health_spend_perca'}, inplace = True)


new = merged.join(health)
new.loc["Russia", 'health_spend_perca'] = 1414.12
new[new.index == "Russia"]
new.loc["United States", 'health_spend_perca'] = 9869.74
len(new)
final = new.dropna()


# In[97]:


suicide_rates.head()


# ##### Mergin FInal Two Tables

# In[98]:


final_table = final.join(suicide_rates)
final_table.head()
final_table.dropna(subset = ['Combined Suicide Rate'], inplace = True)
final_table['% Religious'].fillna(50, inplace = True)
final_table.head()


# In[99]:


final_table.loc[final_table["% Religious"] > 33, "Religious"] = "Medium"
final_table.loc[final_table["% Religious"] >= 66, "Religious"] = "High"
final_table.loc[final_table["% Religious"] <= 33, "Religious"] = "Low"


# In[100]:


final_table.head()


# ##### Checking for Multicolinearity and removing excess features

# In[101]:


abs(final_table.corr()) > 0.75


# In[102]:


import seaborn as sns
plt.figure(figsize = (8,6))
plt.title("Regular Variables Correlation Heatmap", fontsize = 18, color = "#F97E77")
sns.heatmap(final_table.corr(), center = 0)


# ##### Drop "Bipoar Disorder" since it has very high corelation with 3 other variables.

# In[103]:


# Create correlation matrix
corr_matrix = final_table.corr().abs()

# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

# Find index of feature columns with correlation greater than 0.95
to_drop = [column for column in upper.columns if any(upper[column] > 0.75)]

#Drop variables from table
final_table.drop(columns=to_drop, inplace=True)
final_table.shape
to_drop


# ##### Clean up Some Column Names with too many signs and letters

# In[104]:


final_table.rename(columns = {'Schizophrenia (%)': 'Schizophrenia'}, inplace = True)
final_table.rename(columns = {'Drug use disorders (%)': 'Drug_use'}, inplace = True)
final_table.rename(columns = {'Depression (%)': 'Depression'}, inplace = True)
final_table.rename(columns = {'Alcohol use disorders (%)': 'Alcohol_use'}, inplace = True)
final_table.rename(columns = {'Combined Suicide Rate': 'Combined_suicide_rate'}, inplace = True)
final_table.rename(columns = {'% Living in Cities > 100k': 'urban_population'}, inplace = True)


# In[105]:


final_table.head()


# In[106]:


final_table.shape


# ##### Dropping columns we don't need

# In[107]:


test_table = final_table.drop(columns=['Code', "% Religious"])


# ##### Changing health_spend_perca column to float64 so we can do calcualtions

# In[108]:


test_table.health_spend_perca = test_table.health_spend_perca.map(lambda x: float(x))
test_table.info()


# ##### Creating Dummy variables and dropping one of them plus the main category column

# In[110]:


dummies = pd.get_dummies(test_table['Religious'], prefix="Rel")
test_table = pd.concat([test_table, dummies], axis=1)
test_table.drop(columns=['Religious', ], inplace=True)
test_table.drop(columns=['Rel_Low'], inplace=True)


# ##### Move target colum to the end of table for easier DataFrame navigation

# In[121]:



target = test_table['Combined_suicide_rate']
test_table.drop(columns=['Combined_suicide_rate'], inplace=True)
test_table = pd.concat([test_table, target], axis=1)
test_table.head()

dummies = test_table[['Rel_High', 'Rel_Medium']]
dummies.head()


# In[124]:


from sklearn import preprocessing
y = test_table.Combined_suicide_rate
to_scale = test_table.iloc[:,:-3]
X_scaled = preprocessing.scale(to_scale)
new = pd.DataFrame(X)


# ##### Plot a pairplot of dependent variable to independent variables scatterplot relationships

# In[46]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

variables = list(test_table.columns)[:-1]
sns.pairplot(test_table, x_vars=variables[:7], y_vars=['Combined_suicide_rate'])
sns.pairplot(test_table, x_vars=variables[7:], y_vars=['Combined_suicide_rate'])


# ##### Starting our LinearRgegression process by creating a set of polynomial variables to the power = 2

# In[48]:


from sklearn.preprocessing import PolynomialFeatures
from sklearn import preprocessing, pipeline

poly = preprocessing.PolynomialFeatures(degree=2, interaction_only=False, include_bias=False)
features_poly = pd.DataFrame(poly.fit_transform(test_table.drop(columns=['Combined_suicide_rate'])), columns=poly.get_feature_names(test_table.drop(columns=['Combined_suicide_rate']).columns))

X_poly= features_poly
y= test_table['Combined_suicide_rate']


# ##### Check for Multicollinearity of the Polynomial variables

# In[49]:


import seaborn as sns

sns.set(style="white")


# Compute the correlation matrix
corr = features_poly.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
plt.title("Polynomials Correlation Heatmap", fontsize = 30, color = "#F97E77")
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


# ##### Drop any variable with a .corr() > 0.95

# In[50]:


# Create correlation matrix
corr_matrix = features_poly.corr().abs()

# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

# Find index of feature columns with correlation greater than 0.95
to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]

#Drop variables from table
X_poly.drop(columns=to_drop, inplace=True)
X_poly.shape


# ##### Run Linear Regression Model (80-20 split) and use Cross validation to find model with smallest RMSE

# In[51]:


from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE

X_poly = X_poly
y = test_table['Combined_suicide_rate']

def MSE_test(X_poly, y, random_state = 11):
    poly_RSME = []
    for i in range(1, len(X_poly.columns)):
        linreg = LinearRegression()
        selector = RFE(linreg, n_features_to_select = i)
        selector = selector.fit(X_poly, y)
        selected_columns = X_poly.columns[selector.support_]
        selected_var = [column for column in selected_columns]
        X_train, X_test, y_train, y_test = train_test_split(X_poly[selected_columns], y, random_state = random_state,  test_size=.20)
        linreg.fit(X_train, y_train)
        cv_10_results = np.mean(cross_val_score(linreg, X_train, y_train, cv=50, scoring='neg_mean_squared_error'))
        cv_10_results= np.sqrt(abs(cv_10_results))
        poly_RSME.append(dict(variables = selected_var, RMSE = cv_10_results, nu_var = len( selected_var)))
    return poly_RSME

poly_model_list = MSE_test(X_poly, y)

def find_best_model(model_list):
    sorted_mse = sorted(model_list, key=lambda k: k['RMSE'])
    return sorted_mse[0]
    
find_best_model(poly_model_list)


# ##### Graph the minimized RMSE agains number of selected variables

# In[52]:


import matplotlib.patches as mpatches

min_rmse = find_best_model(poly_model_list)['RMSE']
min_var = find_best_model(poly_model_list)['nu_var']
x_val = [item['nu_var'] for item in poly_model_list[:35]]
y_val = [item['RMSE'] for item in poly_model_list[:35]]
plt.figure(figsize = (9,7))
plt.title("Minimizing RMSE Function", fontsize = 25, color = "#073A5A")
plt.plot(x_val, y_val)
plt.xlabel("Number of Independent Variables", fontsize = 18, color = "#073A5A")
plt.ylabel("RMSE", fontsize = 18, color = "#073A5A")

rmse_patch = mpatches.Patch(color='blue', label="RMSE = {}".format(round(min_rmse, 3)))
vars_patch = mpatches.Patch(color='green', label="Variables Chosen = {}".format(min_var))
plt.legend(handles=[rmse_patch, vars_patch])


# ##### Now Test the model against the test data alone and return R2, z_score, and RMSE

# In[53]:


selected_variables = find_best_model(poly_model_list)['variables']
selected_variables
X_train, X_test, y_train, y_test = train_test_split(X_poly[selected_variables], y, random_state = 11,  test_size=.20)
linreg = LinearRegression()
linreg.fit(X_train[selected_variables], y_train)
yhat = linreg.predict(X_test[selected_variables])

RMSE = np.sqrt(mean_squared_error(y_test, yhat))
z_score = RMSE/np.std(y_test)
R_squared = linreg.score(X_test, y_test)
print("RMSE = {}, z_score = {}, R_squared = {}".format(RMSE, z_score, R_squared))


# ##### Graph our final results as a scatterplot of y_test_predicted vs. y_test_actual values

# In[54]:


import matplotlib.patches as mpatches


def bias(y, y_hat):
    return np.mean(y_hat - y)

def variance(y_hat):
    return np.mean([yi**2 for yi in y_hat]) - np.mean(y_hat)**2

selected_columns = find_best_model(poly_model_list)['variables']
X_train, X_test, y_train, y_test = train_test_split(X_poly[selected_columns], y, random_state = 11,  test_size=.20)

reg = LinearRegression().fit(X_train, y_train)

y_hat_train = reg.predict(X_train)
y_hat_test = reg.predict(X_test)
bias_train = bias(y_train, y_hat_train)
bias_test = bias(y_test, y_hat_test)
var_train = variance(y_hat_train)
var_test = variance(y_hat_test)

RMSE_train = np.sqrt(mean_squared_error(y_train, y_hat_train))
z_score_train = RMSE/np.std(y_train)
R_squared_train = linreg.score(X_train, y_train)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize = (15,5))

ax1.set_title("Polynomial y_hat vs y_train")
ax1.set_xlabel("y_train_poly")
ax1.set_ylabel("y_hat_train")
ax1.scatter(y_train, y_hat_train, color = "blue", label='Actual Data')
ax1.plot(y_train, y_train, color = "red", label='Model')

R2_patch = mpatches.Patch(color='#aaff80', label="R_squared_train = {}".format(round(R_squared_train, 3)))
RMSE_patch = mpatches.Patch(color='#ffd480', label="RMSE_train = {}".format(round(RMSE_train, 3)))
z_patch = mpatches.Patch(color='#00cccc', label="z_score_train = {}".format(round(z_score_train, 3)))
Bias_patch = mpatches.Patch(color='#670000', label="Bias_train = {}".format(round(bias_train, 20)))
Variance_patch = mpatches.Patch(color='#7A9A01', label="Var_train = {}".format(round(var_train, 3)))

ax1.legend(handles=[R2_patch, RMSE_patch, z_patch, Bias_patch, Variance_patch])

ax2.set_title("Polynomial y_hat vs y_test")
ax2.set_xlabel("y_test_poly")
ax2.set_ylabel("y_hat_test")
ax2.scatter(y_test, y_hat_test, color = "blue")
ax2.plot(y_test, y_test, color = "red")

R2_patch = mpatches.Patch(color='#aaff80', label="R_squared = {}".format(round(R_squared, 3)))
RMSE_patch = mpatches.Patch(color='#ffd480', label="RMSE = {}".format(round(RMSE, 3)))
z_patch = mpatches.Patch(color='#00cccc', label="z_score = {}".format(round(z_score, 3)))
Bias_patch = mpatches.Patch(color='#670000', label="Bias = {}".format(round(bias_test, 3)))
Variance_patch = mpatches.Patch(color='#7A9A01', label="Var = {}".format(round(var_test, 3)))

ax2.legend(handles=[R2_patch, RMSE_patch, z_patch,  Bias_patch, Variance_patch], loc = "upper left")

# x_val = yhat
# y_val = y_test
# plt.figure(figsize = (9,7))
# plt.title("Comparing y_test to y_hat values", fontsize = 22, color = "#096396")
# plt.scatter(x_val, y_val)
# plt.xlabel("Predicted Suicide Rates", fontsize = 18, color = "#096396")
# plt.ylabel("Actual Suicide Rates", fontsize = 18, color = "#096396")
# plt.plot(x_val, x_val, color = "red")





# ##### Print our final euqation to get a sense of individual variable relationships

# In[83]:


test = list(zip(linreg.coef_, selected_variables))
combined = [str(round(item[0], 2)) + "*" +item[1] for item in test]
one_string = "  +  ".join(combined)
equation = one_string.replace("+  -", "-  ")


# In[84]:


print("y = {} + {}".format(round(linreg.intercept_, 2), equation))


# ##### Plot a Barchart of Independent variables to visualize Variable weight

# In[85]:


coefs = [item[0] for item in test]
varias = [item[1] for item in test]
plt.figure(figsize = (9,7))
plt.title("Independent Variables Chart", fontsize = 30, color = "#535355")
plt.xlabel("Independent Variable", fontsize = 18, color = "#050594")
plt.ylabel("Coefficient Size", fontsize = 18, color = "#050594")
plt.xticks(rotation=90)
plt.bar(varias, coefs)


# ###                                        HURRAY!!!  WE DONE!!!
