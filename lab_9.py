from tkinter import *
from PIL import Image, ImageDraw
from tkinter import colorchooser

def draw (event):
    x1, y1 = (event.x - BrushSize), (event.y - BrushSize)
    x2, y2 = (event.x + BrushSize), (event.y + BrushSize)
    canvas.create_oval(x1, y1, x2, y2, fill=color, width=0)
def chooseColor():
    global color
    (rgb, hx) = colorchooser.askcolor()
    color = hx
    color_lab['bg'] = hx
def select(value):
    global BrushSize
    BrushSize = int(value)

x = 0
y = 0

TheWindow = Tk()
TheWindow.title = 'Paint'
TheWindow.geometry('1280x720')
TheWindow.resizable(0,0)

BrushSize = 10
color = 'black'

TheWindow.columnconfigure(7, weight=1)
TheWindow.rowconfigure(3, weight=1)

canvas = Canvas (TheWindow, bg='white')
canvas.grid(row = 3, column = 0, columnspan = 12, padx = 5, pady = 5, sticky = E + W + S + N)

canvas.bind('<B1-Motion>', draw)

Menu = Menu(tearoff=0)

TheImage = Image.new('RGB',(1280,640),'white')
draw_img = ImageDraw.Draw(TheImage)
Button(TheWindow, text='Выбрать цвет:', width=11,command= chooseColor).grid(row=0,column=1,padx=6)

color_lab = Label(TheWindow,bg=color,width=10)
color_lab.grid(row=0,column = 2, padx = 6)

v = IntVar(value=10)
Scale(TheWindow, variable=v, from_=1, to=100, orient=HORIZONTAL, command=select).grid(row=0,column = 3, padx = 6)

TheWindow.mainloop()
