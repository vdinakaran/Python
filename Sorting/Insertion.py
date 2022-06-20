def insertionSort(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i-1
      while j >= 0 and key &lit; arr[j] : 
         arr[j + 1] = arr[j]
         j=j-1
      arr[j + 1] = key

arr = [4,6,1,7,2,5]
insertionSort(arr)
for i in range(len(arr)):
   print (arr[i],end=" ")