# #Merge sort algorithms

# import time

# def mergesort(data, drawData, timescale):
#   if len(data)>1:
#     left_array = data[:len(data)//2]
#     right_array = data[len(data)//2:]

#     #Recursion
#     mergesort(left_array, drawData, timescale)
#     mergesort(right_array, drawData, timescale)

#     # merge
#     #index of left most element in left and right array
#     i=0
#     j=0
#     #keeps track of index in merged array
#     k = 0
    
#     while i < len(left_array) and j < len(right_array):
#       if left_array[i] < right_array[j]:
#         data[k] =  left_array[i]
#         i += 1
#       else:
#         data[k] = right_array[j]
#         j += 1
#       k += 1

#     while i < len(left_array):
#       data[k] = left_array[i]
#       i += 1
#       k += 1

#     while j < len(right_array):
#       data[k] = right_array[j]
#       j += 1
#       k += 1

#     #drawData(data)
#     #time.sleep(0.2)
import time


def mergesort(data, drawData, timescale):
  mergesort_algo(data,0,len(data)-1, drawData, timescale)

def mergesort_algo(data, left, right, drawData, timescale):
  if left < right:
    middle_val = (left+right)//2
    #recursion
    mergesort_algo(data,left,middle_val, drawData,timescale)
    mergesort_algo(data,left,middle_val+1, drawData,timescale)
    merge(data, left, middle_val, right, drawData, timescale)

def merge(data, left, middle_val, right, drawData, timescale):
  drawData(data, getColourArray(len(data), left, middle_val, right))
  time.sleep(timescale)

  #dividing data set
  leftdata = data[left:middle_val+1]
  rightdata = data[middle_val+1: right+1]

  leftindex = 0
  rightindex = 0

  for x in range (left, right+1):
    if leftindex< len(leftdata) and rightindex < len(rightdata):
      if leftdata[leftindex] <= rightdata[rightindex]:
        data[x] = leftdata[leftindex]
        leftindex += 1
      else:
        data[x] = rightdata[rightindex]
        rightindex += 1

    elif leftindex < len(leftdata):
      data[x] = leftdata[leftindex]
      leftindex += 1

    else:
      data[x] = rightdata[rightindex]
      rightindex += 1

  drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
  time.sleep(timescale)

def getColourArray(length, left, middle_val,right):
  colourArray = []

  for i in range(length):
    if i >= left and i <= right:
      if i >= left and i <= middle_val:
        colourArray.append("yellow")
      else:
        colourArray("purple")
    else:
      colourArray.append("white")

  return colourArray