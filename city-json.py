
import json


with open('twocube.city.json', "r") as f:

    data = json.load(f)

a = data['CityObjects']['onebuilding']['geometry'][0]['boundaries']


for i in a:
    lst1=[]
    lst1.append(a)


print(a)


