from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
import phonenumbers
import opencage
from myphone import number
import folium


from phonenumbers import geocoder


pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))


key = '35bfd77f2bcf45b8a115a66c5e7cc232'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
