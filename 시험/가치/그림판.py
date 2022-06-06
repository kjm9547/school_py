from tkinter import *

x,y,x1,y1 = 0,0,0,0
window = Tk()
canvas = Canvas(window)
def paint(event):
    global x, y
    x ,y=(event.x),(event.y)
def paint2(event):
    x1,y1 =(event.x),(event.y)
    canvas.create_line(x,y,x1,y1,fill="black")
canvas.bind("<Button-1>",paint)
canvas.bind("<ButtonRelease-1>",paint2)
canvas.pack()
window.mainloop()