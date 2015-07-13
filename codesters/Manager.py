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
                    # print e.animation_x_coords
                    # print e.animation_y_coords
                if (abs(e.future_heading - e.heading) >.1) :
                    print e.future_heading-e.heading
                    im2 = e.photo.convert('RGBA')
                    e.photo.close()
                    rot = im2.rotate(e.step_size, expand=1)
                    fff = Image.new("RGBA", rot.size, (0,)*4)
                    e.photo = Image.composite(rot,fff,rot)
                    e.photo.save("check.gif")
                    rot.close()
                    fff.close()
                    im2.close()
                    e.heading += e.step_size