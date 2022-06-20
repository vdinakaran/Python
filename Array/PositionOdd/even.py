from numpy import *
arr1=[8,2,3,4,45,6]
print("Even position numbers:")
for i in range(1,6,2):
   print(arr1[i])
print("Odd position numbers:")
for j in range(0,6,2): #6 will be 5
    print(arr1[j])

#largest element
arr1.sort()
print(arr1[len(arr1)-1])

#NUMBER OF ELEMENTS
print("number of elements")
print(len(arr1))

#SUM OF ELEMENTS
sum=0
for ele in range(len(arr1)):
    sum=sum+arr1[ele]
print(sum)

#descending order
arr1.reverse()
print(arr1)