from Tkinter import *

class ManagerClass:
    def __init__(self, canvas, Elements):
        self.canvas = canvas
        self.Elements = Elements

    def run(self):
        self.canvas.delete("all")
        ## THIS IS WHERE THE CHECKS FOR GRAVITY AND SPEED WOULD GO ##


        print "here"
        ## THIS IS THE END OF THE UPDATES FOR SPEED AND GRAVITY ##
        for e in self.Elements:
            e.draw()
        self.canvas.update()
