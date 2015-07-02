import codesters
import time

#Making a stage
stage = codesters.Stage()

#Making a circle
circle = codesters.Sprite()
circle.set_x(100)
circle.set_y(100)

#Making another circle
circle2 = codesters.Sprite()
circle2.set_x(250)

#time.sleep(2)

#Moving the first circle
circle.set_y(300)
circle.set_x(50)

#time.sleep(1)
circle2.set_y(10)
circle2.set_size(0.5)
circle.set_color('blue')

circle2.set_x(0)
circle2.set_y(0)
circle2.glide_to(100,100)
circle.move_forward(200)

circle3 = codesters.Sprite()
circle3.set_size(0.8)
circle3.set_color('green')
circle3.set_x(300)
circle3.set_y(300)
circle3.glide_to(200,200)
circle2.set_x(200)
circle2.set_y(200)

#Workaround; for right now, this like has to be in the program being run, rather than __init__.py as it should.
codesters.root.mainloop()