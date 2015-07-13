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
                if e.wait_time > 0:
                    e.wait_time = e.wait_time - 1
                else:
                    if len(e.animation_y_coords)>0 and len(e.animation_x_coords)>0:
                        e.set_x(e.animation_x_coords.pop(0))
                        e.set_y(e.animation_y_coords.pop(0))
                        if len(e.animation_x_coords)>0:
                            e.future_x = e.animation_x_coords[-1]
                        if len(e.animation_y_coords)>0:
                            e.future_y = e.animation_y_coords[-1]
                    if len(e.animation_rotation_degrees)>0 :
                        e.heading = e.animation_rotation_degrees.pop(0)
                        im2 = e.base_photo.convert('RGBA')
                        #e.base_photo.close()
                        rot = im2.rotate(e.heading, expand=1)
                        fff = Image.new("RGBA", rot.size, (0,)*4)
                        e.photo = Image.composite(rot,fff,rot)
                        e.photo.save("check.gif")
                        rot.close()
                        fff.close()
                        im2.close()
                    # print e.animation_x_coords
                    # print e.animation_y_coords
