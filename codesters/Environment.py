from Tkinter import *

class StageClass:
    #Placeholders
    xcor = 0
    ycor = 0
    size = 1

    def __init__(self, canvas, Elements):
        #Placeholders
        xcor = 0
        ycor = 0
        size = 1
        self.canvas = canvas
        self.Elements = Elements
        for e in self.Elements:
            e.draw()
        self.canvas.update()

    def draw(self):
        self.canvas.create_rectangle((0,0,500,500), fill='white')
