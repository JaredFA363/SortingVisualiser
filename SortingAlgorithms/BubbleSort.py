#Bubble sort algorithms

import time

#def bubbleSort(data):
#    pass

def bubblesort(data, drawData):

    for i in range(len(data)):

    # loop compares array element
        for x in range(0, len(data) - i - 1):

      # compares the values next to each other
      # changes > to < to sort in descending order
            if data[x] > data[x+1]:

        #swapping elements if elements
        # are not in the intended order
                temp = data[x]
                data[x] = data[x+1]
                data[x+1] = temp

                drawData(data)
                time.sleep(0.2)


#array1 = [20,33,2,5,900]

#bubblesort(array1)
#print(array1)