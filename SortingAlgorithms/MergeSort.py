#Merge sort algorithms

import time

def mergesort(data, drawData):
  if len(data)>1:
    left_array = data[:len(data)//2]
    right_array = data[len(data)//2:]

    #Recursion
    mergesort(left_array)
    mergesort(right_array)

    # merge
    #index of left most element in left and right array
    i=0
    j=0
    #keeps track of index in merged array
    k = 0
    
    while i < len(left_array) and j < len(right_array):
      if left_array[i] < right_array[j]:
        data[k] =  left_array[i]
        i += 1
      else:
        data[k] = right_array[j]
        j += 1
      k += 1

    while i < len(left_array):
      data[k] = left_array[i]
      i += 1
      k += 1

    while j < len(right_array):
      data[k] = right_array[j]
      j += 1
      k += 1

    drawData(data)
    time.sleep(0.2)