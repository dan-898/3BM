
import json, sys, threading


with open('twocube.city.json', "r") as f:

    data = json.load(f)

#a = data['CityObjects']['onebuilding']['geometry'][0]['boundaries']
a = data["CityObjects"]["onebuilding"]["geometry"]


for index, i in enumerate(a):
    # print(i["boundaries"][0])
    for p in i["boundaries"][0]:
        print(f"lijst: {index}, waarde: {p[0]}")
        for x in p[0]:
            print(f"enkel element: {x}, uit lijst: {index}")

sys.exit()

#
# for i in a:
#     lst1=[]
#     lst1.append(a)






