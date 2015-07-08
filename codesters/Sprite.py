from Tkinter import *
import math
import time
from PIL import Image, ImageTk

class SpriteClass:
    #Default values
    xcor = 0
    ycor = 0
    xspeed = 0
    yspeed = 0
    speed = 0
    size = 50
    color = 'white'
    heading = 0
    photo = Image.open("./codesters/sprites/codestersLogo.gif")
    hidden= False
    heading = 0
    animation_duration = 0
    animation_x_coords = []
    animation_y_coords = []
    animation_index = 0
    future_x=0
    future_y=0
    def __init__(self,canvas, Elements, image):
        self.heading = 0
        self.canvas = canvas
        self.Elements = Elements
        self.animation_duration=1000
        self.speed = 1
        if image != '':
            self.photo = Image.open("./codesters/sprites/"+image+".gif")


    def draw(self):
        if self.photo != None and self.hidden == False:
            self.bg_photoimg = ImageTk.PhotoImage(self.photo)
            self.canvas.create_image((self.xcor,self.ycor), image = self.bg_photoimg)
        elif self.hidden == False:
            self.canvas.create_oval((self.xcor-(self.size/2),self.ycor-(self.size/2),self.xcor+(self.size/2),self.ycor+(self.size/2)), fill=self.color)

    def hide(self):
        self.hidden=True
    def show(self):
        self.hidden=False
    #Set variables
    def set_x(self, newx):
        self.xcor = newx+self.canvas.winfo_width()/2
    def set_y(self, newy):
        self.ycor = self.canvas.winfo_height()/2-newy
    def get_x(self):
        return self.xcor
    def get_y(self):
        return self.ycor
    def set_x_speed(self, newspeed):
        self.xspeed = newspeed
    def set_y_speed(self, newspeed):
        self.yspeed = newspeed
    def set_speed(self, newspeed):
        self.speed = newspeed
        self.animation_duration = 1000/newspeed
    def jump(self, newspeed):
        self.yspeed = newspeed
    def set_size(self, newsize):
        self.size = 50 * newsize
    def set_color(self, newcolor):
        self.color = newcolor
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
        self.glide_to(self.future_x-amount,self.future_y)
    def move_right(self, amount):
        self.glide_to(self.future_x+amount, self.future_y)
    def move_up(self, amount):
        self.glide_to(self.future_x,self.future_y+amount)
    def move_down(self, amount):
        self.glide_to(self.future_x,self.future_y-amount)

    #More complex motion
    def go_to(self, newx, newy):
        self.set_x(newx)
        self.set_y(newy)

    def goto(self, newx, newy):
        self.set_x(newx)
        self.set_y(newy)

    def glide_to(self, newx, newy):
        xdist = float(newx - self.future_x)
        ydist = float(newy - self.future_y)
        #dist = math.sqrt(xdist**2 + ydist**2)
        frames_needed = (self.animation_duration / 22)
        x_step_size = xdist/frames_needed
        y_step_size = ydist/frames_needed
        for n in range(int(frames_needed)):
            self.animation_x_coords.append(self.future_x+(x_step_size+(x_step_size * n)))
            self.animation_y_coords.append(self.future_y+(y_step_size+(y_step_size * n)))
        self.future_x = newx
        self.future_y = newy
        print self.future_x, " ", self.future_y
        print self.animation_x_coords, self.animation_y_coords

        # tempheading = self.heading
        # self.heading = math.atan(ydist/xdist)
        # #Trig stuff
        # while dist > self.speed:
        #     if xdist > 0:
        #         self.set_x(self.xcor + self.speed*math.cos(self.heading))
        #     else:
        #         self.set_x(self.xcor - self.speed*math.cos(self.heading))
        #     if ydist > 0:
        #         self.set_y(self.future_y + self.speed*math.sin(self.heading))
        #     else:
        #         self.set_y(self.ycor - self.speed*math.sin(self.heading))
        #     xdist = newx - self.xcor
        #     ydist = newy - self.ycor
        #     dist = math.sqrt(xdist**2 + ydist**2)
        # #Just to make sure it does end up in the right spot
        # self.set_x(newx)
        # self.set_y(newy)
        # self.heading = tempheading
        # self.canvas.delete("all")
