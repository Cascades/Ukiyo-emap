import codecs

data = codecs.open('data.txt', 'rb', encoding='utf-16').readlines()

x = 0

themap = {}

def dms_to_dd(input0):
    d = float(input0[:input0.find("°")])
    m = float(input0[input0.find("°")+1:input0.find("′")])
    s = float(input0[input0.find("′")+1:])

    return (d + m/60 + s/3600)

while x < len(data):
    longlat = data[x+1].strip()[:-1]
    long = longlat[:longlat.find("″N")]
    lat = longlat[longlat.find("″N")+2:-2]

    themap[int(x/2+1)] = [data[x].strip()[1:].replace("/", "&"),dms_to_dd(long),dms_to_dd(lat)]
    x += 2

for key in themap:
    print(str(key) + " : " + str(themap[key]))

import urllib.request
import re

fp = urllib.request.urlopen("https://en.wikipedia.org/wiki/One_Hundred_Famous_Views_of_Edo")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

image_sets = ["https://commons.wikimedia.org/wiki/File:" + im.split(", ")[1].split("/")[-2] for im in re.findall('srcset="(.*)" data-file-width', mystr)]

final_images = []

useless = 0
for i in image_sets:
    if useless < 7:
        useless += 1
        continue
    fp = urllib.request.urlopen(i)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    final_url = re.findall('<a href="(https.*)" class.*Original file<\/a>', mystr)
    if "Fudo_Wasserfall" in final_url[0]:
        continue
    final_images.append(final_url[0])

print(len(themap), len(final_images))

import urllib

for index in range(1,120):
    #urllib.request.urlretrieve(final_images[index-1], str(index) + " - " + str(themap[index][0]) + ".jpg")
    print("L.circleMarker([" + str(themap[index][1]) + ", " + str(themap[index][2]) + "], {radius: 10, color: '#ff0000'}).addTo(mymap).on('click', function() { open_image(\"B" + str(index) + "\") }); //" + str(themap[index][0]))
