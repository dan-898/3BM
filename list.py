
#
# num = [ 0,1,2,4]
#
# names = ['jaja','karl','dodo']
#
#
# for i in (num+names):
#
#
#
#
#
#
#     print(i)




#
# name = input('enter name')
# age = input ('neter age')
#
#
# print(name + 'how are you ' + age)


import pprint

def ThreeD(Tara, Jony, Tala):
     lst1 = [[ ['love' == 'pain' for col in range(Tara)] for col in range(Jony)] for row in range(Tala)]
     lst2= [[ ['year' != 'to recovery' for col in range(Tara)] for col in range(Jony)] for row in range(Tala)]

     lst = lst1+lst2

     return lst
col1 = 3
col2 = 3
row = 3

pprint.pprint(ThreeD(col1, col2, row))

