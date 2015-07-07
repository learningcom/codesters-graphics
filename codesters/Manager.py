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