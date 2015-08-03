from Tkinter import Tk, Canvas


class Manager(object):
    root = Tk()
    canvas = Canvas(root, width=500, height=500)
    elements = []
    stage = None

    frame_number = 1
    mouse_down = False

    default_gravity = False

    wait_time = 0

    def __init__(self):
        #Keeping here essentially global variables to get the mouse position and whether it's pressed at any given moment.
        def mouse_press(event):
            Manager.mouse_down = True
        def mouse_release(event):
            Manager.mouse_down = False
        self.canvas.bind("<Button-1>", mouse_press, add="+")
        self.canvas.bind("<ButtonRelease-1>", mouse_release, add="+")

    ## THE FRAME MANAGER, THE MOST IMPORTANT FUNCTION. ##

    def run(self):
        Manager.frame_number += 1
        self.canvas.delete("all")
        ## THIS IS WHERE THE CHECKS FOR GRAVITY AND SPEED WOULD GO ##
        if Manager.wait_time <= 0:
            self.update_animation()
            self.update_physics()
            self.update_collision()
            self.update_events()
        else:
            Manager.wait_time -= 1
        ## THIS IS THE END OF THE UPDATES FOR SPEED AND GRAVITY ##

        for e in self.elements:
            e.draw()
        self.canvas.update()

    ## ^ THE ABOVE FUNCTION RUNS EVERYTHING ^ ##

    def update_physics(self):
        for e in self.elements:
            if e.physics_true:
                e.update_physics()

    def update_animation(self):
        for e in self.elements:
            e.update_animation()

    def update_collision(self):
        for e in self.elements:
            e.update_collision()

    def update_events(self):
        for e in self.elements:
            e.update_events()

