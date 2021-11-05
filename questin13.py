dict = {'a':50,'b':50,'c':50,'d':40, 'e':100,'f':20}
max=0
smax=0
thmax=0
l=[]
for i in dict:
    if dict[i]>max:
        max=dict[i]
        max_key=i
for j in dict:
    if dict[j]<max:
        if dict[j]>smax:
            smax=dict[j]
            smax_key=j
for k in dict:
    if dict[k]<max:
        if dict[k]<smax:
            if dict[k]> thmax:
                thmax=dict[k]
                thmax_key=k
l.append(max_key)
l.append(max)
l.append(smax_key)
l.append(smax)
l.append(thmax_key)
l.append(thmax)
print(l)