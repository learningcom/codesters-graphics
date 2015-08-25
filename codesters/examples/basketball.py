## BASKETBALL BY GORDON
## LOCATED HERE: https://www.codesters.com/preview/ec1d6c22a6c6ac0bfc71e9d07b74d4425ddc178e/

import codesters

global ball, t

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

ball = codesters.Sprite('basketball')

ball.set_size(0.2)

stage.set_gravity(10)

score = 0
t = codesters.Text('0', 200, 200)

def click():
    ball.set_gravity_off()
    ball.go_to(stage.click_x(), stage.click_y())
    ball.set_y_speed(0)
    ball.set_x_speed(0)
stage.event_click(click)

def click_up():
    ball.set_gravity_on()
    new_velx = ball.get_x() - stage.click_x()
    new_vely = ball.get_y() - stage.click_y()
    ball.set_x_speed(new_velx/5)
    ball.set_y_speed(new_vely/5)
stage.event_click_up(click_up)

def goal():
    global score
    score += 1
    t.set_text(str(score))
    ball.set_y(0)
    ball.set_x(-200)
    ball.set_velx(0)
    ball.set_vely(0)
ball.event_collision_goal(goal)