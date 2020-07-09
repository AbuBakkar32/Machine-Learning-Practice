import requests
import pandas as pd
import csv

# Create your views here.
url = requests.get(
    'https://assets.datacamp.com/production/repositories/1497/datasets/62bd9feef451860db02d26553613a299721882e8/police.csv')
generator = (line.decode('utf-8') for line in url.iter_lines())
reader = list(csv.reader(generator))

lists = []

for row in reader[1:]:
    temp = {
        'state': row[0],
        'stop_date': row[1],
        'stop_time': row[2],
        'county_name': row[3],
        'driver_gender': row[4],
        'driver_race': row[5],
        'violation_raw': row[6],
        'violation': row[7],
        'search_conducted': row[8],
        'search_type': row[9],
        'stop_outcome': row[10],
        'is_arrested': row[11],
        'stop_duration': row[12],
        'drugs_related_stop': row[13],
        'district': row[14]
    }
    lists.append(temp)
col = reader[0]
df = pd.DataFrame(lists, columns=col)
# df.to_csv('police Data.csv')

df = pd.read_csv('police Data.csv')
print(df.get('violation'))
