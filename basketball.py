import codesters

stage = codesters.Environment()
stage.set_background('BasketballStadium')
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
hoop.set_x(110)
hoop.set_y(-50)
hoop.set_gravity_off()
hoop.collision_on()
hoop.is_goal()

ball = codesters.Sprite('basketball')
ball.collision_on()
ball.set_size(0.2)

stage.set_gravity(10)

score = 0
t = codesters.Text('0', 200, 200)

def click(self):
    global ball
    ball.set_gravity_off()
    ball.go_to(stage.click_x(self), stage.click_y(self))
    ball.set_y_speed(0)
    ball.set_x_speed(0)
stage.event_click(click)

def click_up(self):
    global ball
    global stage
    ball.set_gravity_on()
    new_velx = ball.get_x() - stage.click_x(self)
    new_vely = -ball.get_y()+ stage.click_y(self)
    ball.set_x_speed(new_velx/5)
    ball.set_y_speed(new_vely/5)
stage.event_click_up(click_up)

def goal():
    global score
    global t
    score += 1
    t.set_text(str(score))
    ball.set_y(0)
    ball.set_x(-200)
    ball.set_velx(0)
    ball.set_vely(0)
ball.event_collision_goal(goal)
