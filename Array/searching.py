arr=[4,7,3,9]
num=int(input("enter the number:"))
for i in range(len(arr)):
    if arr[i]==num:
        print("found")
        break
else:
    print("not found")