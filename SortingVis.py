#imports
from tkinter import *
from tkinter import ttk
import random
from SortingAlgorithms.BubbleSort import bubblesort

from numpy import c_

#tkinter configuration
root = Tk()
root.title('Sorting Visualiser')
root.maxsize(900, 600)
#background colour = lightblue
root.config(bg='#c8d8e4')

#Variable
selected_algo = StringVar()
data = []

#creates rectangle for grid
def drawData(data):
    canvas.delete('all')
    c_height = 380
    c_width = 600
    x_width = c_width/ (len(data) + 1)
    offset = 30
    spacing = 10
    normalisedData = [i / max(data) for i in data]

    for i, height in enumerate(normalisedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i+1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill = '#dd7973')
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

#Gets algo value submitted by user
def Generate():
    global data
    #if no values inputted hard values takeover
    try:
        minValue = int(minEntry.get())
    except:
        minValue=1
    
    try:
        maxValue = int(maxEntry.get())
    except:
        maxValue=100

    try:
        size = int(sizeEntry.get())
    except:
        size = 10

    #if values inconsistent will swap to different values
    if minValue < 0 : minValue = 0
    if maxValue > 100 : maxValue = 100
    if size > 30 or size < 3: size = 20
    if minValue > maxValue : minValue, maxValue = maxValue, minValue
    
    data = []

    for i in range(size):
        data.append(random.randrange(minValue, maxValue+1))
    drawData(data)

def Start():
    global data
    bubblesort(data, drawData)
    


#UI frame
UI_frame = Frame(root, width=600, height=380, bg='#52ab98')
UI_frame.grid(row=0, column=0, padx=10, pady=5)


#changed width to see all bars
canvas = Canvas(root, width=650, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
Label(UI_frame, text="Algorithm: ", bg='#52ab98').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algoMenu = ttk.Combobox(UI_frame, textvariable=selected_algo, values=['Bubble Sort','Merge Sort','Quick Sort'])
algoMenu.grid(row=0,column=1, padx=5, pady=5)
algoMenu.current(0)

Speed = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label= "Speed:")
Speed.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text='Start', command= Start, bg = '#dd7973').grid(row=0, column=3, padx=5, pady=5)


sizeEntry = Scale(UI_frame, from_=3, to=30, length=200, resolution=1, orient=HORIZONTAL, label= "Data Size:")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, length=200, resolution=1, orient=HORIZONTAL, label= "Min Value:")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, length=200, resolution=1, orient=HORIZONTAL, label= "Max Value:")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text='Generate', command= Generate, bg = '#dd7973').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()