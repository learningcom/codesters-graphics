from Tkinter import *
import sprite
import transformations

class Circle(sprite.SpriteClass):
    def __init__(self):
        super(Circle, self).__init__('', shape='circle')

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            self.canvas.create_polygon(tuple(transformations.poly_oval(offsetx + self.xcor - self.width/2,
                                                                       offsety - self.ycor - self.height/2,
                                                                       offsetx + self.xcor + self.width/2,
                                                                       offsety - self.ycor +self.height/2,
                                                                       rotation=self.heading)), fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])

class Rectangle(sprite.SpriteClass):
    def __init__(self, width, height):
        super(Rectangle, self).__init__('', shape='rectangle')
        self.width = width
        self.height = height

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            self.canvas.create_polygon(tuple(transformations.poly_rect(offsetx + self.xcor,
                                                                       offsety - self.ycor,
                                                                       self.width,
                                                                       self.height,
                                                                       self.heading)), fill = self.color)