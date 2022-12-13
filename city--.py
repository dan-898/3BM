import json

with open('Rotter.json', "r") as f:
    data = json.load(f)

a = data['transform']['scale']
b = data['transform']['translate']


for i in a, b:
    lst1=[]
    lst1.append(a)
    lst1.append(b)


print(i)
