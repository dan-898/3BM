import json
import FreeCAD
import FreeCADGui

with open('C:/Users/danys/AppData/Roaming/FreeCAD/Macro/twocube.city.json', "r") as f:
    data = json.load(f)

doc = FreeCAD.newDocument()

dataCityObjects = data['CityObjects']
a = data['CityObjects']
b = data['transform']['scale']
c = data['transform']['translate']

objectNames = []
for i in dataCityObjects:
    objectNames.append(i)

lod = 0

for i in dataCityObjects[i]['geometry'][lod]['boundaries']:
    boundaries = []
    for j in i:
        for k in j:
            mesh = []
            for l in k:
                point = []

                pointNew = []
                for m, n, o in zip(data['vertices'][l], b, c):
                    pointNew.append(m / n + float(o))
                point.append(pointNew)
                mesh.append(point)
            boundaries.append(mesh)

        solid = doc.addObject("Part::Extrusion", "CityObjects")
        solid.Base = boundaries
        solid.Dir = (0, 0, 100)
        solid.Solid = True

# Update the document
doc.recompute()

FreeCADGui.SendMsgToActiveView("ViewFit")
