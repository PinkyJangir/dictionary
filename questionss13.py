a = {'a':50,'b':58,'c': 56,'d':40,'e':100,'f':20}
m=0
b=0
for i in a:
    if a[i]>m:
        m=a[i]
        b=i
print(b,m)
s=0
for i in a:
    if a[i]!=m:
        if a[i]>s:
            s=a[i]
            b=i
print(b,s)
tm=0
for i in a:
    if a[i]!=m and a[i]!=s:
        if a[i]>tm:
            tm=a[i]
            b=i
print(b,tm)
