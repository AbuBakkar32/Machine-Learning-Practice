import matplotlib.pyplot as plt

# x = [5, 8, 10]
# y = [12, 16, 6]
#
# x2 = [6, 9, 11]
# y2 = [6, 15, 7]

# plt.plot(x, y, 'g', label='line one', linewidth=5)
# plt.plot(x2, y2, 'c', label='line two', linewidth=5)
#
# plt.title('Epic Info')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.legend()
# plt.grid(True, color='r')
# plt.show()

# -------------------------------------------- Bar plot show -------------------------------------------

# plt.bar(x, y, align='center')
# plt.bar(x2, y2, color='g', align='center')
#
# plt.title('Epic Info')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()

# -------------------------------------------- Scatter plot show -------------------------------------------


# plt.scatter(x, y)  # , align='center')
# plt.scatter(x2, y2, color='g')  # , align='center')
#
# plt.title('Epic Info')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
#
# plt.show()

# -------------------------------------------- stackplot plot show -------------------------------------------


# days = [1, 2, 3, 4, 5]
#
# sleeping = [7, 8, 6, 11, 7]
# eating = [2, 3, 4, 3, 2]
# working = [7, 8, 7, 2, 2]
# playing = [8, 5, 7, 8, 13]
#
# plt.plot([], [], color='m', label='Sleeping', linewidth=5)
# plt.plot([], [], color='c', label='Eating', linewidth=5)
# plt.plot([], [], color='r', label='Working', linewidth=5)
# plt.plot([], [], color='k', label='Playing', linewidth=5)
#
# plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()

# -------------------------------------------- Pie plot show -------------------------------------------

# slices = [8, 2, 2, 13]
# activities = ['sleeping', 'eating', 'working', 'playing']
# cols = ['c', 'm', 'r', 'b']
#
# plt.pie(slices, labels=activities, colors=cols, startangle=90,
#         shadow=True,
#         explode=(0, 0.1, 0, 0),
#         autopct='%1.1f%%')
#
# plt.title('Interesting Graph\nCheck it out')
# plt.show()

# -------------------------------------------- Website Data filtering clean and plot Show -------------------------------------------

import numpy as np
from matplotlib.dates import bytespdate2num
import urllib.request

stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source_code = urllib.request.urlopen(stock_price_url).read().decode()

stock_data = []
stock = {}
split_source = source_code.split('\n')

for line in split_source[1:]:
    split_line = line.split(',')
    if len(split_line) == 7:
        if 'values' not in line:
            stock_data.append(line)

# for data in stock_data:
#     data1 = data[0:10]
#     data2 = data[11:]
#     stock[data1] = data2
#
# for key, value in stock.items():
#     print(f'According to this Date: "{key}" all data should be "{value}"')

date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data, delimiter=',', unpack=True,
                                                                  converters={0: bytespdate2num('%Y-%m-%d')})

plt.plot_date(date, closep, '-', label='Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()


# -----------------------------------------------------------------------------------------------------------------------------------
