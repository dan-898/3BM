
lst = [0,1,1,1]
lstemp = [0,1,1,1]

lstemp.append("test")

lst.append("test")

lst.remove(1)

lijst4 = ["a", "b", "c"]

lst.insert(2,lijst4)

a = lst.count(1)

lst2 = [[0, 1, 1], [1, 2, 3], [4, 5, 6]]
lst2.pop(1)
lst3 = ["ali", "baba", "forty", "thieves", "maarten", "jonathan", "3BM"]


b = lst3[2]

lst4 = []
for i in lst2:
    lst5 = []
    for j in i:
        lst5.append(lst3[j])
    lst4.append(lst5)


print(lst4)