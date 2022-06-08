from tkinter import*

x1, y1, x2, y2 = 0, 0, 0, 0

def paint(event):
    global x1, y1
    x1, y1 = (event.x), (event.y)
    
def paint2(event):
    x2, y2 = (event.x), (event.y)
    canvas.create_line(x1, y1, x2, y2, fill = "black")

window = Tk()
canvas = Canvas(window)
canvas.bind("<Button-1>", paint)
canvas.bind("<ButtonRelease-1>", paint2)
canvas.pack()
window.mainloop()