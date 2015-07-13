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
    future_heading = 0
    animation_duration = 0
    animation_x_coords = []
    animation_y_coords = []
    animation_index = 0
    future_x=0
    future_y=0
    angle = 0
    step_size=0
    ## PIVOTAL FUNCTIONS ##
    def __init__(self,canvas, Elements, image):
        self.heading = 0
        self.canvas = canvas
        self.Elements = Elements
        self.animation_duration=1000
        self.speed = 1
        self.rotation_direction=1
        self.xcor= self.canvas.winfo_reqwidth()/2
        self.ycor = self.canvas.winfo_reqheight()/2
        if image != '':
            self.photo = Image.open("./codesters/sprites/"+image+".gif")
            # im2 = self.photo.convert('RGBA')
            # rot = im2.rotate(self.heading, expand=1)
            # fff =  Image.new("RGBA", rot.size, (0,)*4)
            # self.photo = Image.composite(rot,fff,rot)





    def draw(self):
        if self.photo != None and self.hidden == False:
            # im2 = self.photo.convert('RGBA')
            # self.photo.close()
            # rot = im2.rotate(self.heading, expand=1)
            # fff =  Image.new("RGBA", rot.size, (0,)*4)
            # self.photo = Image.composite(rot,fff,rot)
            # rot.close()
            # fff.close()
            # im2.close()
            #  im2 = self.photo.convert('RGBA')
            # self.photo.close()
            # rot = im2.rotate(self.heading, expand=1)
            # fff =  Image.new("RGBA", rot.size, (0,)*4)
            # self.photo = Image.composite(rot,fff,rot)
            # rot.close()
            # fff.close()
            # im2.close()
            self.bg_photoimg = ImageTk.PhotoImage(self.photo)
            self.canvas.create_image((self.xcor + self.canvas.winfo_reqwidth()/2, self.canvas.winfo_reqheight()/2 - self.ycor), image = self.bg_photoimg)
        elif self.hidden == False:
            self.canvas.create_oval((self.xcor-(self.size/2),self.ycor-(self.size/2),self.xcor+(self.size/2),self.ycor+(self.size/2)), fill=self.color)

    ## END OF PIVOTAL FUNCTIONS ##

    def hide(self):
        self.hidden=True
    def show(self):
        self.hidden=False



    #Basic motion
    def move_right(self, amount):
        self.glide_to(self.future_x+amount, self.future_y)
    def move_left(self, amount):
        self.glide_to(self.future_x-amount,self.future_y)
    def move_down(self, amount):
        self.glide_to(self.future_x,self.future_y-amount)
    def move_up(self, amount):
        self.glide_to(self.future_x,self.future_y+amount)
    def move_forward(self,amount):
        desired_x = amount * math.cos(self.heading * (math.pi/180)) + self.future_x
        desired_y = amount * math.sin(self.heading * (math.pi/180)) + self.future_y
        self.glide_to(desired_x,desired_y)
    def forward(self,amount):
        desired_x = amount * math.cos(self.heading * (math.pi/180)) + self.future_x
        desired_y = amount * math.sin(self.heading * (math.pi/180)) + self.future_y
        self.glide_to(desired_x,desired_y)
    def move_backward(self,amount):
        desired_x = (-1*(amount * math.cos(self.heading * (math.pi/180)))) +self.future_x
        desired_y = (-1*(amount * math.sin(self.heading * (math.pi/180)))) + self.future_y
        self.glide_to(desired_x,desired_y)
    def backward(self,amount):
        desired_x = (-1*(amount * math.cos(self.heading * (math.pi/180)))) +self.future_x
        desired_y = (-1*(amount * math.sin(self.heading * (math.pi/180)))) + self.future_y
        self.glide_to(desired_x,desired_y)
    def move_back(self,amount):
        desired_x = (-1*(amount * math.cos(self.heading * (math.pi/180)))) +self.future_x
        desired_y = (-1*(amount * math.sin(self.heading * (math.pi/180)))) + self.future_y
        self.glide_to(desired_x,desired_y)
    def back(self,amount):
        desired_x = (-1*(amount * math.cos(self.heading * (math.pi/180)))) +self.future_x
        desired_y = (-1*(amount * math.sin(self.heading * (math.pi/180)))) + self.future_y
        self.glide_to(desired_x,desired_y)
    def movex(self, amount):
        self.glide_to(self.future_x+amount, self.future_y)
    def move_x(self, amount):
        self.glide_to(self.future_x+amount, self.future_y)
    def movey(self, amount):
        self.glide_to(self.future_x,self.future_y+amount)
    def move_y(self, amount):
        self.glide_to(self.future_x,self.future_y+amount)
    def translate_y(self, amount):
        self.glide_to(self.future_x,self.future_y+amount)
    def translate_x(self, amount):
        self.glide_to(self.future_x+amount, self.future_y)

    #More complex motion
    def go_to(self, newx, newy):
        self.animation_x_coords.append(newx)
        self.animation_y_coords.append(newy)
        self.xcor = newx
        self.ycor = newy
        self.future_x = newx
        self.future_y = newy

    def goto(self, newx, newy):
        self.animation_x_coords.append(newx)
        self.animation_y_coords.append(newy)
        self.xcor = newx
        self.ycor = newy
        self.future_x = newx
        self.future_y = newy

    def glide_to(self, newx, newy):
        print self.future_x, " ", self.future_y
        xdist = float(newx - self.future_x)
        ydist = float(newy - self.future_y)
        dist = math.sqrt(xdist**2 + ydist**2)
        self.animation_duration = dist/self.speed
        frames_needed = (self.animation_duration / 22)
        x_step_size = xdist/frames_needed
        y_step_size = ydist/frames_needed
        for n in range(int(frames_needed)):
            self.animation_x_coords.append(self.future_x+(x_step_size+(x_step_size * n)))
            self.animation_y_coords.append(self.future_y+(y_step_size+(y_step_size * n)))
        self.future_x = self.animation_x_coords[-1]
        self.future_y = self.animation_y_coords[-1]
        #print self.future_x, " ", self.future_y
        #print self.animation_x_coords, self.animation_y_coords

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


    ##
    def set_direction(self, tox, toy):
        self.future_heading = math.atan(float(toy)/float(tox))
        print self.future_heading
        frames_needed = (self.animation_duration / 22)
        degree_rot = self.future_heading - self.heading
        self.step_size = .3 #degree_rot/frames_needed

        print self.future_heading
    #Set variables
    def set_x(self, newx):
        self.xcor = newx
        self.future_x = self.xcor
    def set_y(self, newy):
        self.ycor = newy
        self.future_y = self.ycor
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
    # def step_forward(self):
    #     self.set_x(self.xcor + self.speed*math.cos(self.heading))
    #     self.set_y(self.ycor + self.speed*math.sin(self.heading))
    # def step_backward(self):
    #     self.set_x(self.xcor - self.speed*math.cos(self.heading))
    #     self.set_y(self.ycor - self.speed*math.sin(self.heading))
    # def move_forward(self, amount):
    #     dist = amount
    #     while dist > 0:
    #         self.step_forward()
    #         dist -= self.speed
    #         time.sleep(0.01)
    # def move_backward(self, amount):
    #     dist = amount
    #     while dist > 0:
    #         self.step_backward()
    #         dist -= self.speed
    #         time.sleep(0.01)



