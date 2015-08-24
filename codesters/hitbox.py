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
        head_cos = math.cos(self.sprite.heading * math.pi/180) * self.sprite.size
        head_sin = math.sin(self.sprite.heading * math.pi/180) * self.sprite.size
        self.top_right[0] = -(head_cos * self.base_top_right_x) + (self.base_top_right_y * head_sin) + self.sprite.xcor
        self.top_right[1] = -(head_sin * self.base_top_right_x) - (self.base_top_right_y * head_cos) + self.sprite.ycor
        self.top_left[0] = -(head_cos * self.base_top_left_x) + (self.base_top_left_y * head_sin) + self.sprite.xcor
        self.top_left[1] = -(head_sin * self.base_top_left_x) - (self.base_top_left_y * head_cos) + self.sprite.ycor
        self.bottom_right[0] = -(head_cos * self.base_bottom_right_x) + (self.base_bottom_right_y * head_sin) + self.sprite.xcor
        self.bottom_right[1] = -(head_sin * self.base_bottom_right_x) - (self.base_bottom_right_y * head_cos) + self.sprite.ycor
        self.bottom_left[0] = -(head_cos * self.base_bottom_left_x) + (self.base_bottom_left_y * head_sin) + self.sprite.xcor
        self.bottom_left[1] = -(head_sin * self.base_bottom_left_x) - (self.base_bottom_left_y * head_cos) + self.sprite.ycor

    def printCorners(self):
        self.sprite.modes.append("print_corners")

    def draw(self):
        self.sprite.lines.append([(Manager.width + self.top_right[0],
                                   Manager.height - self.top_right[1],
                                   Manager.width + self.top_left[0],
                                   Manager.height - self.top_left[1]), "red", 1.0])
        self.sprite.lines.append([(Manager.width + self.top_right[0],
                                   Manager.height - self.top_right[1],
                                   Manager.width + self.bottom_right[0],
                                   Manager.height - self.bottom_right[1]), "red", 1.0])
        self.sprite.lines.append([(Manager.width + self.top_left[0],
                                   Manager.height - self.top_left[1],
                                   Manager.width + self.bottom_left[0],
                                   Manager.height - self.bottom_left[1]),"red",1.0])
        self.sprite.lines.append([(Manager.width + self.bottom_right[0],
                                   Manager.height - self.bottom_right[1],
                                   Manager.width + self.bottom_left[0],
                                   Manager.height - self.bottom_left[1]),"red",1.0])
