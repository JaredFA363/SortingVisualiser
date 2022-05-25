#Quick sort algorithms

import time

def partition(data,zero,sizeofarray):

  #choose righmost elememnt as pivot
  pivot = data[sizeofarray]

  #pointer for gretater element
  i = zero - 1

  #compares each element with pivot
  for j in range(zero,sizeofarray):
    if data[j] <= pivot:
      #if element smaller than pivot swap t with greaetr element
      i = i + 1

      #swapping element at i with element at j
      (data[i], data[j]) = (data[j], data[i])

      #swap pivot element with greater element specified by i
  (data[i + 1], data[sizeofarray]) = (data[sizeofarray], data[i + 1])

  return i + 1

def quickSort(data, zero, sizeofarray, drawData):
  if zero < sizeofarray:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pivot = partition(data, zero, sizeofarray)

    # recursive call on the left of pivot
    quickSort(data, zero, pivot - 1)

    # recursive call on the right of pivot
    quickSort(data, pivot + 1, sizeofarray) 

    drawData(data)
    time.sleep(0.2) 