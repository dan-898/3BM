import json

with open('twocube.city.json', "r") as f:
    data = json.load(f)
    dataCityObjects = data['CityObjects']
a = data['CityObjects']['onebuilding']['geometry'][0]['boundaries']
b = data['transform']['scale']
c = data['transform']['translate']

objectNames = []
for i in dataCityObjects:
    objectNames.append(i)

lod = 0  # 0=1, 1=2

meshList = []
for i in dataCityObjects[i]['geometry'][lod]['boundaries']:
    boundaries = []
    for j in i:  # in the boundarie
        for k in j:  # nodenumber of the mesh
            mesh = []
            for l in k:
                point = []
                #point.append(data['vertices'][l])
                pointNew = []
                for m,n,o in zip(data['vertices'][l], b, c):
                    pointNew.append(m/n+float(o)) #of keer
                point.append(pointNew)
                mesh.append(point)
            boundaries.append(mesh)

print(boundaries)

