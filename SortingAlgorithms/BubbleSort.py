#Bubble sort algorithms

import time


def bubblesort(data, drawData, timescale):

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

                #green if data is swapped correctly
                drawData(data, ['green' if y == x or y == x+1 else '#dd7973' for y  in range(len(data))])
                time.sleep(timescale)
    drawData(data, ['green' for x in range(len(data))])
