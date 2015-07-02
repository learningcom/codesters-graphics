from Tkinter import *
from Environment import *
from Circle import *
from Sprite import *

root = Tk()

#A list of whatever exists at this time.
Elements = []

#Setting up canvas
canvas = Canvas(root, width=500, height=500)
canvas.pack()


#This allows the user to call codesters.Sprite() and so on, and it creates the relevant sprite WITH canvas through here.
#All things made here are added to Elements
def Stage():
    Elements.append(StageClass(canvas, Elements))
    return Elements[-1]
def Circle():
    Elements.append(CircleClass(canvas, Elements))
    return Elements[-1]
def Sprite():
    Elements.append(SpriteClass(canvas, Elements))
    return Elements[-1]

#In each class declaration, this must happen:
#        self.canvas = canvas
#        self.Elements = Elements

#In each method for these classes that causes something visible to change, these three lines must happen:
#
#        for e in self.Elements:
#            e.draw()
#        self.canvas.update()

#root.mainloop()