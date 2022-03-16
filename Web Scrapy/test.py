import numpy as np
import pandas as pd

# base_url = 'https://chaldal.com/popular'
# response = requests.get(base_url)
# soup = BeautifulSoup(response.content, "lxml")
# soup = soup.html
# if soup.find('ul', class_='hasSelection level-0') is None:
#     ul = soup.find('ul', class_='level-0')
#     print(ul.li)
# else:
#     ul = soup.find('ul', class_='hasSelection level-0')
#     li = ul.find_all('li')
#     print(li[2])

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
a = pd.DataFrame(np.random.random_sample(2000).reshape(100, 20))
# print(np.random.choice(2, 100, replace={1: True, 0: False}))
print(np.random.random_sample(2000).reshape(100, 20))
# a.to_csv('test.csv')
