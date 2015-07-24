from Tkinter import *
import sprite
import transformations
import math
import bezier


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
            self.canvas.create_polygon(transformations.poly_circle(xc, yc, self.size*self.diam/2),
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
            self.canvas.create_polygon(transformations.poly_rect(xc, yc, self.width*self.size, self.height*self.size, self.heading),
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
            self.canvas.create_polygon(transformations.poly_rect(xc, yc, self.size*self.width, self.size*self.height, self.heading),
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
            y1 = -self.side*self.size/math.sqrt(3) + cy
            x2 = math.cos(210 * math.pi / 180) * self.side*self.size/math.sqrt(3) + cx
            y2 = math.sin(210 * math.pi / 180) * -self.side*self.size/math.sqrt(3) + cy
            x3 = math.cos(330 * math.pi / 180) * self.side*self.size/math.sqrt(3) + cx
            y3 = math.sin(330 * math.pi / 180) * -self.side*self.size/math.sqrt(3) + cy

            points = [x1,y1,x2,y2,x3,y3]
            self.canvas.create_polygon(transformations.poly_poly(cx, cy, points, self.heading), fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])


class Ellipse(sprite.SpriteClass):
    def __init__(self, x, y, width, height, color):
        super(Ellipse, self).__init__('', shape='ellipse')
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
            self.canvas.create_polygon(transformations.poly_oval(offsetx + self.xcor - self.width*self.size/2,
                                                                 offsety - self.ycor - self.height*self.size/2,
                                                                 offsetx + self.xcor + self.width*self.size/2,
                                                                 offsety - self.ycor +self.height*self.size/2,
                                                                 rotation=self.heading),
                                        fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])


class Line(sprite.SpriteClass):
    def __init__(self, x1, y1, x2, y2, color):
        super(Line, self).__init__('', shape='line')
        self.xcor = (x2 - x1)/2 + x1
        self.ycor = (y2 - y1)/2 + y1
        self.width = x2 - x1
        self.height = y2 - y1
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            points = transformations.poly_line(xc, yc, self.width*self.size, self.height*self.size,self.heading)
            #print points
            self.canvas.create_line(points[0],points[1],points[2],points[3],
                                       fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])

class Star(sprite.SpriteClass):
    def __init__(self, x, y, num_points, diam, color):
        super(Star, self).__init__('', shape='star')
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.num_points = num_points
        self.width = diam
        self.height = diam
        self.color = color

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            self.canvas.create_polygon(transformations.poly_star(xc, yc, self.size*self.width, self.size*self.height, self.num_points, self.heading),
                                       fill=self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])

class TriangleIso(sprite.SpriteClass):
    def __init__(self, x, y, width, height, color):
        super(TriangleIso, self).__init__('', shape='triangleiso')
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            cx = offsetx + self.xcor
            cy = offsety - self.ycor

            x1 = cx
            y1 = cy - self.size*self.height/2
            x2 = cx - self.size*self.width/2
            y2 = cy + self.size*self.height/2
            x3 = cx + self.size*self.width/2
            y3 = cy + self.size*self.height/2

            points = [x1,y1,x2,y2,x3,y3]
            self.canvas.create_polygon(transformations.poly_poly(cx, cy, points, self.heading), fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])

class TriangleRight(sprite.SpriteClass):
    def __init__(self, x, y, width, height, color):
        super(TriangleRight, self).__init__('', shape='triangleright')
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            cx = offsetx + self.xcor
            cy = offsety - self.ycor

            x1 = cx - self.size*self.width/2
            y1 = cy + self.size*self.height/2
            x2 = cx + self.size*self.width/2
            y2 = cy + self.size*self.height/2
            x3 = cx - self.size*self.width/2
            y3 = cy - self.size*self.height/2

            points = [x1,y1,x2,y2,x3,y3]
            self.canvas.create_polygon(transformations.poly_poly(cx, cy, points, self.heading), fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])

class Triangle3Pts(sprite.SpriteClass):
    def __init__(self, x1, y1, x2, y2, x3, y3, color):
        super(Triangle3Pts, self).__init__('', shape='triangle3pts')
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

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            cx = self.xcor
            cy = self.ycor

            points = [self.xcor-self.x1,self.ycor-self.y1,self.xcor-self.x2,self.ycor-self.y2,self.xcor-self.x3,self.ycor-self.y3]
            point_tuple = transformations.poly_poly(cx,cy,points,-self.heading)
            points[0] = offsetx + self.size*point_tuple[0]
            points[1] = offsety - self.size*point_tuple[1]
            points[2] = offsetx + self.size*point_tuple[2]
            points[3] = offsety - self.size*point_tuple[3]
            points[4] = offsetx + self.size*point_tuple[4]
            points[5] = offsety - self.size*point_tuple[5]
            self.canvas.create_polygon(tuple(points), fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])


class Quad(sprite.SpriteClass):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, color):
        super(Quad, self).__init__('', shape='quad')
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

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            cx = self.xcor
            cy = self.ycor

            points = [self.xcor-self.x1,self.ycor-self.y1,
                      self.xcor-self.x2,self.ycor-self.y2,
                      self.xcor-self.x3,self.ycor-self.y3,
                      self.xcor-self.x4,self.ycor-self.y4]
            point_tuple = transformations.poly_poly(cx,cy,points,-self.heading)
            points[0] = offsetx + self.size*point_tuple[0]
            points[1] = offsety - self.size*point_tuple[1]
            points[2] = offsetx + self.size*point_tuple[2]
            points[3] = offsety - self.size*point_tuple[3]
            points[4] = offsetx + self.size*point_tuple[4]
            points[5] = offsety - self.size*point_tuple[5]
            points[6] = offsetx + self.size*point_tuple[6]
            points[7] = offsety - self.size*point_tuple[7]
            self.canvas.create_polygon(tuple(points), fill=self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])


class Polygon(sprite.SpriteClass):
    def __init__(self, x, y, num_points, diam, color):
        super(Polygon, self).__init__('', shape='polygon')
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.num_points = num_points
        self.width = diam
        self.height = diam
        self.color = color

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            xc = offsetx + self.xcor
            yc = offsety - self.ycor
            points = [xc - self.width*self.size/2, yc-self.height*self.size/2, xc + self.width*self.size/2, yc + self.size*self.height/2]
            self.canvas.create_polygon(transformations.poly_oval(points[0],points[1],points[2],points[3],
                                                                 steps = self.num_points,
                                                                 rotation = self.heading),
                                       fill=self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])


class Arc(sprite.SpriteClass):
    def __init__(self, x, y, diam, start, end, color):
        super(Arc, self).__init__('', shape='arc')
        self.width = diam
        self.height = diam
        self.xcor = x
        self.ycor = y
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.color = color
        self.start_angle = start
        self.end_angle = end

    def draw(self):
        if not self.hidden:
            offsetx = self.canvas.winfo_reqwidth()/2
            offsety = self.canvas.winfo_reqheight()/2
            self.canvas.create_polygon(transformations.poly_arc(offsetx + self.xcor - self.width*self.size/2,
                                                                 offsety - self.ycor - self.height*self.size/2,
                                                                 offsetx + self.xcor + self.width*self.size/2,
                                                                 offsety - self.ycor +self.height*self.size/2,
                                                                 self.start_angle, self.end_angle,
                                                                 rotation=self.heading),
                                        fill = self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill = p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill = l[1], width = l[2])

class Curve(sprite.SpriteClass):
    def __init__(self, x1, y1, cx1, cy1, cx2, cy2, x2, y2, fill, color):
        super(Curve, self).__init__('', shape='curve')
        offsetx = self.canvas.winfo_reqwidth()/2
        offsety = self.canvas.winfo_reqheight()/2
        self.xcor = (x1+x2)/2
        self.ycor = (y1+y2)/2
        cx = offsetx + self.xcor
        cy = offsety - self.ycor
        self.x1,self.cx1,self.cx2,self.x2 = x1,cx1,cx2,x2
        self.y1,self.cy1,self.cy2,self.y2 = y1,cy1,cy2,y2
        self.P0 = [cx + x1, cy - y1]
        self.P1 = [cx + cx1, cy - cy1]
        self.P2 = [cx + cx2, cy - cy2]
        self.P3 = [cx + x2, cy - y2]
        self.color = color

    def draw(self):
        offsetx = self.canvas.winfo_reqwidth()/2
        offsety = self.canvas.winfo_reqheight()/2
        cx = offsetx + self.xcor
        cy = offsety - self.ycor

        x1,cx1,cx2,x2 = cx+self.x1, cx+self.cx1, cx+self.cx2, cx+self.x2
        y1,cy1,cy2,y2 = cy-self.y1, cy-self.cy1, cy-self.cy2, cy-self.y2

        theta = -self.heading * math.pi/180

        newx1 = (math.cos(theta) * (x1-cx) - math.sin(theta) * (y1-cy))*self.size + cx
        newy1 = (math.sin(theta) * (x1-cx) + math.cos(theta) * (y1-cy))*self.size + cy
        newcx1 = (math.cos(theta) * (cx1-cx) - math.sin(theta) * (cy1-cy))*self.size + cx
        newcy1 = (math.sin(theta) * (cx1-cx) + math.cos(theta) * (cy1-cy))*self.size + cy
        newcx2 = (math.cos(theta) * (cx2-cx) - math.sin(theta) * (cy2-cy))*self.size + cx
        newcy2 = (math.sin(theta) * (cx2-cx) + math.cos(theta) * (cy2-cy))*self.size + cy
        newx2 = (math.cos(theta) * (x2-cx) - math.sin(theta) * (y2-cy))*self.size + cx
        newy2 = (math.sin(theta) * (x2-cx) + math.cos(theta) * (y2-cy))*self.size + cy

        self.P0 = [newx1,newy1]
        self.P1 = [newcx1,newcy1]
        self.P2 = [newcx2,newcy2]
        self.P3 = [newx2,newy2]

        b = bezier.Bezier()
        points = b.draw_cubic_bez(self.P0,self.P1,self.P2,self.P3)
        for i in range(len(points) - 1):
            pointuple = tuple([points[i][0],points[i][1],points[i+1][0],points[i+1][1]])
            self.canvas.create_line(pointuple, fill = self.color)