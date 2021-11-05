l="MISSISSIPPI"
# l=list(str)list
b={}
for i in l:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
