## BASKETBALL BY GORDON
## LOCATED HERE: https://www.codesters.com/preview/ec1d6c22a6c6ac0bfc71e9d07b74d4425ddc178e/


import codesters

stage = codesters.Environment()
stage.set_background('BasketballStadium') # NAMES OF FILES ARE DIFFERENT (SITE VS. LOCAL ISSUE)
stage.set_background_x(-650)
stage.set_bounce(0.5)

back = codesters.Sprite('backboard')

back.set_size(0.5)
back.set_x(200)
back.set_y(-100)
back.set_gravity_off()
back.cannot_collide()

hoop = codesters.Sprite('net')
hoop.set_size(0.5)
hoop.set_x(110) # TWEAKED BECAUSE WE ACTUALLY HAVE THE IMAGE FILE AND THE SITE DOESNT
hoop.set_y(-50) # ^ SAME REASON
hoop.set_gravity_off()
hoop.collision_on() # DO NOT UNDERSTAND HOW THE HOOP IS A GOAL WITHOUT COLLISION SET TO TRUE ON THE SITE, INFRASTRUCTURE ISSUE
hoop.is_goal()

ball = codesters.Sprite('basketball')
ball.collision_on() # NEED TO SET SPRITE DEFAULT COLLISION TO TRUE, BUT WAS BUGGY
ball.set_size(0.2)

stage.set_gravity(10)

score = 0
t = codesters.Text('0', 200, 200)

def click(): 
    global ball # ADDED GLOBALS
    ball.set_gravity_off()
    ball.go_to(stage.click_x(), stage.click_y())
    ball.set_y_speed(0)
    ball.set_x_speed(0)
stage.event_click(click)

def click_up(): 
    global ball# ADDED GLOBALS
    global stage# ADDED GLOBALS
    ball.set_gravity_on()
    new_velx = ball.get_x() - stage.click_x()
    new_vely = ball.get_y() - stage.click_y()
    print ball.get_y(), stage.click_y(), new_vely

    ball.set_x_speed(new_velx/5)
    ball.set_y_speed(new_vely/5)
stage.event_click_up(click_up)

def goal():
    global score
    global t # ADDED GLOBALS
    score += 1
    t.set_text(str(score))
    ball.set_y(0)
    ball.set_x(-200)
    ball.set_velx(0)
    ball.set_vely(0)
ball.event_collision_goal(goal)
