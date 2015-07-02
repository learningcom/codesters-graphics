import codesters
import time

#Making a stage
stage = codesters.Stage()

#Making a circle
circle = codesters.Sprite()
circle.set_x(100)
circle.set_y(100)
circle.go_to(0,0)
circle.set_speed(1)

time.sleep(2)

circle.move_right(200)
circle.move_left(100)
circle.move_down(200)
circle.move_backward(50)
circle.move_up(50)
circle.move_forward(100)

#Workaround; for right now, this like has to be in the program being run, rather than __init__.py as it should.
codesters.root.mainloop()