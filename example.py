import codesters

#Making a circle
#When declaring a circle, you have to pass in the appropriate canvas, so it knows where to draw itself. This would be unnecessary if all of the classes were in one file. Pick your poison.
circle = codesters.Circle(codesters.canvas)
circle.set_x(100)
circle.set_y(100)
circle.draw()

#Making another circle
circle2 = codesters.Circle(codesters.canvas)
circle2.set_x(250)
circle2.draw()


#Workaround; for right now, this like has to be in the program being run, rather than __init__.py as it should.
codesters.root.mainloop()