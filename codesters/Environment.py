from Tkinter import *

class Stage:
    #Placeholders
    xcor = 0
    ycor = 0
    size = 1

    def __init__(self, canvas):
        #Placeholders
        xcor = 0
        ycor = 0
        size = 1
        self.canvas = canvas

    def draw(self):
        self.canvas.create_rectangle((0,0,500,500), fill='white')
