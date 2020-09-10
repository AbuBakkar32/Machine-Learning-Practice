import phonenumbers
from phonenumbers import geocoder, geodata

data = phonenumbers.parse('+8801689040992')
# putput = geocoder.country_name_for_number(data, 'en')
putput = geocoder.description_for_valid_number(data, 'en')
print(putput)

