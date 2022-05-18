from tkinter import * 
from PIL import ImageTk, Image

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

##### select object
"""
selobj = Frame(window, width = 3, height = 3)

img_block = ImageTk.PhotoImage(Image.open("Resources/block.png"))
img_label_block = Button(selobj, image = img_block)
img_label_block.pack()

img_HeavyBlock2 = ImageTk.PhotoImage(Image.open("Resources/HeavyBlock2.png"))
img_label_HeavyBlock2 = Button(selobj, image = img_HeavyBlock2)
img_label_HeavyBlock2.pack()

img_Pedestrain = ImageTk.PhotoImage(Image.open("Resources/Pedestrain.png"))
img_label_Pedestrian = Button(selobj, image = img_Pedestrain)
img_label_Pedestrian.pack()

img_VagonBlock = ImageTk.PhotoImage(Image.open("Resources/VagonBlock.png"))
img_label_VagonBlock = Button(selobj, image = img_VagonBlock)
img_label_VagonBlock.pack()

img_Zhorizontal = ImageTk.PhotoImage(Image.open("Resources/Zhorizontal.png"))
img_label_Zhorizontal = Button(selobj, image = img_Zhorizontal)
img_label_Zhorizontal.pack()

img_Zvertical = ImageTk.PhotoImage(Image.open("Resources/Zvertical.png"))
img_label_Zvertical = Button(selobj, image = img_Zvertical)
img_label_Zvertical.pack()

img_TLgreen = ImageTk.PhotoImage(Image.open("Resources/TLgreen.png"))
img_label_TLgreen = Button(selobj, image = img_TLgreen)
img_label_TLgreen.pack()


#selobj.grid(ipadx=35, ipady = 35, padx = 0, pady = 0)

selobj.pack()
selobj.place(anchor = E, relx = 1, rely = 0.2)
"""


##### coordinates

coords =Button(window, command = dump, text = "Test")
coords.place(relx = 0.85, rely = 0.5)
#cellCoordinate()

coords.place(relx = 0.85, rely = 0.5)

window.mainloop()

