from numpy import *
arr1=array([1,2,3,3])
for i in range(len(arr1)-1):
     if arr1[i]==arr1[i+1]:
         print(arr1[i])
