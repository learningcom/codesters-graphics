import codesters
import time

#Making a stage
stage = codesters.Stage()

#Making a circle
circle = codesters.Circle()
circle.set_x(100)
circle.set_y(100)

#Making another circle
circle2 = codesters.Circle()
circle2.set_x(250)

time.sleep(2)

#Moveing the first circle
circle.set_y(300)
circle.set_x(50)

#Workaround; for right now, this like has to be in the program being run, rather than __init__.py as it should.
codesters.root.mainloop()