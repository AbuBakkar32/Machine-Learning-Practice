# Importing the required module.
from countryinfo import CountryInfo

# Getting a country name from the user.
count = input("Please enter your country name: ")
country = CountryInfo(count)

# print(country.info()) # It returns the object with all the info about the country.

# Different APIs to get the data as per the requirements.
print("Others names : ", country.alt_spellings())
print("Capital is : ", country.capital())
print("Currencies is :", country.currencies())
print("Language is : ", country.languages())
print("Borders are : ", country.borders())

print(country.area())
print(country.calling_codes())
print(country.capital_latlng())
print(country.demonym())
print(country.latlng())
print(country.population())
print(country.region())
print(country.subregion())
print(country.timezones())
print(country.tld())
print(country.translations())
print(country.wiki())
print(country.flag())
print(country.native_name())
print(country.geo_json())
print(country.info())
print(country.provinces())
print(country.name())


