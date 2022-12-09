import json


#with open('Rotter.json', 'r') as myfile:
 #   data=myfile.read()
#obj = json.loads(data)
#cityobject = obj['CityObjects']
#vertices = obj['vertices']

lst = [0,1,1,1]
lst.append("test")
lst.remove(1)

lijst4 = ["a","b","c"]

lst.insert(2,lijst4)

a = lst.count(1)

lst2 = [[0,1,1],[1,2,3],[4,5,6]]

lst3 = ["ali", "baba","forty", "thieves","maarten","jonathan","3BM"]


lst4 = []
for i in lst2:
    lst5 = []
    for j in i:
        lst5.append(lst3[j])
    lst4.append(lst5)

print(lst)


#print("transform: " + str(obj['transform']))


#print(cityobject)
#print(vertices)