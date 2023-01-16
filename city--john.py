import json

with open('twocube.city.json', "r") as f:
    data = json.load(f)
    dataCityObjects = data['CityObjects']
a = data['CityObjects']['onebuilding']['geometry'][0]['boundaries']
scale = data['transform']['scale']

# print(scale[0])

objectNames = []
for i in dataCityObjects:
    objectNames.append(i)

lod = 0  # 0=1, 1=2

for i in dataCityObjects[i]['geometry'][lod]['boundaries']:

    for j in i: #in the boundaries
        boundaries = []
        for k in j: #nodenumber of the mesh
            mesh = []
            for num, l in enumerate(k):
                point = []
                point.append(data['vertices'][l])
                mesh.append(point)
            boundaries.append(mesh)


motherlist = []
for x in boundaries[0]:
    elementlist = x[0]
    templist = []
    for num, element in enumerate(elementlist):
        output = element * scale[num]

        templist.append(output)
    motherlist.append([templist])
print([motherlist])
print(boundaries)

# for x in range(0,10):
    # print(x)

list = [2,4,5,6]

for index, x in enumerate(list):
    print(f"index: {index}, value: {x}")