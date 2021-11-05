#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 2.****************
# a="w3resource"
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 3****************************
# d=int(input("enter the number"))
# b={}
# for i in range(1,d+1):
#     b[i]=d=i**2
# print(b)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# for i in d:
#     for j in d:
#         if d[i]>d[j]:
#             d[i],d[j]=d[j],d[i]
# print(d)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# 6.
# p={0: 10, 1: 20}
# p[2]=30
# print(p)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#7.
# d1={1:10, 2:20}
# d2={3:30, 4:40}
# d3={5:50,6:60}
# d4={}
# for i in (d1,d2,d3):
#     d4.update(i)
# print(d4)

#8
# d={"name":"pinky","surename":"jangid"}
# num=input("enter the number")
# if num in d.values():
#     print("yes")
# else:
#     print("no")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#9
# d={1:"pinky",2:"jangir",3:"rajptiya"}
# for i in d:
    # print(d[i])



#11.

# d={1:"pinky"}
# e={2:"jangir"}
# f={}
# for i in (d,e):
#     f.update(i)
# print(f)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#14
# p={1: 10, 2: 20}
# m=1
# for i in p:
#     m=m*p[i]
# print(m)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 15
# p={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# p.pop(1)
# print(p)

#16 
# l=["blue","black","green","orange"]
# s=[1,2,3,4]
# b={}
# for i in l:
#     for j in s:
#         b[i]=j
#         s.remove(j)
#         break

# print(b)



#17
# d={1:59,8:50,2:5,4:43,5:35,6:53,3:354}
# for i in d:
#     for j in d:
#         if d[i] < d[j]:
#             d[i],d[j]=d[j],d[i]
# print(d)

# d={1:59,8:50,2:5,4:43,5:35,6:53,3:354}
# #18=
# l=[5,2,6,34,65,7]
# smallist=l[0]
# for i in l:
#     if i<=smallist:
#         s=i
# print("smallest",s)
# print(max)

# 20
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3=dict(d1)
# d3.update(d2)
# for i ,j in d1.items():
#     for x,y in d2.items():
#             if i==x:
#                 d3[i]=(j+y)
# print(d3)


# 21
# l=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# b=[]
# i=0
# while i <len(l):
#     for j in l[i]:
#         if l[i][j] not in b:
#             b.append(l[i][j])
#         i+=1
# print(b)

# 32
# num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# c=0
# for i,j in num.items():
#     c+=1
#     print(i,j,c)


# # 37
# # d={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# # num=int(input("enter the number"))
# # for i in d:
# #     j=0
# #     while j<len(d[i]):
# #         j+=1
# #     print(d[i][num-1])

# s=["S001","S002","S003","S004"]
# a=["Adina park","Leyton marsh","Duncan Boyle","Saim Richard"]
# c=[85,98,89,92]
# i=0
# dic={}
# p=[]
# while i<len(s):
#     d={}
#     d[a[i]]=c[i]
#     dic[s[i]]=d
#     i=i+1
# p.append(dic)
# print(p)

# 42
# d={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# num=int(input("enter the number"))
# for i in d:
#     if d[i]==num:
#         print(True)
#     else:
#         print(False)
#     break

# d={"pinky": 1, "preeti": 2, "geetu": 3, "sapna": 4}
# b={}
# for i,j in d.items():
#         b[j]=[i]
# print(b)



# 43
# d=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# b={}
# p=[]
# t=[]
# s=[]
# for k,v in d:
#     if k=="yellow":
#         p.append(v)
#         b[k]=p
#     elif k=="blue":
#         t.append(v)
#         b[k]=t
#     elif k=="red":
#         s.append(v)
#         b[k]=s
# print(b)

# 44@@@@@@@@@@@@@@@@@@@@@@@22222222



d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
p={}
q={}
r={}
s={}
t=[]
for i in d:
    p[i]=d[i][0]
    q[i]=d[i][1]
    r[i]=d[i][2]
    s[i]=d[i][3]
    t.append(p)
    t.append(q)
    t.append(r)
    t.append(s)  
print(t)

# 45

# d=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# d.pop(0)
# print(d)

# 47
# d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# p={}
# for i ,j in d.items():
#     p[i]=d[i]
#     j.clear()
# print(p)

# 48
# d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b={}
# for i,j in d.items():
#     b[j]=(len(j))
# print(b)
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}

# 49
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# for i in  num:
#     print(i)


# 50
# d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b=[]
# for i in d.items():
#     b.append(list(i))
# print(b)

# 51 wrong
# d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for i,j in d.items():
#     if d%2!=0:
#         j.remove()
#     e
# print(d)



#{((((w3resource))))))}
# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for color_key, value in d.items():
#      print(color_key, 'corresponds to ', d[color_key])

# myDict = {'a':1,'b':2,'c':3,'d':4}
# print(myDict)
# if 'a' in myDict: 
#     del myDict['a']
# print(myDict)

# my_dict = {'x':500, 'y':5874, 'z': 560}

# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

# print('Maximum Value: ',my_dict[key_max])
# print('Minimum Value: ',my_dict[key_min])


