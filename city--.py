import json

with open('twocube.city.json', "r") as f:
    data = json.load(f)
    dataCityObjects = data['CityObjects']
a = data['CityObjects']['onebuilding']['geometry'][0]['boundaries']

objectNames = []
for i in dataCityObjects:
    objectNames.append(i)

lod = 0  # 0=1, 1=2

for i in dataCityObjects[i]['geometry'][lod]['boundaries']:
    for j in i: #in the boundaries
        boundaries = []
        for k in j: #nodenumber of the mesh
            mesh = []
            for l in k:
                point = []
                point.append(data['vertices'][l])
                mesh.append(point)
            boundaries.append(mesh)
#

print(boundaries)
