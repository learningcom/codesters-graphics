import codesters
import time

#Making a stage
stage = codesters.Stage()

#Making a circle
# circle = codesters.Sprite()
# circle.set_x(100)
# circle.set_y(100)
# circle.go_to(0,0)
# circle.set_speed(1)
#
# circle.glide_to(100,100)

stage.draw()
stage.set_background("Winterscape")

#Workaround; for right now, this like has to be in the program being run, rather than __init__.py as it should.
codesters.root.mainloop()