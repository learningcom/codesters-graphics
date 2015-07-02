from Tkinter import *

class StageClass:
    #Placeholders
    xcor = 0
    ycor = 0
    size = 1
    bg_image= None
    def __init__(self, canvas, Elements, root):
        #Placeholders
        xcor = 0
        ycor = 0
        size = 1
        self.root=root
        self.canvas = canvas
        self.Elements = Elements
        for e in self.Elements:
            e.draw()
        self.canvas.update()

    def draw(self):
        self.canvas.create_rectangle((0,0,500,500), fill='white')

    def set_background(self, image):
        self.bg_image=PhotoImage(file = "./codesters/sprites/"+image+".gif")
        background_label = Label(self.root, image=self.bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image=self.bg_image
        self.canvas.update()