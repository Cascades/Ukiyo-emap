from os import listdir
from geopy.geocoders import Nominatim
import re

not_found = []
found = {}

for filename in listdir("C:\\Users\gtatt\Pictures\Hiroshige\The Fifty-three Stations of the Tōkaidō"):
    #print(filename)
    cutoff = [m.start() for m in re.finditer('-', filename)]
    #print(filename[cutoff[0]+2:cutoff[1]-1] + ", Japan")
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode(filename[cutoff[0]+2:cutoff[1]-1] + ", Japan")
    try:
        result = "L.circleMarker([" + str(location.latitude) + ", " + str(location.longitude) + '], 100).addTo(mymap).on(\'click\', function() { open_image("' + filename[:filename.find(" ")] + '") }); //' + filename[cutoff[0]+2:cutoff[1]-1]
        #print(result)
        found[filename[:filename.find(" ")]] = result
    except:
        not_found.append(filename[cutoff[0]+2:cutoff[1]-1] + ", Japan")

for x in range(1,54):
    try:
        print(found[str(x)])
    except:
        pass
print(not_found)


