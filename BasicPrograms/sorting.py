num=[1,3,2,7,6]
for x in range(0,5):
    for y in range(x+1,5):
        if num[x]>num[x+1]:
            temp=num[x]
            num[x]=num[x+1]
            num[x+1]=temp


print(num)