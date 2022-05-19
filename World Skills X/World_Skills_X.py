from tkinter import * 
from PIL import ImageTk, Image
import numpy as np
import time
from threading import Thread 
from TLMode import*

from Timer import Timer

def endTrue():
    global t
    send_process = Thread(target=begin)
    send_process.start()
    flag = False

t = Timer()

#import os
#print (os.getcwd())

def start():
    button.state(['pressed', 'disabled'])
    style.configure(SUNKABLE_BUTTON, relief=tk.SUNKEN, foreground='green')

def stop():
    button.state(['!pressed', '!disabled'])
    style.configure(SUNKABLE_BUTTON, relief=tk.RAISED, foreground='red')

def dump():
    selobj = Frame(window, width = 3, height = 3)

    
    img_label_block = Button(selobj, image = img_block)
    img_label_block.pack()


    
    img_label_Pedestrian = Button(selobj, image = img_Pedestrain)
    img_label_Pedestrian.pack()


    
    img_label_Zhorizontal = Button(selobj, image = img_Zhorizontal)
    img_label_Zhorizontal.pack()


    
    img_label_TLgreen = Button(selobj, image = img_TLgreen)
    img_label_TLgreen.pack()

    selobj.pack()
    selobj.place(anchor = E, relx = 1, rely = 0.2)

def cellCoordinate(x, y):
    print(x, " ", y)

window = Tk()
window.title("World Skills X")
window.iconbitmap(r'C:/Users/zhitlo/Source/Repos/World Skills X/World Skills X/Resources/icon.ico')
window.geometry("1200x700")


##### road from blocks
img_road = ImageTk.PhotoImage(Image.open("Resources/road.png"))
for r in range (20):
    for c in range (20):
        road = Frame(window)
        road.grid(row = r, column = c, ipadx=35, ipady = 35, padx = 0, pady = 0)
        road.place(relx = 0, rely = 0.5)
road.pack()
road_png = Label(road, image = img_road)
road_png.pack()


img_block = ImageTk.PhotoImage(Image.open("Resources/block.png"))
img_Zhorizontal = ImageTk.PhotoImage(Image.open("Resources/Zhorizontal.png"))
img_Pedestrain = ImageTk.PhotoImage(Image.open("Resources/Pedestrain.png"))
img_TLgreen = ImageTk.PhotoImage(Image.open("Resources/TLgreen.png"))


selobj = Frame(window, width = 35, height = 35)

img_TLgreen = ImageTk.PhotoImage(Image.open("Resources/TLgreen.png"))
img_label_TLgreen = Button(selobj, image = img_TLgreen)
img_label_TLgreen.pack()
img_label_TLgreen.place(anchor = NE, relx = 1, rely = 1)
selobj.place(anchor = NE, relx = 1, rely = 1)
##### coordinates

#CurrentMode = "No mode selected"

Edit = Button(window, text = "Edit", command = dump)
Edit.place(relx = 0.85, rely = 0.3)

TimeMode = Button(window, text = "Time mode", command = lambda: Thread(target=TLTimeMode).start())
TimeMode.place(relx = 0.85, rely = 0.4)

#TLTimeMode(isClicked)

TransportMode = Button(window, text = "Transport mode", command = lambda: Thread(target=TLTransportMode).start())
TransportMode.place(relx = 0.85, rely = 0.5)

TraficLightsMode = Label(window, text=("Current mode: "))
TraficLightsMode.place(relx = 0.85, rely = 0.6)
#Mode.set(CurrentMode)

TestSample = Button(window, text = "Test sample")
TestSample.place(relx = 0.85, rely = 0.7)

TestRandom = Button(window, text = "Test random")
TestRandom.place(relx = 0.85, rely = 0.8)

StartTrain = Button(window, text = "Start training", command =lambda: t.start())
StartTrain.place(relx = 0.85, rely = 0.87)

EndTrain = Button(window, text = "End training", command =lambda: t.stop())
EndTrain.place(relx = 0.85, rely = 0.92)

w = Scale(window, from_=0, to=200)
w.pack()
w.place (relx = 0.8, rely = 0.8)



AIInterface = Frame(window)
IterNum = Label(AIInterface, text = "Iteration № ")
IterNum.grid(row = 0, column = 0)
IterCurrentTimer = Label(AIInterface, text = "Current time: ")
IterCurrentTimer.grid(row = 1, column = 0)
IterBestTime = Label(AIInterface, text = "Best time: ")
IterBestTime.grid(row = 2, column = 0)
AIInterface.pack()
AIInterface.place(relx = 0.05, rely = 0.2)

window.mainloop()
