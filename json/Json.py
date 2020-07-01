from datetime import time

import requests
import json

r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()
results = []

for package in packages_json[0:]:
    try:
        package_name = package['name']
        package_desc = package['desc']

        packages_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

        r = requests.get(packages_url)
        package_json = r.json()

        installs_30 = package_json['analytics']['install']['30d'][package_name]
        installs_90 = package_json['analytics']['install']['90d'][package_name]
        installs_365 = package_json['analytics']['install']['365d'][package_name]

        data = {
            'name': package_name,
            'desc': package_desc,
            'analytics': {
                '30d': installs_30,
                '90d': installs_90,
                '365d': installs_365,
            }
        }
        results.append(data)
        print(f'Got {package_name} in {r.elapsed.total_seconds()} seconds')
    except:
        pass
with open('test.json', 'a') as f:
    json.dump(results, f, indent=2)
