from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

ladd1 = "27488 Stanford Avenue, North Dakota"
print("Location address:", ladd1)
location = geolocator.geocode(ladd1)
print("Street address, street name: {} ".format(location.address))

ladd2 = "380 New York St, Redlands, CA 92373"
print("\nLocation address:", ladd2)
location = geolocator.geocode(ladd2)
print("Street address, street name: {}".format(location.address))

ladd3 = "1600 Pennsylvania Avenue NW"
print("\nLocation address:", ladd3)
location = geolocator.geocode(ladd3)
print("Street address, street name: {}".format(location.address))

ladd4 = "5/A Dhanmondi,bangladesh"
print("\nLocation address:", ladd4)
location = geolocator.geocode(ladd4)
print("Street address, street name: {}".format(location.address))

# Distance Calculation

# from geopy import distance
# london = ("51.5074° N, 0.1278° W")
# newyork = ("40.7128° N, 74.0060° W")
# print("Distance between London and New York city (in km):")
# print(distance.distance(london, newyork).km," kms")


