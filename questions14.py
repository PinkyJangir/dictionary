d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in d:
    for j in d:
        if d[i] < d[j]:
            d[i],d[j]=d[j],d[i]
print(d)
for i in d:
    for j in d:
        if d[i]>d[j]:
            d[i],d[j]=d[j],d[i]
print(d)

