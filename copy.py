# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# mydict=classes.copy()
# print(mydict)
#{'room2': '7th', 'room3': '8th', 'room1': '6th'}
# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# mydict=classes.copy()
# print(mydict)


a={1:"one",2:"two",3:"three"}
b={4:"four",5:"five",6:"six"}
c={}
for i in a.keys():
    for j in b:
        c[i]=b[j]
        b.pop(j)
        break
print(c)



