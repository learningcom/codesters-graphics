from Tkinter import *
import sprite
import transformations
import math


class Point(sprite.SpriteClass):
    def __init__(self,x,y):
        super(Point, self).__init__('', shape = 'point')
        self.width = 5
        self.height = 5
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            self.canvas.create_oval(xc - 5, yc - 5, xc + 5, yc + 5, fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])


class Circle(sprite.SpriteClass):
    def __init__(self, x, y, diam, color):
        super(Circle, self).__init__('', shape='circle')
        self.diam = diam
        self.width = diam
        self.height = diam
        self.xcor = x
        self.ycor = y
        self.color = color
        self.future_x = self.xcor
        self.future_y = self.ycor

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            self.canvas.create_polygon(transformations.poly_circle(xc, yc, self.diam/2),
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
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            self.canvas.create_polygon(transformations.poly_rect(xc, yc, self.width, self.height, self.heading),
                                       fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])


class Square(sprite.SpriteClass):
    def __init__(self, x, y, side, color):
        super(Square, self).__init__('', shape='square')
        self.width = side
        self.height = side
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            self.canvas.create_polygon(transformations.poly_rect(xc, yc, self.width, self.height, self.heading),
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
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.side = side
        self.color = color

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            cx = offsetx + self.xcor
            cy = offsety - self.ycor

            x1 = cx
            y1 = -self.side/math.sqrt(3) + cy
            x2 = math.cos(210 * math.pi / 180) * self.side/math.sqrt(3) + cx
            y2 = math.sin(210 * math.pi / 180) * -self.side/math.sqrt(3) + cy
            x3 = math.cos(330 * math.pi / 180) * self.side/math.sqrt(3) + cx
            y3 = math.sin(330 * math.pi / 180) * -self.side/math.sqrt(3) + cy

            points = [x1,y1,x2,y2,x3,y3]
            self.canvas.create_polygon(transformations.poly_poly(cx, cy, points, self.heading), fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])


class Ellipse(sprite.SpriteClass):
    def __init__(self, x, y, width, height, color):
        super(Ellipse, self).__init__('', shape='circle')
        self.width = width
        self.height = height
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
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