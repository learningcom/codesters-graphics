import math
import Tkinter

class Bezier(Tkinter.Canvas):
    '''
    Simple and slow algorithm to draw quadratic and
    cubic Bezier curves. Heavily inspired by http://pomax.github.io/bezierinfo/#control
    This code should just prove a concept and is not intended to be
    used in a real world app...
    Author: Nikolai Tschacher
    Date: 07.10.2013
    '''
    # Because Canvas doesn't support simple pixel plotting,
    # we need to help us out with a line with length 1 in
    # positive x direction.
    def plot_pixel(self, x0, y0):
        self.create_line(x0, y0, x0+1, y0)
        print x0, y0

    # Calculates the cubic Bezier polynomial for
    # the n+1=4 coordinates.
    def cubic_bezier_sum(self, t, w):
        t2 = t * t
        t3 = t2 * t
        mt = 1-t
        mt2 = mt * mt
        mt3 = mt2 * mt
        return w[0]*mt3 + 3*w[1]*mt2*t + 3*w[2]*mt*t2 + w[3]*t3


    def draw_cubic_bez(self, p1, p2, p3, p4):
        t = 0
        points = []
        while (t < 1):
            x = self.cubic_bezier_sum(t, (p1[0], p2[0], p3[0], p4[0]))
            y = self.cubic_bezier_sum(t, (p1[1], p2[1], p3[1], p4[1]))
            points.append((math.floor(x), math.floor(y)))
            t += 0.001
        return points