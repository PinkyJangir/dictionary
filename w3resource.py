# 1
# a={0: 10, 1: 20}
# a[2]=30
# print(a)

# 2
# d1={1:10, 2:20}
# d2={3:30, 4:40}
# d3={5:50,6:60}
# d4={}
# for i in (d1,d2,d3):
#     d4.update(i)
# print(d4)

# 3.
# a={1:"pinky",2:"jangir"}
# name=input("enter the nuber")
# if name in a.values():
#     print("yes")
# else:
#     print("no")


a={1:"pinky",2:"jangir",3:"komal"}
b={1,2,3,}
p=dict(zip(a,b))
print(p)
