from Tkinter import *
import math
import time

class SpriteClass:
    #Default values
    xcor = 0
    ycor = 0
    speed = 1
    size = 50
    color = 'white'
    heading = 0
    photo = PhotoImage(file = "./codesters/sprites/codestersLogo.gif")

    def __init__(self,canvas, Elements, image):
        self.heading = 0
        self.canvas = canvas
        self.Elements = Elements
        if image != '':
            self.photo = PhotoImage(file = "./codesters/sprites/"+image+".gif")
        for e in self.Elements:
            e.draw()
        self.canvas.update()

    def draw(self):
        if self.photo != None:
            self.canvas.create_image((self.xcor,self.ycor), image = self.photo)
        else:
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
    #Step functions to build other functions
    def step_forward(self):
        self.set_x(self.xcor + self.speed*math.cos(self.heading))
        self.set_y(self.ycor + self.speed*math.sin(self.heading))
    def step_backward(self):
        self.set_x(self.xcor - self.speed*math.cos(self.heading))
        self.set_y(self.ycor - self.speed*math.sin(self.heading))
    #ALL ONCOMING LOOPS POTENTIALLY INEFFICIENT
    # TODO MAKE LOOPS NOT TERRIBLY INEFFICIENT
    def move_forward(self, amount):
        dist = amount
        while dist > 0:
            self.step_forward()
            dist -= self.speed
            time.sleep(0.01)
    def move_backward(self, amount):
        dist = amount
        while dist > 0:
            self.step_backward()
            dist -= self.speed
            time.sleep(0.01)
    def move_left(self, amount):
        dist = amount
        while dist > 0:
            self.set_x(self.xcor - self.speed)
            dist -= self.speed
            time.sleep(0.01)
    def move_right(self, amount):
        dist = amount
        while dist > 0:
            self.set_x(self.xcor + self.speed)
            dist -= self.speed
            time.sleep(0.01)
    def move_up(self, amount):
        dist = amount
        while dist > 0:
            self.set_y(self.ycor - self.speed)
            dist -= self.speed
            time.sleep(0.01)
    def move_down(self, amount):
        dist = amount
        while dist > 0:
            self.set_y(self.ycor + self.speed)
            dist -= self.speed
            time.sleep(0.01)

    #More complex motion
    def go_to(self, newx, newy):
        self.set_x(newx)
        self.set_y(newy)
    def glide_to(self, newx, newy):
        xdist = newx - self.xcor
        ydist = newy - self.ycor
        dist = math.sqrt(xdist**2 + ydist**2)
        tempheading = self.heading
        self.heading = math.atan(ydist/xdist)
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
        #Just to make sure it does end up in the right spot
        self.set_x(newx)
        self.set_y(newy)
        self.heading = tempheading
        for e in self.Elements:
            e.draw()
        self.canvas.update()