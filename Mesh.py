import json
import FreeCAD
import MeshPart

# Load the JSON file
with open("C:/Users/angza/Desktop/twocube.city.json", "r") as f:
    data = json.load(f)

# Extract the model data from the JSON file
model_data = data["CityObjects"]

# Create a new document in FreeCAD
doc = FreeCAD.newDocument()

# Create the model in FreeCAD
obj = doc.addObject("transform::scale", "CityObjects")
obj.Mesh = MeshPart.Mesh()

# Add the vertices to the mesh
for vertex in model_data["vertices"]:
    obj.Mesh.addVertex(vertex[0], vertex[1], vertex[2])

# Add the faces to the mesh
for face in model_data["faces"]:
    obj.Mesh.addFace(face)

# Update the document
doc.recompute()
