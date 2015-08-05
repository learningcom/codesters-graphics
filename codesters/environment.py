from Tkinter import Canvas
from PIL import Image, ImageTk
from .manager import Manager


class StageClass(object):
    image_dictionary = {

    }
    def __init__(self):
        self.root = Manager.canvas
        self.canvas = Manager.canvas
        Manager.elements.append(self)
        Manager.stage = self

        self.type = Environment

        self.canvas.create_rectangle((0, 0, 500, 500), fill='white')

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

        self.wall_bottom_on = True
        self.wall_top_on = True
        self.wall_left_on = True
        self.wall_right_on = True

        self.gravity = 0
        self.bounce = 1
        self.gravity_true = Manager.default_gravity
        self.gravity_override = True

        self.forever_function = None
        self.interval_function = None
        self.interval_length = 0

    #### IMPORTANT FUNCTIONS ####

    def update_physics(self):
        pass

    def update_animation(self):
        pass

    def update_collision(self):
        pass

    def update_events(self):
        pass

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if self.interval_length >=1:
            #print Manager.frame_number, self.interval_length
            if Manager.frame_number % self.interval_length == 0:
                if self.interval_function is not None:
                    #print "we are hrere"
                    self.interval_function()
        self.canvas.create_rectangle((0,0,500,500), fill='white')
        if self.bg_image != None:
            self.bg_photoimg = ImageTk.PhotoImage(self.bg_image)
            self.canvas.create_image(self.xcor, Manager.canvas.winfo_reqheight() - self.ycor, image=self.bg_photoimg)
        # else:


    #### END OF IMPORTANT FUNCTIONS ####


    def add_sprite(self, sprite):
        if sprite not in Manager.elements:
            Manager.elements.append(sprite)

    def add_shape(self, shape):
        if shape not in Manager.elements:
            Manager.elements.append(shape)

    def add_text(self, text): #BROKEN ON CODESTERS.COM
        pass

    def remove_sprite(self,sprite):
        if sprite in Manager.elements:
            Manager.elements.remove(sprite)

    def remove_shape(self, shape):
        if shape in Manager.elements:
            Manager.elements.remove(shape)

    def remove_text(self,text): #BROKEN ON codesters.com
        if text in Manager.elements:
            Manager.elements.remove(text)


    def event_left_key(self, function):
        def newfunction(event):
            self.event = event
            function()
        self.canvas.bind("<Left>", newfunction,add="+")

    def event_right_key(self, function):
        def newfunction(event):
            self.event = event
            function()
        self.canvas.bind("<Right>", newfunction,add="+")

    def event_up_key(self, function):
        def newfunction(event):
            self.event = event
            function()
        self.canvas.bind("<Up>", newfunction,add="+")

    def event_down_key(self, function):
        def newfunction(event):
            self.event = event
            function()
        self.canvas.bind("<Down>", newfunction,add="+")

    def event_space_key(self, function):
        def newfunction(event):
            self.event = event
            function()
        self.canvas.bind("<space>", newfunction, add="+")

    def event_key(self, key, function):
        def newfunction(event):
            self.event = event
            function()
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
        self.canvas.bind(bound_key_name, newfunction, add = "+")

    def event_click(self, function):
        def newfunction(event):
            self.event = event
            function()
        self.canvas.bind("<Button-1>", newfunction, add="+")

    def event_click_down(self, function):
        def newfunction(event):
            self.event = event
            function()
        self.event_click(newfunction,add="+")

    def event_click_up(self, function):
        def newfunction(event):
            self.event = event
            function()
        self.canvas.bind("<ButtonRelease-1>", newfunction, add="+")

    def event_mouse_move(self,function):
        def newfunction(event):
            self.event = event
            function()
        self.canvas.bind("<Motion>", newfunction, add="+")

    def event_forever(self,function):
        self.forever_function = function

    def event_interval(self, function, seconds):
        self.interval_length = seconds * 100
        self.interval_function = function

    def event_delay(self, function, seconds):
        pass

    def set_background(self, image):
        self.bg_image_name= image
        self.bg_image= Image.open("./codesters/sprites/"+image+".gif")

    def set_background_x(self, amount):
        self.xcor=amount + self.canvas.winfo_reqwidth()

    def set_background_y(self, amount):
        self.ycor= amount

    def move_right(self, amount):
        self.xcor +=amount

    def move_left(self, amount):
        self.xcor = self.xcor - amount

    def move_up(self,amount):
        self.ycor += amount

    def move_down(self, amount):
        self.ycor = self.ycor - amount

    def set_background_scaleX(self, amount):
        amount = 1/amount
        amount = int(amount)
        self.bg_scale_x = amount

    def set_background_scaleY(self, amount):
        amount = 1/amount
        amount = int(amount)
        self.bg_scale_y = amount
        self.canvas.update()

    def click_x(self):
        # print "x coord", event.x
        return self.event.x - (self.canvas.winfo_reqwidth()/2)

    def click_y(self):
        # print "y coord", event.y
        return (self.canvas.winfo_reqheight()/2) - self.event.y

    def mouse_x(self):
        return (self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()) - self.canvas.winfo_reqwidth()/2
    def mouse_y(self):
        return self.canvas.winfo_reqheight()/2 - (self.canvas.winfo_pointery() - self.canvas.winfo_rooty())

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
        for e in Manager.elements:
            if not e.gravity_override:
                e.gravity_true = True
                e.gravity = amount/10.0
        Manager.default_gravity = True


    def wait(self, seconds):
        for e in Manager.elements:
            if e.type != Environment:
                e.wait(seconds)

    def get_sprite_by_index(self, index):
        return Manager.elements[index]

class Environment(StageClass):
    def __init__(self):
        super(Environment, self).__init__()
