import codesters
from Tkinter import *
import time



class App(object):

    def __init__(self):
        self.root = codesters.root
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.Elements =[]
        self.stage = self.Stage()
        self.manager = self.Manager()
        self.do()
        self.animate=self.moveOne()
        self.stage.draw()


    def Stage(self):
        self.Elements.append(codesters.StageClass(self.canvas, self.Elements, self.root))
        return self.Elements[-1]
    def Circle(self):
        self.Elements.append(codesters.CircleClass(self.canvas, self.Elements))
        return self.Elements[-1]
    def Sprite(self, image = ''):
        self.Elements.append(codesters.SpriteClass(self.canvas, self.Elements, image = image))
        return self.Elements[-1]
    def Manager(self):
        return codesters.ManagerClass(self.canvas, self.Elements)

    #Making a circle
    # circle = codesters.Sprite()
    # circle.set_x(100)
    # circle.set_y(100)
    # circle.go_to(0,0)
    # circle.set_speed(1)
    #
    # circle.glide_to(100,100)
    def do(self):
        self.stage.set_background("summer")
        #stage.set_background_x(0)
        # self.stage.set_background_scaleX(.25)
        # self.stage.set_background_scaleY(.25)
        self.sprite = self.Sprite("Alien1")
        self.sprite.set_speed(2)
        # self.sprite.move_left(100)
        # self.sprite.move_up(100)
        # self.sprite.glide_to(230,70)
        # self.sprite.set_heading(160)
        # self.sprite.move_forward(200)
        #
        # self.sprite.set_x(0)
        # self.sprite.set_y(100)
        #
        # print self.sprite.future_x
        #
        # def moveToMouse(event):
        #     self.sprite.glide_to(event.x-250, (event.y-250)*-1)
        # self.stage.event_click(moveToMouse)

        self.sprite.turn_left(90)
        self.sprite.wait(2)
        self.sprite.left(270)

        # def checkCors(event):
        #      self.clickedX=self.stage.click_x(event)
        #      self.clickedY=self.stage.click_y(event)
        #      print "x coord: ", self.clickedX, " y coord: ", self.clickedY
        #      self.sprite.go_to(self.clickedX, self.clickedY)
        # self.stage.event_click_up(checkCors)
        # self.manager.updatePhyiscs()
        # print self.Elements
        # #self.sprite.hide()
        # print self.sprite.hidden
        # def spriteCors(event):
        #     self.spriteX=self.sprite.get_x()
        #     self.spriteY=self.sprite.get_y()
        #     self.sprite.show()
        #     self.sprite.set_x_speed(3)
        #     self.sprite.jump(2)
        #     print "x coord: ", self.spriteX, "y coord: ", self.spriteY
        # self.stage.event_key("space", spriteCors)

    def moveOne(self):
        self.manager.run()
        self.animate = self.root.after(22, self.moveOne)

#Workaround; for right now, this like has to be in the program being run, rather than __init__.py as it should.
app = App()
app.root.mainloop()