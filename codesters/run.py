#!/usr/bin/python
import os
import sys
import random

from manager import Manager
from environment import Environment

class App(object):

    def __init__(self, filename):
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
        #filepath = str(os.getcwd())+ '/' + self.filename
        filepath = self.filename
        try:
            execfile(filepath, globals())
        except IOError:
            print "There is no file named "+filepath+". Please try again!"
        except SyntaxError:
            print filepath+" is not a codesters Python file. Please try again!"

    def move_one(self):
        self.manager.run()
        self.animate = Manager.root.after(5, self.move_one)

#Workaround; for right now, this like has to be in the program being run, rather than __init__.py as it should.
def run(filename):
    app = App(filename)
    app.root.mainloop()

#run(sys.argv[1])
