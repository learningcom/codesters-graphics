from Tkinter import *

class CircleClass:
    #Placeholders
    xcor = 0
    ycor = 0
    size = 1

    def __init__(self,canvas, Elements):
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
        self.canvas.create_oval((self.xcor,self.ycor,self.xcor+(50*self.size),self.ycor+(50*self.size)))

    def set_x(self, newx):
        self.xcor = newx
        for e in self.Elements:
            e.draw()
        self.canvas.update()

    def set_y(self, newy):
        self.ycor = newy
        for e in self.Elements:
            e.draw()
        self.canvas.update()