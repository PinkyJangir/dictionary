# a="pinky"
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)


b={}
for i in range(0,5):
    name=input("enter the number")
    for i in range(name):
        if i in b:
            b[i]+=1
        else:
            b[i]=1
print(b)