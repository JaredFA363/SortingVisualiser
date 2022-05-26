#Quick sort algorithms

import time

def partition(data, start, end, drawData, timescale):

  #choose righmost elememnt as pivot
  pivot = data[end]
  border = start

  #pointer for gretater element
  i = start - 1

  drawData(data,getColourArray(len(data), start, end, border, border))
  time.sleep(timescale)

  #compares each element with pivot
  for j in range(start,end):
    if data[j] <= pivot:
      #if element smaller than pivot swap t with greaetr element
      i = i + 1

      drawData(data,getColourArray(len(data), start, end, border, j, True))
      time.sleep(timescale)

      #swapping element at i with element at j
      (data[i], data[j]) = (data[j], data[i])
      border +=1

    drawData(data,getColourArray(len(data), start, end, border, j))
    time.sleep(timescale)

      #swap pivot element with greater element specified by i
  drawData(data,getColourArray(len(data), start, end, border, end, True))
  time.sleep(timescale)
  (data[i + 1], data[end]) = (data[end], data[i + 1])

  #return i + 1,border
  return border

def quickSort(data, start, end, drawData, timescale):
  if start < end:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pivot = partition(data, start, end, drawData, timescale)

    # recursive call on the left of pivot
    quickSort(data, start, pivot - 1, drawData, timescale)

    # recursive call on the right of pivot
    quickSort(data, pivot + 1, end, drawData, timescale) 

#data = [8, 7, 2, 1, 0, 9, 6]

#size = len(data)

#quickSort(data, 0, size - 1, 0, 0)

#print(data)

def getColourArray(dataLength, start, end ,border, current, isSwapping = False):
  colourArray = []
  for i in range(dataLength):
    #base Colouring
    if i >= start and i <= end:
      #grey is partition we are working on
      colourArray.append('grey')
    else:
      #white partition we are not working on
      colourArray.append('white')

    if i == end:
      colourArray[i] = 'blue'
    elif i == border:
      colourArray[i] = 'red'
    elif i == current:
      colourArray[i] = 'yellow'

    if isSwapping:
      if i == border or i == current:
        colourArray[i] = 'green'

  return colourArray

      

