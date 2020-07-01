import requests
from bs4 import BeautifulSoup

"""url = requests.get('https://www.prothomalo.com/')
soup = BeautifulSoup(url.text, 'html.parser')
result = soup.find_all('span', attrs={'class': 'tab_list_title'})
print(result)
for i in result:
    link = i.find('a')['href']
    span = i.find('span').text
    print(link)
    print(span)"""

# This US Government site Active visitors With JSON

"""
import requests

url = 'https://analytics.usa.gov/data/live/realtime.json'
j = requests.get(url).json()
print("Number of people visiting a U.S. government website-")
print("Active Users Right Now:")
print(j['data'][0]['active_visitors'])
print(j['taken_at'])"""

# Write a Python program to that retrieves an arbitary Wikipedia page of "Python" and creates a list of links on that page.

"""from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Python")
soup = BeautifulSoup(html, 'lxml')
result = soup.find_all('a')

for link in result:
    if 'href' in link.attrs:
        links = link.attrs['href'][1:]
        print(links)"""

# Python Web Scraping: Check whether a page contains a title or not
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

    title = getTitle(url)
    if title == None:
        return "Title could not be found"
    else:
        return title


print(getTitle("https://www.w3resource.com/"))
print(getTitle("http://www.example.com/"))"""

# Python Web Scraping: Get the number of followers of a given twitter account


"""from bs4 import BeautifulSoup
import requests

handle = input('Input your account name on Twitter: ')
temp = requests.get('https://twitter.com/' + handle)
data = BeautifulSoup(temp.text, 'lxml')
try:
    following_box = data.find('li', {'class': 'ProfileNav-item ProfileNav-item--following'})
    following = following_box.find('a').find('span', {'class': 'ProfileNav-value'})
    print("{} is following {} people.".format(handle, following.get('data-count')))

    follow_box = data.find('li', {'class': 'ProfileNav-item ProfileNav-item--followers'})
    followers = follow_box.find('a').find('span', {'class': 'ProfileNav-value'})
    print("Number of followers: {} ".format(followers.get('data-count')))

    favorite_box = data.find('li', {'class': 'ProfileNav-item ProfileNav-item--favorites'})
    favorite = favorite_box.find('a').find('span', {'class': 'ProfileNav-value'})
    print("Number of post {}  liked are {}: ".format(handle, favorite.get('data-count')))
except:
    print('Account name not found...')"""

# Python Web Scraping: Scrap number of tweets of a given Twitter account


"""from bs4 import BeautifulSoup
import requests

handle = input('Input your account name on Twitter: ')
ctr = int(input('Input number of tweets to scrape: '))
res = requests.get('https://twitter.com/' + handle)
data = BeautifulSoup(res.content, 'lxml')
all_tweets = data.find_all('div', {'class': 'tweet'})
if all_tweets:
    for tweet in all_tweets[:ctr]:
        context = tweet.find('div', {'class': 'context'}).text.replace("\n", " ").strip()
        content = tweet.find('div', {'class': 'content'})
        header = content.find('div', {'class': 'stream-item-header'})
        user = header.find('a', {'class': 'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace("\n"," ").strip()
        time = header.find('a', {'class': 'tweet-timestamp js-permalink js-nav js-tooltip'}).find('span').text.replace("\n", " ").strip()
        message = content.find('div', {'class': 'js-tweet-text-container'}).text.replace("\n", " ").strip()
        footer = content.find('div', {'class': 'stream-item-footer'})
        stat = footer.find('div', {'class': 'ProfileTweet-actionCountList u-hiddenVisually'}).text.replace("\n"," ").strip()
        if context:
            print(context)
        print(user, time)
        print(message)
        print(stat)
        print()
else:
    print("List is empty/account name not found.")"""

# Write a Python program to download IMDB's Top 250 data (movie name, Initial release, director name and stars).


"""from bs4 import BeautifulSoup
import requests
import re

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index)) - (len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(data)

for item in imdb:
    print(item['place'], '-', item['movie_title'], '(' + item['year'] + ') -', 'Starring:', item['star_cast'])"""

# Write a Python program to get the number of magnitude 4.5+ earthquakes detected worldwide by the USGS.

""" 
#https://bit.ly/2lVhlLX
# landing page:
# http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
import csv
import requests
csvurl = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv'
rows = list(csv.DictReader(requests.get(csvurl).text.splitlines()))
print("The number of magnitude 4.5+ earthquakes detected worldwide by the USGS:", len(rows))
  
"""

# Write a Python program to display the date, days, title, city, country of next 25 Hackevents.


"""
import requests
from bs4  import BeautifulSoup
res = requests.get('https://hackevents.co/hackathons')
bs = BeautifulSoup(res.text, 'lxml')
hacks_data = bs.find_all('div',{'class':'hackathon '})
for i,f in enumerate(hacks_data,1):
    hacks_month = f.find('div',{'class':'date'}).find('div',{'class':'date-month'}).text.strip()
    hacks_date = f.find('div',{'class':'date'}).find('div',{'class':'date-day-number'}).text.strip()
    hacks_days = f.find('div',{'class':'date'}).find('div',{'class':'date-week-days'}).text.strip()
    hacks_final_date = "{} {}, {} ".format(hacks_date, hacks_month, hacks_days )
    hacks_name = f.find('div',{'class':'info'}).find('h2').text.strip()
    hacks_city = f.find('div',{'class':'info'}).find('p').find('span',{'class':'city'}).text.strip()
    hacks_country = f.find('div',{'class':'info'}).find('p').find('span',{'class':'country'}).text.strip()
    print("{:<5}{:<15}: {:<90}: {}, {}\n ".format(str(i)+')',hacks_final_date, hacks_name.title(), hacks_city, hacks_country))
  
"""

# Python Web Scraping: Display the contains of different attributes of a specified resource

"""
import requests
response = requests.get('https://python.org')
print("Status Code: ",response.status_code)
print("Headers: ",response.headers)
print("Url: ",response.url)
print("History: ",response.history)
print("Encoding: ",response.encoding)
print("Reason: ",response.reason)
print("Cookies: ",response.cookies)
print("Elapsed: ",response.elapsed)
print("Request: ",response.request)
print("Content: ",response._content)
  
"""

# Write a Python program to get the latest number of confirmed, deaths, recovered and active cases of Novel Coronavirus (COVID-19) Country wise.

"""import pandas as pd
import requests
import csv

url = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
decode = (line.decode('utf-8') for line in url.iter_lines())
reader = list(csv.reader(decode))
lists = []
for row in reader[1:]:
    temp = {
        'country': row[1],
        'Last Update': row[2],
        'Confirmed': row[3],
        'Deaths': row[4],
        'Recovered': row[5]
    }
    lists.append(temp)
dp = pd.DataFrame(lists, columns=['Country', 'Last Update', 'Confirmed', 'Deaths', 'Recovered'])
data = dp.to_csv('Corona_Update.csv', index=True, encoding='utf-8')"""

"""covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
result = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
print(result)"""

# Write a Python program to create a plot (lines) of total deaths, confirmed, recovered and active cases Country wise where deaths greater than 150.

"""import pandas as pd
import matplotlib.pyplot as plt

covid_data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-19-2020.csv', usecols=['Last Update', 'Country/Region', 'Confirmed', 'Deaths', 'Recovered'])
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
r_data = covid_data.groupby(["Country/Region"])["Deaths", "Confirmed", "Recovered", "Active"].sum().reset_index()
print(r_data)
r_data = r_data.sort_values(by='Deaths', ascending=False)
r_data = r_data[r_data['Deaths'] > 50]
plt.figure(figsize=(15, 5))
plt.plot(r_data['Country/Region'], r_data['Deaths'], color='red')
plt.plot(r_data['Country/Region'], r_data['Confirmed'], color='green')
plt.plot(r_data['Country/Region'], r_data['Recovered'], color='blue')
plt.plot(r_data['Country/Region'], r_data['Active'], color='black')

plt.title('Total Deaths(>150), Confirmed, Recovered and Active Cases by Country')
plt.show()"""

# Python Exercise: Visualize the state/province wise Active cases of Novel Coronavirus in USA
"""import pandas as pd
import plotly.express as px

covid_data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-18-2020.csv')
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
us_data = covid_data[covid_data['Country/Region'] == 'US'].drop(['Country/Region', 'Latitude', 'Longitude'], axis=1)
us_data = us_data[us_data.sum(axis=1) > 0]
us_data = us_data.groupby(['Province/State'])['Active'].sum().reset_index()
us_data_death = us_data[us_data['Active'] > 0]
print(us_data)

        df = pd.DataFrame({'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]})
        print(df)
        fig = px.bar(df, x='X', y='Y')
        fig.show()

state_fig = px.bar(us_data_death, x='Province/State', y='Active', title='State wise recovery cases of COVID-19 in USA', text='Active')
state_fig.show()"""

"""import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(141)
plt.bar(names, values)

plt.subplot(142)
plt.scatter(names, values)

plt.subplot(143)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()"""

"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('E:\Coalpublic2013.xlsx')
# result = df[(df['hire_date'] >='Jan-2005') & (df['hire_date'] <= 'Dec-2006')].head()
plt.figure(figsize=(100, 3))
plt.plot(df['Mine_Name'], df['Production'], color='red')
plt.plot(df['Mine_Name'], df['Labor_Hours'], color='green')
plt.xlabel('Dataset')
plt.ylabel('Number of Dataset')
plt.title('Dataset of different type of paper')
#plt.show()"""

"""import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get('https://corona.gov.bd/')
soup = BeautifulSoup(url.text, 'html.parser')
find = soup.find_all('a')
keep = []
count = 0
for list in find:
    f = list.get('href')
    keep.append(f)
    for i in keep:
        do = i
        count +=1
    print(do)
print(count)"""

"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]})
print(df)
plt.plot(df)
plt.show()"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.plot(names, values)
plt.show()

