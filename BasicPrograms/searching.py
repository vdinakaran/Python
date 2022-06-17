list=[4,3,8,5,9]
flag=0
for x in range(0,5):
    if list[x]==10:
        flag=1

if flag==1:
    print("value found")
else:
    print("value not found")