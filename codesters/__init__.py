from Tkinter import *
from Environment import *
from Circle import *

root = Tk()

#Setting up canvas
canvas = Canvas(root, width=500, height=500)
canvas.pack()

#Making a palceholder stage for now
stage = Stage(canvas)
stage.draw()

#root.mainloop()