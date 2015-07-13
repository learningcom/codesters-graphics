from Tkinter import *
from Environment import *
from Circle import *
from Sprite import *


class ManagerClass:
    def __init__(self, canvas, Elements):
        self.canvas = canvas
        self.Elements = Elements

    def run(self):
        self.canvas.delete("all")
        ## THIS IS WHERE THE CHECKS FOR GRAVITY AND SPEED WOULD GO ##
        self.updateAnimation()
        self.updatePhyiscs()
        ## THIS IS THE END OF THE UPDATES FOR SPEED AND GRAVITY ##
        for e in self.Elements:
            e.draw()
        self.canvas.update()


    def updatePhyiscs(self):
        for e in self.Elements:
            if isinstance(e, SpriteClass):
                e.xcor+=e.xspeed
                e.ycor-=e.yspeed

    def updateAnimation(self):
        for e in self.Elements:
            if isinstance(e, SpriteClass):
                if len(e.animation_y_coords)>0 and len(e.animation_x_coords)>0:
                    e.set_x(e.animation_x_coords.pop(0))
                    e.set_y(e.animation_y_coords.pop(0))
                    if len(e.animation_x_coords)>0:
                        e.future_x = e.animation_x_coords[-1]
                    if len(e.animation_y_coords)>0:
                        e.future_y = e.animation_y_coords[-1]
                    # print e.animation_x_coords
                    # print e.animation_y_coords