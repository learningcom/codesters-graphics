from Tkinter import *
import math

class SpriteClass:
    #Default values
    xcor = 0
    ycor = 0
    speed = 1
    size = 50
    color = 'white'
    heading = 0

    def __init__(self,canvas, Elements):
        self.canvas = canvas
        self.Elements = Elements
        for e in self.Elements:
            e.draw()
        self.canvas.update()

    def draw(self):
        self.canvas.create_oval((self.xcor-(self.size/2),self.ycor-(self.size/2),self.xcor+(self.size/2),self.ycor+(self.size/2)), fill=self.color)

    #Set variables
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
    def set_speed(self, newspeed):
        self.speed = newspeed
        for e in self.Elements:
            e.draw()
        self.canvas.update()
    def set_size(self, newsize):
        self.size = 50 * newsize
        for e in self.Elements:
            e.draw()
        self.canvas.update()
    def set_color(self, newcolor):
        self.color = newcolor
        for e in self.Elements:
            e.draw()
        self.canvas.update()
    def set_heading(self, degrees):
        self.heading = degrees * math.pi * 2 / 360

    #Basic motion
    def move_forward(self, amount):
        self.set_x(self.xcor + amount*math.cos(self.heading))
        self.set_y(self.ycor + amount*math.sin(self.heading))
    def move_backward(self, amount):
        self.set_x(self.xcor - amount*math.cos(self.heading))
        self.set_y(self.ycor - amount*math.sin(self.heading))
    def move_left(self, amount):
        self.set_x(self.xcor - amount)
    def move_right(self, amount):
        self.set_x(self.xcor + amount)
    def move_up(self, amount):
        self.set_y(self.ycor - amount)
    def move_down(self, amount):
        self.set_y(self.ycor + amount)

    #More complex motion
    def glide_to(self, newx, newy):
        xdist = newx - self.xcor
        ydist = newy - self.ycor
        dist = math.sqrt(xdist**2 + ydist**2)
        tempheading = self.heading
        self.heading = math.atan(ydist/xdist)

        print xdist * ydist
        print self.heading

        #Trig stuff
        while dist > self.speed:
            if xdist > 0:
                self.set_x(self.xcor + self.speed*math.cos(self.heading))
            else:
                self.set_x(self.xcor - self.speed*math.cos(self.heading))
            if ydist > 0:
                self.set_y(self.ycor + self.speed*math.sin(self.heading))
            else:
                self.set_y(self.ycor - self.speed*math.sin(self.heading))
            xdist = newx - self.xcor
            ydist = newy - self.ycor
            dist = math.sqrt(xdist**2 + ydist**2)

        self.set_x(newx)
        self.set_y(newy)
        self.heading = tempheading
        for e in self.Elements:
            e.draw()
        self.canvas.update()