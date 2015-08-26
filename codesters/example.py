#!/usr/bin/python
import os
import sys
import random

from manager import Manager
from environment import Environment


class App(object):

    def __init__(self,filename):
        self.manager = Manager()
        self.canvas = Manager.canvas
        self.root = Manager.root
        self.filename = filename
        self.canvas.pack()
        self.do()
        self.move_one()
        self.animate = None

    def do(self):
        global stage
        stage = Environment()

        filepath = os.path.dirname(os.path.abspath(__file__)) + '/examples/' + self.filename
        execfile(filepath, globals())



    def move_one(self):
        self.manager.run()
        self.animate = Manager.root.after(5, self.move_one)

#Workaround; for right now, this like has to be in the program being run, rather than __init__.py as it should.
def run(filename):
    app = App(filename)
    app.root.mainloop()


