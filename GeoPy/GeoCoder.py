import geocoder
import folium

geo = geocoder.ip('103.87.214.163')
myAddress = geo.latlng

myApplication = folium.Map(location=myAddress, zoom_start=12, max_zoom=18, position='relative', control_scale=True,
                           zoom_control=True)

folium.CircleMarker(location=myAddress, radius=50, popup="yorkshire").add_to(myApplication)
folium.Marker(myAddress, popup="yorkshire").add_to(myApplication)

myApplication.save('location.html')

