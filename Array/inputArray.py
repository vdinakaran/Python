from array import *
arr=array('i',[])
num=int(input("enter the number"))
for i in range(num):
    x=int(input("number:"))
    arr.append(x)
print(arr)
for j in range(len(arr)):
    print(arr[j])