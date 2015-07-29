import math
from Tkinter import Tk, Canvas
from .manager import Manager


class Hitbox(object):

    def __init__(self, top_right, top_left, bottom_right, bottom_left, sprite):
        self.root = Manager.canvas
        self.canvas = Manager.canvas
        self.sprite = sprite
        self.base_top_right_x = top_right[0]
        self.base_top_right_y = top_right[1]
        self.base_top_left_x = top_left[0]
        self.base_top_left_y = top_left[1]
        self.base_bottom_right_x = bottom_right[0]
        self.base_bottom_right_y = bottom_right[1]
        self.base_bottom_left_x = bottom_left[0]
        self.base_bottom_left_y = bottom_left[1]
        self.top_right = top_right
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.bottom_left = bottom_left

    def update_corners(self):
        heading_cos = math.cos(self.sprite.future_heading * math.pi/180)
        heading_sin = math.sin(self.sprite.future_heading * math.pi/180)
        self.top_right[0] = heading_cos * (-self.base_top_right_x) - (-self.base_top_right_y) * heading_sin + self.sprite.future_x
        self.top_right[1] = heading_sin * (-self.base_top_right_x) + (-self.base_top_right_y) * heading_cos +self.sprite.future_y
        self.top_left[0] = heading_cos * (-self.base_top_left_x) - (-self.base_top_left_y) * heading_sin +self.sprite.future_x
        self.top_left[1] = heading_sin * (-self.base_top_left_x) + (-self.base_top_left_y) * heading_cos +self.sprite.future_y
        self.bottom_right[0] = heading_cos * (-self.base_bottom_right_x) - (-self.base_bottom_right_y) * heading_sin +self.sprite.future_x
        self.bottom_right[1] = heading_sin * (-self.base_bottom_right_x) + (-self.base_bottom_right_y) * heading_cos +self.sprite.future_y
        self.bottom_left[0] = heading_cos * (-self.base_bottom_left_x) - (-self.base_bottom_left_y) * heading_sin +self.sprite.future_x
        self.bottom_left[1] = heading_sin * (-self.base_bottom_left_x) + (-self.base_bottom_left_y) * heading_cos +self.sprite.future_y

        #print self.base_bottom_left_y, "baseee"

    def printCorners(self):
        self.sprite.modes.append("print_corners")

    def draw(self):
        #print "DRAWING"
        self.sprite.lines.append([(self.canvas.winfo_reqwidth()/2 +self.top_right[0],self.canvas.winfo_reqheight()/2 - self.top_right[1],self.canvas.winfo_reqwidth()/2 +self.top_left[0],self.canvas.winfo_reqheight()/2 - self.top_left[1]), "red", 1.0])
        self.sprite.lines.append([(self.canvas.winfo_reqwidth()/2 +self.top_right[0],self.canvas.winfo_reqheight()/2 - self.top_right[1],self.canvas.winfo_reqwidth()/2 +self.bottom_right[0],self.canvas.winfo_reqheight()/2 - self.bottom_right[1]), "red", 1.0])
        self.sprite.lines.append([(self.canvas.winfo_reqwidth()/2 +self.top_left[0],self.canvas.winfo_reqheight()/2 - self.top_left[1],self.canvas.winfo_reqwidth()/2 +self.bottom_left[0],self.canvas.winfo_reqheight()/2 - self.bottom_left[1]),"red",1.0])
        self.sprite.lines.append([(self.canvas.winfo_reqwidth()/2 +self.bottom_right[0],self.canvas.winfo_reqheight()/2 - self.bottom_right[1],self.canvas.winfo_reqwidth()/2 +self.bottom_left[0],self.canvas.winfo_reqheight()/2 - self.bottom_left[1]),"red",1.0])
