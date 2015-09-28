from Tkinter import Canvas
from PIL import Image, ImageTk
from .manager import Manager
import os
import sys

class StageClass(object):
    """The base class of the Environment class

    This defines all the methods of the Environment class

    .. note::

       This is an example note

    """
    image_dictionary = {
        "underwater": "Underwater_BG-01",
        "summer": "beach",
        "space": "space2",
        "moon": "Space-Background",
        "stage": "Stage",
        "winter": "Winterscape",
        "grid2": "gridfine",
        "park": "Playground",
        "stadium": "BasketballStadium",
        "flower_field": "Long-flower-field",
        "spring": '',   # CANNOT FIND THIS IMAGE IN SPRITES
        "fall": '',   # CANNOT FIND THIS IMAGE IN SPRITES
        "tilewall": "bathroom-01",
        "concert": "concertstage",
        "theater": "Stage",
        "city": "CityBackground",
        "baseballfield": "baseballdiamond",
        "grid": "Modified-graph",
        "houseinterior": '',   # CANNOT FIND THIS IMAGE IN SPRITES
        "soccerfield": "soccer-field",
        "subway": '',   # CANNOT FIND THIS IMAGE IN SPRITES
        "flowers": "flowerfield",
        "footballfield": "footballfield",
        "jungle": '',   # CANNOT FIND THIS IMAGE IN SPRITES
    }

    def __init__(self):
        self.root = Manager.canvas
        self.canvas = Manager.canvas
        Manager.elements.append(self)
        Manager.stage = self

        self.type = Environment

        self.canvas.create_rectangle((0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()), fill='white')

        self.xcor = 0
        self.ycor = 0
        self.size = 1
        self.bg_image_name = None
        self.bg_image = None
        self.bg_photoimg = None
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
        self.bounce = 0.9
        self.gravity_true = Manager.default_gravity
        self.gravity_override = True

        self.forever_function = None
        self.interval_function = None
        self.interval_length = 0

        import os
        self.directory = os.path.dirname(str(os.path.abspath(__file__)))
        import glob
        self.sprite_list = glob.glob(self.directory+'/sprites/*')
        self.script_directory = os.path.dirname(os.path.realpath(sys.argv[0]))



        self.key_functions = {}

    #### IMPORTANT FUNCTIONS ####

    def update_physics(self):
        pass

    def update_animation(self):
        pass

    def update_collision(self, i):
        pass

    def update_events(self):
        for key in Manager.keys_pressed:
            if key in self.key_functions.keys() and Manager.frame_number % Manager.event_delay == 0:
                # for e in Manager.elements:
                #     e.clear_queue()
                for i in self.key_functions[key]:
                    i()

    def draw(self):
        """The draw function updates the tk canvas

        """
        if self.forever_function is not None:
            self.forever_function()
        if self.interval_length >= 1:
            if Manager.frame_number % self.interval_length == 0:
                if self.interval_function is not None:
                    self.interval_function()
        self.canvas.create_rectangle((0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()), fill='white')
        if self.bg_photoimg is not None:
            self.canvas.create_image(self.xcor, Manager.canvas.winfo_reqheight() - self.ycor, image=self.bg_photoimg)
        elif self.bg_image is not None:
            self.bg_photoimg = ImageTk.PhotoImage(self.bg_image)
            self.canvas.create_image(self.xcor, Manager.canvas.winfo_reqheight() - self.ycor, image=self.bg_photoimg)

    #### END OF IMPORTANT FUNCTIONS ####

    def add_sprite(self, sprite):
        """add_sprite will add a sprite to the stage.
        Note that a sprite may not be visible on the tk canvas when added if there
        is no image for the sprite or if the sprite is hidden.
        Manager.elements keeps a list of all sprites that have been added to the stage.

        """
        if sprite not in Manager.elements:
            Manager.elements.append(sprite)

    def add_shape(self, shape):
        if shape not in Manager.elements:
            Manager.elements.append(shape)

    def add_text(self, text):  # BROKEN ON CODESTERS.COM
        pass

    def remove_sprite(self, sprite):
        if sprite in Manager.elements:
            sprite.clean_up()
            Manager.elements.remove(sprite)


    def remove_shape(self, shape):
        if shape in Manager.elements:
            Manager.elements.remove(shape)

    def remove_text(self, text):  # BROKEN ON codesters.com
        if text in Manager.elements:
            Manager.elements.remove(text)

    def clear_queue(self):
        pass

    def event_left_key(self, function):
        def newfunction():
            # for e in Manager.elements:
            #     e.clear_queue()
            function()
        if "Left" not in self.key_functions.keys():
            self.key_functions['Left'] = [newfunction]
        else:
            self.key_functions['Left'].append(newfunction)

    def event_right_key(self, function):
        def newfunction():
            # for e in Manager.elements:
            #     e.clear_queue()
            function()
        if "Right" not in self.key_functions.keys():
            self.key_functions['Right'] = [newfunction]
        else:
            self.key_functions['Right'].append(newfunction)

    def event_up_key(self, function):
        def newfunction():
            # for e in Manager.elements:
            #     e.clear_queue()
            function()
        if "Up" not in self.key_functions.keys():
            self.key_functions['Up'] = [newfunction]
        else:
            self.key_functions['Up'].append(newfunction)

    def event_down_key(self, function):
        def newfunction():
            # for e in Manager.elements:
            #     e.clear_queue()
            function()
        if "Down" not in self.key_functions.keys():
            self.key_functions['Down'] = [newfunction]
        else:
            self.key_functions['Down'].append(newfunction)

    def event_space_key(self, function):
        def newfunction():
            # for e in Manager.elements:
            #     e.clear_queue()
            function()
        if "space" not in self.key_functions.keys():
            self.key_functions['space'] = [newfunction]
        else:
            self.key_functions['space'].append(newfunction)

    def event_key(self, key, function):
        def newfunction():
            # for e in Manager.elements:
            #     e.clear_queue()
            function()
        bound_key_name = key
        if key == "left":
            bound_key_name = "Left"
        if key == "right":
            bound_key_name = "Right"
        if key == "up":
            bound_key_name = "Up"
        if key == "down":
            bound_key_name = "Down"
        if key == "space":
            bound_key_name = "space"
        if bound_key_name not in self.key_functions.keys():
            self.key_functions[bound_key_name] = [newfunction]
        else:
            self.key_functions[bound_key_name].append(newfunction)

    def event_click(self, function):
        """sets the function to call on the event of a click on the tk canvas.
        """
        def newfunction(event):
            self.event = event
            if function:
                function()
        self.canvas.bind("<Button-1>", newfunction, add="+")

    def event_click_down(self, function):
        def newfunction(event):
            self.event = event
            if function:
                function()
        self.canvas.bind("<Button-1>", newfunction, add="+")

    def event_click_up(self, function):
        def newfunction(event):
            self.event = event
            if function:
                function()
        self.canvas.bind("<ButtonRelease-1>", newfunction, add="+")

    def event_mouse_move(self, function):
        def newfunction(event):
            self.event = event
            if function:
                function()
        self.canvas.bind("<Motion>", newfunction, add="+")

    def event_forever(self, function):
        self.forever_function = function

    def event_interval(self, function, seconds):
        self.interval_length = seconds * 25
        self.interval_function = function

    def event_delay(self, function, seconds):
        pass

    def set_background(self, image):
        if image:

            if image in self.image_dictionary:
                self.bg_image_name = self.image_dictionary[image]
            else:
                self.bg_image_name = image

            default_img_path = self.directory+"/sprites/"+self.bg_image_name+".gif"
            script_img_path = self.script_directory + "/" + self.bg_image_name + ".gif"
            img_path = None

            if os.path.isfile(script_img_path):
                img_path = script_img_path
            elif os.path.isfile(default_img_path):
                img_path = default_img_path
            else:
                self.bg_image_name = self.image_dictionary['grid']
                img_path = self.directory + "/sprites/" + self.bg_image_name + ".gif"

            try:
                self.bg_image = Image.open(img_path)
            except Exception as ex:
                print ex
                self.bg_photoimg = None
                self.bg_image = None
                self.bg_image_name = ''

        else:
            self.bg_photoimg = None
            self.bg_image = None
            self.bg_image_name = ''

    def set_background_x(self, amount):
        self.xcor = amount + self.canvas.winfo_reqwidth()

    def set_background_y(self, amount):
        self.ycor = amount

    def move_right(self, amount):
        self.xcor += amount

    def move_left(self, amount):
        self.xcor = self.xcor - amount

    def move_up(self, amount):
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
        return self.mouse_x()

    def click_y(self):
        return self.mouse_y()

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
        self.enable_all_walls()

    def set_gravity(self, amount):
        self.gravity = amount
        self.enable_floor()
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
    """The class of the Environment class

    This defines all the methods of the Environment class

    .. note::

       This is an example note

    """
    def __init__(self):
        super(Environment, self).__init__()
