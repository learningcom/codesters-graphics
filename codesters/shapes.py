from Tkinter import Tk, Canvas
import sprite
import transformations
import math
import bezier
from .hitbox import Hitbox
import inspect
import re


class Point(sprite.SpriteClass):
    def __init__(self, x=0, y=0, size=5, color='black', outline=None):
        super(Point, self).__init__('', x, y, shape='point')
        self.width = size
        self.height = size
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            self.canvas.create_oval(xc - self.width/2, yc - self.height/2, xc + self.width/2, yc + self.height/2,
                                    fill=self.color, outline=self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Circle(sprite.SpriteClass):
    def __init__(self, x=0, y=0, diam=20, color='black', outline=None):
        super(Circle, self).__init__('', x, y,  shape='circle')
        self.diam = diam
        self.width = diam
        self.height = diam
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            self.canvas.create_polygon(transformations.poly_circle(xc, yc, self.size*self.diam/2),
                                       fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Rectangle(sprite.SpriteClass):
    def __init__(self, x=0, y=0, width=100, height=50, color='black', outline=None):
        super(Rectangle, self).__init__('', x, y, shape='rectangle')
        self.width = width
        self.height = height
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1
            self.canvas.create_polygon(transformations.poly_rect(xc, yc,
                                                                 xf*self.width*self.size,
                                                                 yf*self.height*self.size,
                                                                 self.heading),
                                       fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Square(sprite.SpriteClass):
    def __init__(self, x=0, y=0, side=50, color='black', outline=None):
        super(Square, self).__init__('', x, y, shape='square')
        self.width = side
        self.height = side
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1
            self.canvas.create_polygon(transformations.poly_rect(xc, yc,
                                                                 xf*self.size*self.width,
                                                                 yf*self.size*self.height,
                                                                 self.heading),
                                       fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Triangle(sprite.SpriteClass):
    def __init__(self, x=0, y=0, side=50, color='black', outline=None):
        super(Triangle, self).__init__('', x, y, shape='triangle')
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.side = side
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            cx = offsetx + self.xcor
            cy = offsety - self.ycor
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1

            x1 = cx
            y1 = -yf*self.side*self.size/math.sqrt(3) + cy
            x2 = math.cos(210 * math.pi / 180) * xf*self.side*self.size/math.sqrt(3) + cx
            y2 = math.sin(210 * math.pi / 180) * -yf*self.side*self.size/math.sqrt(3) + cy
            x3 = math.cos(330 * math.pi / 180) * xf*self.side*self.size/math.sqrt(3) + cx
            y3 = math.sin(330 * math.pi / 180) * -yf*self.side*self.size/math.sqrt(3) + cy

            points = [x1, y1, x2, y2, x3, y3]
            self.canvas.create_polygon(transformations.poly_poly(cx, cy, points, self.heading),
                                       fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Ellipse(sprite.SpriteClass):
    def __init__(self, x=0, y=0, width=100, height=50, color='black', outline=None):
        super(Ellipse, self).__init__('', x, y, shape='ellipse')
        self.width = width
        self.height = height
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1
            self.canvas.create_polygon(transformations.poly_oval(offsetx + self.xcor - xf * self.width * self.size / 2,
                                                                 offsety - self.ycor - yf * self.height * self.size / 2,
                                                                 offsetx + self.xcor + xf * self.width * self.size / 2,
                                                                 offsety - self.ycor + yf * self.height * self.size / 2,
                                                                 rotation=self.heading),
                                       fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Line(sprite.SpriteClass):
    def __init__(self, x1=0, y1=0, x2=100, y2=100, color='black'):
        super(Line, self).__init__('', x1, y1, shape='line')
        self.xcor = (x2 - x1)/2 + x1
        self.ycor = (y2 - y1)/2 + y1
        self.width = x2 - x1
        self.height = y2 - y1
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1
            points = transformations.poly_line(xc, yc, xf*self.width*self.size, yf*self.height*self.size, self.heading)
            self.canvas.create_line(points[0], points[1], points[2], points[3],
                                    fill=self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Star(sprite.SpriteClass):
    def __init__(self, x=0, y=0, num_points=5, diam=50, color='black', outline=None):
        super(Star, self).__init__('', x, y, shape='star')
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.num_points = num_points
        self.width = diam
        self.height = diam
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1
            self.canvas.create_polygon(transformations.poly_star(xc, yc,
                                                                 xf*self.size*self.width,
                                                                 yf*self.size*self.height,
                                                                 self.num_points,
                                                                 self.heading),
                                       fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class TriangleIso(sprite.SpriteClass):
    def __init__(self, x=0, y=0, width=100, height=50, color='black', outline=None):
        super(TriangleIso, self).__init__('', x, y, shape='triangleiso')
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.width = width
        self.height = height
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            cx = offsetx + self.xcor
            cy = offsety - self.ycor
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1

            x1 = cx
            y1 = cy - yf*self.size*self.height/2
            x2 = cx - xf*self.size*self.width/2
            y2 = cy + yf*self.size*self.height/2
            x3 = cx + xf*self.size*self.width/2
            y3 = cy + yf*self.size*self.height/2

            points = [x1, y1, x2, y2, x3, y3]
            self.canvas.create_polygon(transformations.poly_poly(cx, cy, points, self.heading),
                                       fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class TriangleRight(sprite.SpriteClass):
    def __init__(self, x=0, y=0, width=50, height=50, color='black', outline=None):
        super(TriangleRight, self).__init__('', x, y, shape='triangleright')
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.width = width
        self.height = height
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            cx = offsetx + self.xcor
            cy = offsety - self.ycor
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1

            x1 = cx - xf*self.size*self.width/2
            y1 = cy + yf*self.size*self.height/2
            x2 = cx + xf*self.size*self.width/2
            y2 = cy + yf*self.size*self.height/2
            x3 = cx - xf*self.size*self.width/2
            y3 = cy - yf*self.size*self.height/2

            points = [x1, y1, x2, y2, x3, y3]
            self.canvas.create_polygon(transformations.poly_poly(cx, cy, points, self.heading),
                                       fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Triangle3Pts(sprite.SpriteClass):
    def __init__(self, x1=-50, y1=-50, x2=50, y2=-50, x3=0, y3=50, color='black', outline=None):
        x = (x1 + x2 + x3)/3
        y = (y1 + y2 + y3)/3
        super(Triangle3Pts, self).__init__('', x, y, shape='triangle3pts')
        self.xcor = (x1 + x2 + x3)/3
        self.ycor = (y1 + y2 + y3)/3

        self.x1 = self.xcor-x1
        self.x2 = self.xcor-x2
        self.x3 = self.xcor-x3
        self.y1 = self.ycor-y1
        self.y2 = self.ycor-y2
        self.y3 = self.ycor-y3

        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            cx = self.xcor
            cy = self.ycor
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1

            points = [self.xcor-xf*self.x1, self.ycor-yf*self.y1,
                      self.xcor-xf*self.x2, self.ycor-yf*self.y2,
                      self.xcor-xf*self.x3, self.ycor-yf*self.y3]
            point_tuple = transformations.poly_poly(cx, cy, points, -self.heading)
            points[0] = offsetx + self.size*point_tuple[0]
            points[1] = offsety - self.size*point_tuple[1]
            points[2] = offsetx + self.size*point_tuple[2]
            points[3] = offsety - self.size*point_tuple[3]
            points[4] = offsetx + self.size*point_tuple[4]
            points[5] = offsety - self.size*point_tuple[5]
            self.canvas.create_polygon(tuple(points), fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Quad(sprite.SpriteClass):
    def __init__(self, x1=-50, y1=-50, x2=50, y2=-50, x3=50, y3=50, x4=-50, y4=50, color='black', outline=None):
        x = (x1 + x2 + x3 + x4)/4
        y = (y1 + y2 + y3 + x4)/4
        super(Quad, self).__init__('', x, y, shape='quad')
        self.xcor = (x1 + x2 + x3 + x4)/4
        self.ycor = (y1 + y2 + y3 + x4)/4

        self.x1 = self.xcor-x1
        self.x2 = self.xcor-x2
        self.x3 = self.xcor-x3
        self.x4 = self.xcor-x4
        self.y1 = self.ycor-y1
        self.y2 = self.ycor-y2
        self.y3 = self.ycor-y3
        self.y4 = self.ycor-y4

        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            cx = self.xcor
            cy = self.ycor
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1

            points = [self.xcor-xf*self.x1, self.ycor-yf*self.y1,
                      self.xcor-xf*self.x2, self.ycor-yf*self.y2,
                      self.xcor-xf*self.x3, self.ycor-yf*self.y3,
                      self.xcor-xf*self.x4, self.ycor-yf*self.y4]
            point_tuple = transformations.poly_poly(cx, cy, points, -self.heading)
            points[0] = offsetx + self.size*point_tuple[0]
            points[1] = offsety - self.size*point_tuple[1]
            points[2] = offsetx + self.size*point_tuple[2]
            points[3] = offsety - self.size*point_tuple[3]
            points[4] = offsetx + self.size*point_tuple[4]
            points[5] = offsety - self.size*point_tuple[5]
            points[6] = offsetx + self.size*point_tuple[6]
            points[7] = offsety - self.size*point_tuple[7]
            self.canvas.create_polygon(tuple(points), fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Polygon(sprite.SpriteClass):
    def __init__(self, x=0, y=0, num_points=6, diam=100, color='black', outline=None):
        super(Polygon, self).__init__('', x, y, shape='polygon')
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.num_points = num_points
        self.width = diam
        self.height = diam
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1
            points = [xc - xf*self.width*self.size/2,
                      yc-yf*self.height*self.size/2,
                      xc + xf*self.width*self.size/2,
                      yc + yf*self.size*self.height/2]
            self.canvas.create_polygon(transformations.poly_oval(points[0], points[1], points[2], points[3],
                                                                 steps=self.num_points,
                                                                 rotation=self.heading),
                                       fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Arc(sprite.SpriteClass):
    def __init__(self, x=0, y=0, diam=50, start=0, end=270, color='black', outline=None):
        super(Arc, self).__init__('', x, y, shape='arc')
        self.width = diam
        self.height = diam
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color
        self.outline = outline
        if self.color is None:
            self.color = ''
        if self.outline is None:
            self.outline = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

        self.start_angle = start
        self.end_angle = end

        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xf = 1
            yf = 1
            if self.x_flipped:
                xf = -1
            if self.y_flipped:
                yf = -1
            self.canvas.create_polygon(transformations.poly_arc(offsetx + self.xcor - xf*self.width*self.size/2,
                                                                offsety - self.ycor - yf*self.height*self.size/2,
                                                                offsetx + self.xcor + xf*self.width*self.size/2,
                                                                offsety - self.ycor + yf*self.height*self.size/2,
                                                                self.start_angle, self.end_angle,
                                                                rotation=self.heading),
                                       fill=self.color, outline=self.outline)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Curve(sprite.SpriteClass):
    def __init__(self, x1=0, y1=0, cx1=0, cy1=100, cx2=0, cy2=100, x2=100, y2=100, fill='black', color='black'):
        super(Curve, self).__init__('', x1, y1, shape='curve')
        offsetx = self.canvas.winfo_reqwidth()/2
        offsety = self.canvas.winfo_reqheight()/2
        self.xcor = (x1+x2)/2
        self.ycor = (y1+y2)/2
        cx = offsetx + self.xcor
        cy = offsety - self.ycor
        self.x1, self.cx1, self.cx2, self.x2 = x1, cx1, cx2, x2
        self.y1, self.cy1, self.cy2, self.y2 = y1, cy1, cy2, y2
        self.P0 = [cx + x1, cy - y1]
        self.P1 = [cx + cx1, cy - cy1]
        self.P2 = [cx + cx2, cy - cy2]
        self.P3 = [cx + x2, cy - y2]
        self.color = color

        self.pen_color_var = self.color
        self.fill_color_var = self.pen_color_var

    def draw(self):
        offsetx = self.canvas.winfo_reqwidth()/2
        offsety = self.canvas.winfo_reqheight()/2
        cx = offsetx + self.xcor
        cy = offsety - self.ycor
        xf = 1
        yf = 1
        if self.x_flipped:
            xf = -1
        if self.y_flipped:
            yf = -1

        x1, cx1, cx2, x2 = cx+self.x1, cx+self.cx1, cx+self.cx2, cx+self.x2
        y1, cy1, cy2, y2 = cy-self.y1, cy-self.cy1, cy-self.cy2, cy-self.y2

        theta = -self.heading * math.pi/180
        costhe = math.cos(theta)
        sinthe = math.sin(theta)

        newx1 = (costhe * (x1-cx) - sinthe * (y1-cy))*self.size*xf + cx
        newy1 = (sinthe * (x1-cx) + costhe * (y1-cy))*self.size*yf + cy
        newcx1 = (costhe * (cx1-cx) - sinthe * (cy1-cy))*self.size*xf + cx
        newcy1 = (sinthe * (cx1-cx) + costhe * (cy1-cy))*self.size*yf + cy
        newcx2 = (costhe * (cx2-cx) - sinthe * (cy2-cy))*self.size*xf + cx
        newcy2 = (sinthe * (cx2-cx) + costhe * (cy2-cy))*self.size*yf + cy
        newx2 = (costhe * (x2-cx) - sinthe * (y2-cy))*self.size*xf + cx
        newy2 = (sinthe * (x2-cx) + costhe * (y2-cy))*self.size*yf + cy

        self.P0 = [newx1, newy1]
        self.P1 = [newcx1, newcy1]
        self.P2 = [newcx2, newcy2]
        self.P3 = [newx2, newy2]

        b = bezier.Bezier()
        points = b.draw_cubic_bez(self.P0, self.P1, self.P2, self.P3)
        for i in range(len(points) - 1):
            pointuple = tuple([points[i][0], points[i][1], points[i+1][0], points[i+1][1]])
            self.canvas.create_line(pointuple, fill=self.color)

        if self.forever_function is not None:
            self.forever_function()

        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])

        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor - 100,
                                    text=self.say_text,
                                    font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1


class Text(sprite.SpriteClass):
    def __init__(self, text, x=0, y=0, color="black"):
        super(Text, self).__init__('', x, y, shape='text')
        self.say_text = text
        self.say_time = 10000000
        self.say_color = color
        self.say_size = 12
        self.say_font = "Helvetica"
        self.xcor = x
        self.ycor = y
        self.hidden = True
        self.gravity_off()
        self.collision_off()
        self.drag = False

    def set_text(self, text):
        self.say_text = text

    def say(self):
        pass

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if not self.hidden:
            self.canvas.create_oval((self.xcor-(self.size/2),
                                     self.ycor-(self.size/2),
                                     self.xcor+(self.size/2),
                                     self.ycor+(self.size/2)),
                                    fill=self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + self.canvas.winfo_reqwidth()/2,
                                    self.canvas.winfo_reqheight()/2 - self.ycor,
                                    text=self.say_text, font=(self.say_font, self.say_size),
                                    fill=self.say_color)


class Display(sprite.SpriteClass):
    def __init__(self, var, x=-200, y=200):
        super(Display, self).__init__('', x, y, shape="display")

        frame = inspect.currentframe()
        try:
            context = inspect.getframeinfo(frame.f_back).code_context
            caller_lines = ''.join([line.strip() for line in context])
            m = re.search(r'echo\s*\((.+?)\)$', caller_lines)
            if m:
                caller_lines = m.group(1)
            self.s = caller_lines, var
        finally:
            del frame

        self.s_split1 = self.s[0].split('(')
        self.s_split2 = self.s_split1[1].split(')')
        self.var_text = self.s_split2[0]
        self.display_var = self.s[1]

        self.physics_off()

    def update(self, var):
        frame = inspect.currentframe()
        try:
            context = inspect.getframeinfo(frame.f_back).code_context
            caller_lines = ''.join([line.strip() for line in context])
            m = re.search(r'echo\s*\((.+?)\)$', caller_lines)
            if m:
                caller_lines = m.group(1)
            self.s = caller_lines, var
        finally:
            del frame

        self.s_split1 = self.s[0].split('(')
        self.s_split2 = self.s_split1[1].split(')')
        self.var_text = self.s_split2[0]
        self.display_var = self.s[1]

    def draw(self):
        offX = self.xcor + self.canvas.winfo_reqwidth()/2
        offY = self.canvas.winfo_reqheight()/2 - self.ycor
        self.canvas.create_rectangle(offX-25, offY-25, offX+25, offY+25,
                                     fill='#000066', outline='#FFFFFF')
        self.canvas.create_text(offX, offY - 10, text=self.var_text, fill='#FF8800')
        self.canvas.create_text(offX, offY + 10, text=self.display_var, fill='#6688FF')
