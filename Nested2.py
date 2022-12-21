lst2 = [[[0, 1, 1], [1, 2, 3], [4, 5, 6]], [[0, 2, 3], [4, 4, 3], [3, 2, 5]]]

lst3 = ["ali", "baba", "forty", "thieves", "maarten", "jonathan", "3BM"]

lst4 = []

for i in lst2:
    lst5 = []

    for j in i:
        lst6 = []

        for k in j:
            lst6.append(lst3[k])

        lst5.append(lst6)
        lst4.append(lst6)
print(lst4)
