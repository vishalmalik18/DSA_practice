def find_small(n,arr):
 value = arr[0]
 for i in range(n):
  if arr[i]<value:
   value = arr[i]
 return value 
