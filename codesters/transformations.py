import math

def poly_circle(x,y,r):
    step = math.pi/25
    point_list = []

    for i in range(50):
        newx = math.cos(step * i) * r + x
        newy = math.sin(step * i) * r + y
        point_list.append(newx)
        point_list.append(newy)

    return tuple(point_list)


def poly_oval(x0,y0, x1,y1, steps=20, rotation=0):
    rotation = rotation * math.pi / 180.0

    # major and minor axes
    a = (x1 - x0) / 2.0
    b = (y1 - y0) / 2.0

    # center
    xc = x0 + a
    yc = y0 + b

    point_list = []

    # create the oval as a list of points
    for i in range(steps):

        # Calculate the angle for this step
        # 360 degrees == 2 pi radians
        theta = (math.pi * 2) * (float(i) / steps)

        x1 = a * math.cos(theta)
        y1 = b * math.sin(theta)

        # rotate x, y
        x = (x1 * math.cos(rotation)) + (y1 * math.sin(rotation))
        y = (y1 * math.cos(rotation)) - (x1 * math.sin(rotation))

        point_list.append(round(x + xc))
        point_list.append(round(y + yc))

    return tuple(point_list)

def poly_rect(x,y, width, height, rotation):
    theta = -rotation*math.pi / 180

    x1 = x-width/2
    y1 = y-height/2
    x2 = x+width/2
    y2 = y-height/2
    x3 = x+width/2
    y3 = y+height/2
    x4 = x-width/2
    y4 = y+height/2

    point_list = [x1,y1,x2,y2,x3,y3,x4,y4]
    return poly_poly(x,y, point_list, rotation)


def poly_line(x,y,width,height,rotation):
    theta = -rotation*math.pi / 180
    x1 = x-width/2
    y1 = y-height/2
    x2 = x+width/2
    y2 = y+height/2

    points = poly_poly(x,y, [x1,y1,x2,y2], rotation)
    point_list = [points[0],points[1],points[2],points[3]]

    return point_list

def poly_poly(cx, cy, points, rotation):
    theta = -rotation*math.pi / 180

    point_list = []

    for i in range(len(points)/2):
        x = points[i*2] - cx
        y = points[i*2 + 1] - cy

        x1 = math.cos(theta) * x - math.sin(theta) * y
        y1 = math.sin(theta) * x + math.cos(theta) * y
        x1 += cx
        y1 += cy

        point_list.append(x1)
        point_list.append(y1)

    return tuple(point_list)

def poly_star(x,y, width,height, num_points, rotation):
    rotation = rotation * math.pi / 180.0

    a = width/2
    b = height/2

    point_list = []

    # create the oval as a list of points
    for i in range(num_points):

        theta = (math.pi * 2) * (float(i) / num_points)

        x1 = a * math.cos(theta)
        y1 = b * math.sin(theta)

        x2 = (x1 * math.cos(rotation)) + (y1 * math.sin(rotation))
        y2 = (y1 * math.cos(rotation)) - (x1 * math.sin(rotation))

        point_list.append(round(x2 + x))
        point_list.append(round(y2 + y))

        theta = (math.pi * 2) * ((float(i) + 0.5) / num_points)

        x1 = a * math.cos(theta)/2
        y1 = b * math.sin(theta)/2

        x2 = (x1 * math.cos(rotation)) + (y1 * math.sin(rotation))
        y2 = (y1 * math.cos(rotation)) - (x1 * math.sin(rotation))

        point_list.append(round(x2 + x))
        point_list.append(round(y2 + y))

    return tuple(point_list)