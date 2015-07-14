#!/usr/bin/python
import sys
import codesters
from codesters import Manager


if len(sys.argv) != 2:
    print 'You must supply a filename to run with the codesters library e.g. "python run.py example1.py"'
    exit()

filename = sys.argv[1]

class App(object):

    def __init__(self):
        self.manager = Manager()
        self.canvas = Manager.canvas
        self.root = Manager.root
        self.canvas.pack()
        self.do()
        self.move_one()
        self.animate = None

    def do(self):
        #execfile(filename)
        stage = codesters.Environment()
        #stage.draw()
        stage.set_background("summer")
        sprite = codesters.Sprite("Alien1")
        sprite.set_speed(.5)
        sprite.move_up(100)
        sprite.turn_left(90)
        sprite.wait(2)
        sprite.glide_to(0,0)
        sprite.wait(3)
        sprite.right(70)

        def moveToMouse(event):
            sprite.glide_to(event.x-250, (event.y-250)*-1)
        stage.event_click(moveToMouse)

    def move_one(self):
        self.manager.run()
        self.animate = Manager.root.after(22, self.move_one)

#Workaround; for right now, this like has to be in the program being run, rather than __init__.py as it should.
app = App()
app.root.mainloop()
