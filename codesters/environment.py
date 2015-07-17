from Tkinter import *
from PIL import Image, ImageTk
from .manager import Manager

class StageClass(object):

    def __init__(self):
        self.root = Manager.canvas
        self.canvas = Manager.canvas
        Manager.elements.append(self)
        Manager.stage = self

        self.canvas.create_rectangle((0, 0, 500, 500), fill='white')

        # self.canvas.bind("<Button-1>", self.click_x)
        # self.canvas.bind("<Button-1>", self.click_y)
        # self.canvas.bind("<1>", lambda event: self.canvas.focus_set())

        self.xcor = 0
        self.ycor = 0
        self.size = 1
        self.bg_image_name = None
        self.bg_image = None
        self.bg_scale_y = 1
        self.bg_scale_x = 1
        self.scaled_image = None
        self.canvas.focus_set()

        self.xcor = self.canvas.winfo_reqwidth()/2
        self.ycor = self.canvas.winfo_reqheight()/2
        self.size = 1

        self.physics_true = False

        self.wall_bottom_on = False
        self.wall_top_on = False
        self.wall_left_on = False
        self.wall_right_on = False

        self.gravity = 0
        self.bounce = 1

    def update_physics(self):
        pass

    def update_animation(self):
        pass

    def update_collision(self):
        pass

    def draw(self):
        if self.bg_image != None:
            # background_label = Label(self.root, image=self.bg_image)
            # background_label.place(x=self.xcor, y=self.ycor, relwidth=1, relheight=1)
            # background_label.image=self.bg_image
            # print self.canvas.winfo_width()
            self.bg_photoimg = ImageTk.PhotoImage(self.bg_image)
            self.canvas.create_image(self.xcor, self.ycor, image=self.bg_photoimg)
        else:
            self.canvas.create_rectangle((0,0,500,500), fill='white')

    def set_background(self, image):
        self.bg_image_name= image
        self.bg_image= Image.open("./codesters/sprites/"+image+".gif")
        # print self.bg_image.height, "blah"

    def set_background_x(self, amount):
        self.xcor=amount+self.canvas.winfo_width()

    def set_background_y(self, amount):
        self.ycor=amount+self.canvas.winfo_height()

    def set_background_scaleX(self, amount):
        amount = 1/amount
        amount = int(amount)
        self.bg_scale_x = amount

    def set_background_scaleY(self, amount):
        amount = 1/amount
        amount = int(amount)
        self.bg_scale_y = amount
        self.canvas.update()

    def click_x(self, event):
        #print "x coord", event.x
        return event.x-250

    def click_y(self, event):
        #print "y coord", event.y
        return (event.y*-1)+250

    def event_click(self, function):
        self.canvas.bind("<Button-1>", function)

    def event_up_key(self, function):
        self.canvas.bind("<Up>", function)

    def event_down_key(self, function):
        self.canvas.bind("<Down>", function)

    def event_left_key(self, function):
        self.canvas.bind("<Left>", function)

    def event_right_key(self, function):
        self.canvas.bind("<Right>", function)

    def event_space_key(self, function):
        self.canvas.bind("<space>", function)

    def event_click_up(self, function):
        self.canvas.bind("<ButtonRelease-1>", function)

    def event_key(self, key, function):
        bound_key_name = key
        if key == "left":
            bound_key_name = "<Left>"
        if key == "right":
            bound_key_name = "<Right>"
        if key == "up":
            bound_key_name = "<Up>"
        if key == "down":
            bound_key_name = "<Down>"
        if key == "space":
            bound_key_name = "<space>"
        print bound_key_name
        self.canvas.bind(bound_key_name, function)

    def enable_floor(self):
        self.wall_bottom_on = True

    def disable_floor(self):
        self.wall_bottom_on = False

    def enable_ceiling(self):
        self.wall_top_on = True

    def disable_ceiling(self):
        self.wall_top_on = False

    def enable_right_wall(self):
        self.wall_right_on = True

    def disable_right_wall(self):
        self.wall_right_on = False

    def enable_left_wall(self):
        self.wall_left_on = True

    def disable_left_wall(self):
        self.wall_left_on = False

    def enable_all_walls(self):
        self.enable_floor()
        self.enable_ceiling()
        self.enable_left_wall()
        self.enable_right_wall()

    def disable_all_walls(self):
        self.disable_floor()
        self.disable_ceiling()
        self.disable_left_wall()
        self.disable_right_wall()

    def set_bounce(self, amount):
        self.bounce = amount

    def set_gravity(self, amount):
        self.gravity = amount

class Environment(StageClass):
    def __init__(self):
        super(Environment, self).__init__()
