## FOOR SOME REASON, basketball.py IS BROKEN
## CODE BY GORDON HERE: https://www.codesters.com/preview/ec1d6c22a6c6ac0bfc71e9d07b74d4425ddc178e/
## IN THIS FILE, I AM REBUILDING IT PIECE BY PIECE TO SEE WHERE THE PROBLEM IS

import codesters

stage = codesters.Environment()
stage.set_background('stadium')
stage.set_background_x(-650)
stage.set_bounce(0.5)

back = codesters.Sprite('backboard')

back.set_size(0.5)
back.set_x(200)
back.set_y(-100)
back.set_gravity_off()
back.cannot_collide()

hoop = codesters.Sprite('hoop')
hoop.set_size(0.5)
hoop.set_x(170)
hoop.set_y(-90)
hoop.set_gravity_off()
hoop.cannot_collide()
hoop.is_goal()

## IT WAS A STUPID KEY ERROR WITH THE SPRITES