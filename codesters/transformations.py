import math


def poly_circle(x, y, r):
    step = math.pi/25
    point_list = []

    for i in range(50):
        newx = math.cos(step * i) * r + x
        newy = math.sin(step * i) * r + y
        point_list.append(newx)
        point_list.append(newy)

    return tuple(point_list)


def poly_oval(x0, y0, x1, y1, steps=20, rotation=0):
    rotation = rotation * math.pi / 180.0
    cos_rot = math.cos(rotation)
    sin_rot = math.sin(rotation)

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
        x = (x1 * cos_rot) + (y1 * sin_rot)
        y = (y1 * cos_rot) - (x1 * sin_rot)

        point_list.append(round(x + xc))
        point_list.append(round(y + yc))

    return tuple(point_list)


def poly_rect(x, y, width, height, rotation):
    x1 = x-width/2
    y1 = y-height/2
    x2 = x+width/2
    y2 = y+height/2

    point_list = [x1, y1, x2, y1, x2, y2, x1, y2]
    return poly_poly(x, y, point_list, rotation)


def poly_line(x, y, width, height, rotation):
    x1 = x-width/2
    y1 = y-height/2
    x2 = x+width/2
    y2 = y+height/2

    points = poly_poly(x, y, [x1, y1, x2, y2], rotation)
    point_list = [points[0], points[1], points[2], points[3]]

    return point_list


def poly_poly(cx, cy, points, rotation):
    theta = -rotation*math.pi / 180
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    point_list = []

    for i in range(len(points)/2):
        x = points[i*2] - cx
        y = points[i*2 + 1] - cy

        x1 = cos_theta * x - sin_theta * y
        y1 = sin_theta * x + cos_theta * y
        x1 += cx
        y1 += cy

        point_list.append(x1)
        point_list.append(y1)

    return tuple(point_list)


def poly_star(x, y, width, height, num_points, rotation):
    rotation = rotation * math.pi / 180.0
    cos_rot = math.cos(rotation)
    sin_rot = math.sin(rotation)

    a = width/2
    b = height/2

    point_list = []

    # create the oval as a list of points
    for i in range(num_points):

        theta = (math.pi * 2) * (float(i) / num_points)

        x1 = a * math.cos(theta)
        y1 = b * math.sin(theta)

        x2 = (x1 * cos_rot) + (y1 * sin_rot)
        y2 = (y1 * cos_rot) - (x1 * sin_rot)

        point_list.append(round(x2 + x))
        point_list.append(round(y2 + y))

        theta = (math.pi * 2) * ((float(i) + 0.5) / num_points)

        x1 = a * math.cos(theta)/2
        y1 = b * math.sin(theta)/2

        x2 = (x1 * cos_rot) + (y1 * sin_rot)
        y2 = (y1 * cos_rot) - (x1 * sin_rot)

        point_list.append(round(x2 + x))
        point_list.append(round(y2 + y))

    return tuple(point_list)


def poly_arc(x0, y0, x1, y1, start, end, steps=90, rotation=0):
    rotation = rotation * math.pi / 180.0
    cos_rot = math.cos(rotation)
    sin_rot = math.sin(rotation)

    # major and minor axes
    a = (x1 - x0) / 2.0
    b = (y1 - y0) / 2.0

    # center
    xc = x0 + a
    yc = y0 + b

    point_list = [(x1-x0)/2 + x0, (y1-y0)/2 + y0]

    # create the oval as a list of points
    for i in range(steps):

        # Calculate the angle for this step
        # 360 degrees == 2 pi radians
        theta = ((start-end) * (math.pi * 2) * (float(i) / steps) / 360) - start*math.pi/180

        x1 = a * math.cos(theta)
        y1 = b * math.sin(theta)

        # rotate x, y
        x = (x1 * cos_rot) + (y1 * sin_rot)
        y = (y1 * cos_rot) - (x1 * sin_rot)

        point_list.append(round(x + xc))
        point_list.append(round(y + yc))

    return tuple(point_list)