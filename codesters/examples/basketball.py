import codesters

stage = codesters.Environment()

sky = codesters.Rectangle(0, 0, 510, 510, 'lightblue')
sky.set_gravity_off()
sky.cannot_collide()

floor = codesters.Rectangle(0, -250, 500, 20, 'grey')
floor.set_gravity_off()
floor.cannot_collide()

back = codesters.Sprite('backboard', 200, -160)
back.set_gravity_off()
back.set_size(0.5)
back.cannot_collide()

hoop = codesters.Sprite('hoop', 170, -150)
hoop.set_gravity_off()
hoop.cannot_collide()
hoop.set_size(0.5)
hoop.is_goal()

ball = codesters.Sprite('basketball')
ball.set_size(0.4)
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
    ball.set_velx(0)
    ball.set_vely(0)
    ball.set_position(-200, 0)
    score += 1
    t.set_text(str(score))
ball.event_collision_goal(goal)