list=[{"first":"1"}, {"second": "2"},{"third": "1"},{"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
b=[]
i=0
while i<len(list):
     for j in list[i]:
          if list[i][j] not in b:
                    b.append(list[i][j])
          i+=1
print(b)