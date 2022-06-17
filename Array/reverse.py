from numpy import *
arr1=array([3,4,5,6])
arr2=[None]*len(arr1)
j=0
print(len(arr1))
for i in range(len(arr1)-1,-1,-1):
    arr2[j]=arr1[i]
    j=j+1
print(arr2)