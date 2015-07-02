from Tkinter import *

class StageClass:
    #Placeholders
    xcor = 0
    ycor = 0
    size = 1
    bg_image_name = None
    bg_image = None
    bg_scale_y = 1
    bg_scale_x = 1
    scaled_image = None
    def __init__(self, canvas, Elements, root):
        #Placeholders
        xcor = 0
        ycor = 200
        size = 1
        self.canvas = canvas
        self.Elements = Elements
        for e in self.Elements:
            e.draw()
        self.canvas.update()
        self.xcor = self.canvas.winfo_width()/2
        self.ycor = self.canvas.winfo_height()/2
        self.size = 1
        self.root=root

    def draw(self):
        if self.bg_image != None:
            # background_label = Label(self.root, image=self.bg_image)
            # background_label.place(x=self.xcor, y=self.ycor, relwidth=1, relheight=1)
            # background_label.image=self.bg_image
            #print self.canvas.winfo_width()
            self.scaled_image= self.bg_image.subsample(self.bg_scale_x,self.bg_scale_y)
            self.canvas.create_image(self.xcor, self.ycor, image=self.scaled_image)
        else:
            self.canvas.create_rectangle((0,0,500,500), fill='white')

    def set_background(self, image):
        self.bg_image_name= image
        self.bg_image= PhotoImage(file = "./codesters/sprites/"+image+".gif")

    def set_background_x(self, amount):
        self.xcor=amount+self.canvas.winfo_width()

    def set_background_y(self, amount):
        self.ycor=amount+self.canvas.winfo_height()

    def set_background_scaleX(self, amount):
        amount=1/amount
        amount=int(amount)
        self.bg_scale_x=amount

    def set_background_scaleY(self, amount):
        amount=1/amount
        amount=int(amount)
        self.bg_scale_y=amount
        for e in self.Elements:
            e.draw()
            print e
        self.canvas.update()


