from Tkinter import Tk, Canvas


class Manager(object):
    root = Tk()
    canvas = Canvas(root, width=500, height=500)
    elements = []
    stage = None

    frame_number = 1
    mouse_down = False

    default_gravity = False

    keys_pressed = []

    event_delay = 2

    width = 250
    height = 250

    def __init__(self):
        Manager.width = self.canvas.winfo_reqwidth()/2
        Manager.height = self.canvas.winfo_reqwidth()/2

        # Keeping here essentially global variables to get whether the mouse is pressed at any given moment.
        def mouse_press(event):
            Manager.mouse_down = True

        def mouse_release(event):
            Manager.mouse_down = False

        self.canvas.bind("<Button-1>", mouse_press, add="+")
        self.canvas.bind("<ButtonRelease-1>", mouse_release, add="+")

        # Keeping track of what keys are pressed at any given moment

        def key_press(event):
            Manager.keys_pressed.append(event.keysym)

        def key_release(event):
            Manager.keys_pressed.remove(event.keysym)

        self.canvas.bind("<KeyPress>", key_press, add="+")
        self.canvas.bind("<KeyRelease>", key_release, add="+")

        def up_press(event):
            Manager.keys_pressed.append('Up')
        def left_press(event):
            Manager.keys_pressed.append('Left')
        def right_press(event):
            Manager.keys_pressed.append('Right')

        self.canvas.bind('<Up>', up_press, add="+")
        self.canvas.bind('<Left>', left_press, add="+")
        self.canvas.bind('<Right>', right_press, add="+")

    ## THE FRAME MANAGER, THE MOST IMPORTANT FUNCTION. ##

    def run(self):
        Manager.frame_number += 1
        self.canvas.delete("all")
        ## THIS IS WHERE THE CHECKS FOR GRAVITY AND SPEED WOULD GO ##
        self.update_animation()
        self.update_physics()
        self.update_collision()
        self.update_events()
        ## THIS IS THE END OF THE UPDATES FOR SPEED AND GRAVITY ##

        for e in self.elements:
            e.draw()
        self.canvas.update()

    ## ^ THE ABOVE FUNCTION RUNS EVERYTHING ^ ##

    def update_physics(self):
        for e in self.elements:
            if hasattr(e, 'physics_true') and e.physics_true:
                e.update_physics()

    def update_animation(self):
        for e in self.elements:
            e.update_animation()

    def update_collision(self):
        for i in range(len(self.elements) - 1):
            try:
                self.elements[i].update_collision(i + 1)
            except IndexError:
                pass

    def update_events(self):
        for e in self.elements:
            e.update_events()

