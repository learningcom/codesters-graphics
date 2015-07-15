from Tkinter import *

class Manager(object):
    root = Tk()
    canvas = Canvas(root, width=500, height=500)
    elements = []

    def run(self):
        self.canvas.delete("all")
        ## THIS IS WHERE THE CHECKS FOR GRAVITY AND SPEED WOULD GO ##
        self.update_animation()
        self.update_physics()
        ## THIS IS THE END OF THE UPDATES FOR SPEED AND GRAVITY ##
        for e in self.elements:
            e.draw()
        self.canvas.update()

    def update_physics(self):
        for e in self.elements:
            if e.physics_true:
                e.update_physics()

    def update_animation(self):
        for e in self.elements:
            e.update_animation()
