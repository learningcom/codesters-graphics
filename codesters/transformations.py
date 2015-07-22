import math

def poly_oval(x0,y0, x1,y1, steps=50, rotation=0):
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

    return point_list

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

    print [x1,y1,x2,y2,x3,y3,x4,y4]

    x1 = math.cos(theta) * (x1-x) - math.sin(theta) * (y1-y) + x
    y1 = math.sin(theta) * (x1-x) + math.cos(theta) * (y1-y) + y
    x2 = math.cos(theta) * (x2-x) - math.sin(theta) * (y2-y) + x
    y2 = math.sin(theta) * (x2-x) + math.cos(theta) * (y2-y) + y
    x3 = math.cos(theta) * (x3-x) - math.sin(theta) * (y3-y) + x
    y3 = math.sin(theta) * (x3-x) + math.cos(theta) * (y3-y) + y
    x4 = math.cos(theta) * (x4-x) - math.sin(theta) * (y4-y) + x
    y4 = math.sin(theta) * (x4-x) + math.cos(theta) * (y4-y) + y

    point_list = [x1,y1,x2,y2,x3,y3,x4,y4]
    print point_list
    print '"""""""""""""""""""""""""""""""""""""""""""""""""'
    return point_list