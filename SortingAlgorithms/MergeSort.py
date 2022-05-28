#Merge Sort Algorithm

import time

def mergesort(data, drawData, timescale):
    mergesort_algo(data,0, len(data)-1, drawData, timescale)


def mergesort_algo(data, left, right, drawData, timescale):
    if left < right:
        middle = (left + right) // 2
        #recursion
        mergesort_algo(data, left, middle, drawData, timescale)
        mergesort_algo(data, middle+1, right, drawData, timescale)
        merge(data, left, middle, right, drawData, timescale)

def merge(data, left, middle_val, right, drawData, timescale):
    drawData(data, getColourArray(len(data), left, middle_val, right))
    time.sleep(timescale)

    #dividing data set
    leftData = data[left:middle_val+1]
    rightData = data[middle_val+1: right+1]

    leftIndex = 0
    rightIndex = 0

    # data index in main array
    for dataIndex in range(left, right+1):
      #checking if both indicies are in bound
        if leftIndex < len(leftData) and rightIndex < len(rightData):
            if leftData[leftIndex] <= rightData[rightIndex]:
                data[dataIndex] = leftData[leftIndex]
                #pointer to right
                leftIndex += 1
            else:
                data[dataIndex] = rightData[rightIndex]
                rightIndex += 1
        
        elif leftIndex < len(leftData):
            data[dataIndex] = leftData[leftIndex]
            leftIndex += 1
        else:
            data[dataIndex] = rightData[rightIndex]
            rightIndex += 1
    
    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timescale)

def getColourArray(lenght, left, middle_val, right):
    colourArray = []

    for i in range(lenght):
        if i >= left and i <= right:
            if i >= left and i <= middle_val:
                colourArray.append("yellow")
            else:
                colourArray.append("purple")
        else:
            colourArray.append("white")

    return colourArray