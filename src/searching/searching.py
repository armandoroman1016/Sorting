# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while arr[low] != arr[high]:

    middle = (low + high) // 2

    if arr[middle] > target:
      high = middle

    elif arr[middle] < target:
      low = middle
    
    elif arr[middle] == target:
      return middle
  
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  # if range of elements is two consecutive elements 
  # and target element wasn't found or array is empty then return -1
  if len(arr) == 0 or high - low == 1:
    return -1 # array empty

  # if found return index of element
  if arr[middle] == target:
    return middle

  elif arr[middle] < target:
    return binary_search_recursive(arr, target, middle, high)
  
  else:
    return binary_search_recursive(arr, target, low, middle)

