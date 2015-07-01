from Tkinter import *

class Circle:
    #Placeholders
    xcor = 0
    ycor = 0
    size = 1

    def __init__(self,canvas):
        #Placeholders
        xcor = 0
        ycor = 0
        size = 1
        self.canvas = canvas
        #self.canvas.create_oval((xcor,ycor,xcor+(50*size),ycor+(50*size)))

    def draw(self):
        self.canvas.create_oval((self.xcor,self.ycor,self.xcor+(50*self.size),self.ycor+(50*self.size)))

    def set_x(self, newx):
        self.xcor = newx
        #self.draw()

    def set_y(self, newy):
        self.ycor = newy
        #self.draw()