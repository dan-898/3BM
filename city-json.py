import json
import pprint
with open('twocube.city.json', 'r') as city:
    data = city.read()
    file = json.loads(data)
    vertices = file[ 'CityObjects']




    pprint.pprint(vertices)
