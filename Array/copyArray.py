from numpy import *
arr1=array([1,3,4,5])
arr2= [None] * len(arr1); 
for i in range(len(arr1)):
    arr2[i]=arr1[i]
print(arr2)