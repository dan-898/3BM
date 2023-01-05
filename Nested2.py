# import pprint
#
# lst2 = [[0, 1, 1], [1, 2, 3], [4, 5, 6]]
# lst2.pop(1)
# lst3 = ["ali", "baba", "forty", "thieves", "maarten", "jonathan", "3BM"]
#
# lst4 = []
# for i in lst2:
#     lst5 = []
#     for j in i:
#         lst5.append(lst3[j])
#     lst4.append(lst5)
#
# pprint.pprint(lst4)


import pprint

lst10 = [[[0, 1, 1], [1, 2, 3], [4, 5, 6]], [[0, 2, 3], [4, 4, 3], [3, 2, 5]]]
lst11 = ["ali", "baba", "forty", "thieves", "maarten", "jonathan", "3BM"]

# lst12 = []

for i in lst10:
    for j in i:
        lst12 = [j]

        for k in i:
            lst13 = []
            lst13.append(lst11)




print(lst13)





# pprint.pprint(lst12)

