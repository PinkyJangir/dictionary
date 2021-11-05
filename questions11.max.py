dict = {'a':50,'b':50,'c':50,'d':40, 'e':100,'f':20}
max=0
smax=0
thmax=0
for i in dict:
    if dict[i]>max:
        max=dict[i]
for j in dict:
    if dict[j]<max:
        if dict[j]>smax:
            smax=dict[j]
for k in dict:
    if dict[k]<max:
        if dict[k]<smax:
            if dict[k]> thmax:
                thmax=dict[k]
print(max) 
print(smax)
print(thmax)              



    

    

# my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20,}
# max=0
# sec_max=0
# third_max=0
# l=[]
# for i in my_dict:
#     if my_dict[i]>max:
#         max=my_dict[i]
#         max_key=i
# #print(max)
# for j in my_dict:
#     if my_dict[j]<max:
#         if my_dict[j]>sec_max:
#             sec_max=my_dict[j]
#             sec_key=j
# #print(sec_max)
# for k in my_dict:
#     if my_dict[k]<max:
#         if my_dict[k]<sec_max:
#             if my_dict[k]>third_max:
#                 third_max=my_dict[k]
#                 third_key=k

# l.append(max_key)
# l.append(max)
# l.append(sec_key)
# l.append(sec_max)
# l.append(third_key)
# l.append(third_max)
# print(l)








#rint(max)