from Tkinter import *
import sprite
import transformations
import math


class Point(sprite.SpriteClass):
    def __init__(self,x,y):
        super(Point, self).__init__('', shape = 'point')
        self.size = 5
        self.width = 5
        self.height = 5

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            self.canvas.create_oval(offsetx + self.xcor - 5, offsety - self.ycor - 5, offsetx + self.xcor + 5, offsety - self.ycor + 5, fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])


class Circle(sprite.SpriteClass):
    def __init__(self, x, y, size, color):
        super(Circle, self).__init__('', shape='circle')
        self.size = size
        self.width = size
        self.height = size
        self.xcor = x
        self.ycor = y
        self.color = color

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            self.canvas.create_polygon(transformations.poly_oval(offsetx + self.xcor - self.width/2,
                                                                 offsety - self.ycor - self.height/2,
                                                                 offsetx + self.xcor + self.width/2,
                                                                 offsety - self.ycor +self.height/2,
                                                                 rotation=self.heading),
                                        fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])


class Rectangle(sprite.SpriteClass):
    def __init__(self, x, y, width, height, color):
        super(Rectangle, self).__init__('', shape='rectangle')
        self.width = width
        self.height = height
        self.xcor = x
        self.ycor = y
        self.color = color

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            x1 = xc - self.width/2
            y1 = yc - self.height/2
            x2 = xc + self.width/2
            y2 = yc - self.height/2
            x3 = xc + self.width/2
            y3 = yc + self.height/2
            x4 = xc - self.width/2
            y4 = yc + self.height/2
            points = [x1,y1,x2,y2,x3,y3,x4,y4]
            self.canvas.create_polygon(transformations.poly_poly(xc, yc, points, self.heading),
                                       fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])


class Triangle(sprite.SpriteClass):
    def __init__(self, x, y, side, color):
        super(Triangle, self).__init__('', shape='triangle')
        self.xcor = x
        self.ycor = y
        self.side = side
        self.color = color

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            cx = offsetx + self.xcor
            cy = offsety - self.ycor

            x1 = math.cos((90 + self.heading) * math.pi / 180) * self.side/math.sqrt(3) + cx
            y1 = math.sin((90 + self.heading) * math.pi / 180) * -self.side/math.sqrt(3) + cy
            x2 = math.cos((210 + self.heading) * math.pi / 180) * self.side/math.sqrt(3) + cx
            y2 = math.sin((210 + self.heading) * math.pi / 180) * -self.side/math.sqrt(3) + cy
            x3 = math.cos((330 + self.heading) * math.pi / 180) * self.side/math.sqrt(3) + cx
            y3 = math.sin((330 + self.heading) * math.pi / 180) * -self.side/math.sqrt(3) + cy

            points = [x1,y1,x2,y2,x3,y3]
            self.canvas.create_polygon(tuple(points), fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])
