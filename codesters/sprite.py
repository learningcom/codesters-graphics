import math
from PIL import Image, ImageTk
from .manager import Manager

class SpriteClass(object):

    # PIVOTAL FUNCTIONS ##
    def __init__(self, image):
        self.canvas = Manager.canvas
        Manager.elements.append(self)

        # Default values
        self.xcor = 0
        self.ycor = 0
        self.xspeed = 0
        self.yspeed = 0
        self.speed = 1
        self.modes=[]
        self.size = 1
        self.color = 'white'
        self.heading = 0

        self.photo = Image.open("./codesters/sprites/codestersLogo.gif")
        self.base_photo = Image.open("./codesters/sprites/codestersLogo.gif")

        self.hidden = False

        self.future_heading = 0
        self.animation_duration = 1000
        self.animation_x_coords = []
        self.animation_y_coords = []
        self.animation_rotation_degrees = []
        self.animation_index = 0
        self.rotation_direction=1
        self.future_x = 0
        self.future_y = 0
        self.angle = 0
        self.step_size = 0

        self.wait_list = []
        self.total_wait_time = 0
        self.future_most_recent_wait_time = 0

        self.say_text = ""
        self.say_color = ""
        self.say_size = 0
        self.say_time = 0
        self.say_font = ""

        self.paused = False

        self.gravity = 0.1
        self.gravity_true = False
        self.physics_true = False

        self.goal = False
        self.hazard = False
        self.collision = False
        self.drag = False

        if image != '':
            self.base_photo = Image.open("./codesters/sprites/"+image+".gif")
            self.photo = Image.open("./codesters/sprites/"+image+".gif")
            im2 = self.photo.convert('RGBA')
            rot = im2.rotate(self.heading, expand=1)
            fff =  Image.new("RGBA", rot.size, (0,)*4)
            self.photo = Image.composite(rot,fff,rot)

        self.width = self.photo.size[0]
        self.height = self.photo.size[1]

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
            if self.say_time != 0:
                self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,self.canvas.winfo_reqheight()/2 - self.ycor - 100,text=self.say_text, font=(self.say_font,self.say_size),fill=self.say_color)
                self.say_time = self.say_time-1
        elif self.hidden == False:
            self.canvas.create_oval((self.xcor-(self.size/2),self.ycor-(self.size/2),self.xcor+(self.size/2),self.ycor+(self.size/2)), fill=self.color)

    def update_physics(self):
        self.xcor += self.xspeed
        self.ycor -= self.yspeed
        if self.gravity_true:
            self.yspeed += self.gravity

    def update_image(self):
        im2 = self.base_photo.convert('RGBA')
        #self.base_photo.close()
        rot = im2.rotate(self.heading, expand=1)
        scale = rot.resize((int(self.size * self.width), int(self.size*self.width)), Image.ANTIALIAS)
        fff = Image.new("RGBA", scale.size, (0,)*4)
        self.photo = Image.composite(scale,fff,scale)
        self.photo.save("check.gif")

    def update_animation(self):
        if len(self.modes) > 0 and not self.paused:
            #print self.modes
            if self.modes[0] == "wait":
                if len(self.wait_list)> 0:
                    if self.wait_list[0] == 0:
                        print self.wait_list.pop(0)
                        print self.wait_list.pop(0)
                        print self.modes.pop(0)
                    else:
                        self.wait_list[0] = self.wait_list[0] - 1

            else:
                if self.modes[0] == "translate":
                    if len(self.animation_y_coords)>0 and len(self.animation_x_coords)>0:
                        if isinstance(self.animation_x_coords[0],basestring) and isinstance(self.animation_y_coords[0],basestring):
                            print self.animation_x_coords.pop(0)
                            print self.animation_y_coords.pop(0)
                            print self.modes.pop(0)
                        else:
                            self.set_x(self.animation_x_coords.pop(0))
                            self.set_y(self.animation_y_coords.pop(0))
                            if len(self.animation_x_coords)>0:
                                self.future_x = self.animation_x_coords[-1]
                            if len(self.animation_y_coords)>0:
                                self.future_y = self.animation_y_coords[-1]
                elif self.modes[0] == "rotate":
                    if len(self.animation_rotation_degrees)>0 :
                        if isinstance(self.animation_rotation_degrees[0],basestring):
                            print self.animation_rotation_degrees.pop(0)
                            print self.modes.pop(0)
                        else:
                            self.heading = self.animation_rotation_degrees.pop(0)
                            self.update_image()

                            #rot.close()
                            #fff.close()
                            #im2.close()

    # END OF PIVOTAL FUNCTIONS ##

    def hide(self):
        self.hidden=True

    def show(self):
        self.hidden=False

    # Basic motion
    def move_right(self, amount):
        self.glide_to(self.future_x+amount, self.future_y)

    def move_left(self, amount):
        self.glide_to(self.future_x-amount,self.future_y)

    def move_down(self, amount):
        self.glide_to(self.future_x,self.future_y-amount)

    def move_up(self, amount):
        self.glide_to(self.future_x,self.future_y+amount)
    def move_forward(self, amount):
        desired_x = amount * math.cos(self.future_heading * (math.pi/180)) + self.future_x
        desired_y = amount * math.sin(self.future_heading * (math.pi/180)) + self.future_y
        self.glide_to(desired_x,desired_y)

    def forward(self, amount):
        self.move_forward(amount)

    def move_backward(self, amount):
        self.move_forward(-amount)

    def backward(self, amount):
        self.move_forward(-amount)

    def move_back(self, amount):
        desired_x = (-1*(amount * math.cos(self.heading * (math.pi/180)))) +self.future_x
        desired_y = (-1*(amount * math.sin(self.heading * (math.pi/180)))) + self.future_y

    def move_forward(self,amount):
        desired_x = amount * math.cos(self.future_heading * (math.pi/180)) + self.future_x
        desired_y = amount * math.sin(self.future_heading * (math.pi/180)) + self.future_y
        self.glide_to(desired_x,desired_y)
    def forward(self,amount):
        self.move_forward(amount)
    def move_backward(self,amount):
        self.move_forward(-1 * amount)
    def backward(self,amount):
        self.move_backward(amount)
    def move_back(self,amount):
        self.move_backward(amount)
    def back(self,amount):
        self.move_backward(amount)
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

    # More complex motion
    def go_to(self, newx, newy):
        self.set_x(newx)
        self.set_y(newy)

    def goto(self, newx, newy):
        self.go_to(newx,newy)

    def glide_to(self, newx, newy):
        print self.future_x, " ", self.future_y
        print newx, self.future_x
        xdist = float(newx - self.future_x)
        ydist = float(newy - self.future_y)
        dist = math.sqrt(xdist**2 + ydist**2)
        frames_needed = ((dist/self.speed) / 22)
        if frames_needed == 0:
            frames_needed = 1
        x_step_size = xdist/frames_needed
        y_step_size = ydist/frames_needed
        tempx = self.future_x
        tempy = self.future_y
        self.future_x = newx
        self.future_y = newy
        for n in range(int(frames_needed)):
            self.animation_x_coords.append(tempx+(x_step_size+(x_step_size * n)))
            self.animation_y_coords.append(tempy+(y_step_size+(y_step_size * n)))
            #print self.animation_x_coords, self.animation_y_coords
        print self.future_x, " ", self.future_y
        self.future_x = self.animation_x_coords[-1]
        self.future_y = self.animation_y_coords[-1]
        self.animation_x_coords.append("Finished current animation")
        self.animation_y_coords.append("Finished current animation")
        print self.future_x, "future_x"
        self.modes.append("translate")
        print '###########'


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

    #
    def set_direction(self, tox, toy):
        if (tox==0):
            tox=.000001
        destination = math.atan(float(toy - self.future_y)/float(tox - self.future_x))*(180/math.pi)
        if tox - self.future_x < 0:
            destination += 180
        print destination - self.future_heading, "HERE"
        frames_needed = (self.animation_duration / 22)
        if frames_needed == 0:
            frames_needed = 1
        degree_rot = destination - self.future_heading
        self.step_size = float(degree_rot)/float(frames_needed)
        for n in range(int(frames_needed)):
            self.animation_rotation_degrees.append(self.step_size+(self.step_size*n)+self.future_heading)
        self.animation_rotation_degrees[-1] = destination
        self.animation_rotation_degrees.append("Finished current animation")
        self.modes.append("rotate")
        self.future_heading = destination

    def point_towards(self, tox, toy):
        self.set_direction(tox, toy)

    def turn_clockwise(self, degrees):
        destination = self.future_heading - degrees
        frames_needed = (self.animation_duration / 22)
        degree_rot = destination - self.future_heading
        self.step_size = float(degree_rot)/float(frames_needed)
        for n in range(int(frames_needed)):
            self.animation_rotation_degrees.append(self.step_size+(self.step_size*n)+self.future_heading)
        self.animation_rotation_degrees[-1] = destination
        self.animation_rotation_degrees.append("Finished current animation")
        print self.animation_rotation_degrees
        self.modes.append("rotate")
        self.future_heading = destination

    def turn_right(self, degrees):
        self.turn_clockwise(degrees)

    def right(self, degrees):
        self.turn_clockwise(degrees)

    def turn_counterclockwise(self,degrees):
        destination = self.future_heading + degrees
        frames_needed = (self.animation_duration / 22)
        degree_rot = destination - self.future_heading
        self.step_size = float(degree_rot)/float(frames_needed)
        for n in range(int(frames_needed)):
            self.animation_rotation_degrees.append(self.step_size+(self.step_size*n)+self.future_heading)
        self.animation_rotation_degrees[-1] = destination
        self.animation_rotation_degrees.append("Finished current animation")
        self.modes.append("rotate")
        self.future_heading = destination

    def turn_left(self,degrees):
        self.turn_counterclockwise(degrees)

    def left(self,degrees):
        self.turn_counterclockwise(degrees)

    #
    def wait(self, seconds):
        self.modes.append("wait")
        self.wait_list.append(seconds*10)
        self.wait_list.append("Finished current animation")
        print self.wait_list
        self.total_wait_time += seconds
        self.future_most_recent_wait_time = seconds

    def get_wait_time(self):
        return self.future_most_recent_wait_time

    def get_total_wait_time(self):
        return self.total_wait_time

    def say(self, text,seconds=-1,color="#000000", size=12, font="Purisa"):
        self.say_text = text
        self.say_time = seconds
        self.say_color = color
        self.say_size = size
        self.say_font = font

    def ask(self, text):
        return raw_input(text)

    def reset_animation(self):
        self.animation_rotation_degrees = []
        self.animation_x_coords = []
        self.animation_y_coords = []
        self.modes = []

    def pause(self):
        self.paused = True

    def stop(self):
        self.reset_animation()

    def reset(self):
        self.reset_animation()

    def play(self):
        self.paused = False

    #Physics

    def jump(self, newspeed):
        self.yspeed = -newspeed

    def gravity_on(self):
        self.gravity_true = True

    def gravity_off(self):
        self.gravity_true = False

    def physics_on(self):
        self.physics_true = True
        self.gravity_on()

    def physics_off(self):
        self.physics_true = False
        self.gravity_off()

    def set_gravity_on(self):
        self.gravity_on()

    def set_gravity_off(self):
        self.gravity_off()

    def set_physics_on(self):
        self.physics_on()

    def set_physics_off(self):
        self.physics_off()

    def is_goal(self):
        self.goal = True

    def collision_goal_on(self):
        self.goal = True

    def collision_goal_off(self):
        self.goal = False

    def is_hazard(self):
        self.hazard = True

    def collision_hazard_on(self):
        self.hazard = True

    def collision_hazard_off(self):
        self.hazard = False

    def cannot_collide(self):
        self.collision = False

    def collision_on(self):
        self.collision = True

    def collision_off(self):
        self.collision = False

    def set_drag_on(self):
        self.drag = True

    def set_drag_off(self):
        self.drag = False

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

    def set_size(self, newsize):
        self.size = newsize
        self.update_image()

    def set_color(self, newcolor):
        self.color = newcolor

    def set_heading(self, degrees):
        self.heading = degrees

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


class Sprite(SpriteClass):

    def __init__(self, image):
        super(Sprite, self).__init__(image)
