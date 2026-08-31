def count_negative_number(n,arr):
  count = 0
  for i in range(n,arr):
    if arr[i]<0:
      count +=1
  return count

