import codesters
import time

#Making a stage
stage = codesters.Stage()

#Making a circle
circle = codesters.Sprite()
circle.set_x(100)
circle.set_y(100)
circle.set_speed(1)

sprite = codesters.Sprite("Alien1")
sprite.go_to(50,200)

#Workaround; for right now, this like has to be in the program being run, rather than __init__.py as it should.
codesters.root.mainloop()