## PROJECT BY CHRISTA
## LOCATED HERE: https://www.codesters.com/preview/e96c32d78a583d31b8e05529fe1d85fc02fddbb6/

import codesters
global stage
stage = codesters.Environment()


global ball, sprite1

stage.set_background("gridfine")
sprite1 = codesters.Sprite("penguin")
ball = codesters.Sprite("soccerball")
bounce = random.random()
stage.set_bounce(bounce)
ballbounce= random.randint(1,10)

sprite1.glide_to(-213, -162)
ball.set_bottom(-233)


def mouse_move():
    x = stage.mouse_x()
    y = stage.mouse_y()
    sprite1.set_position(x, y)
    # add other actions...
stage.event_mouse_move(mouse_move)

def ball_move():
    x = random.randint(-220,220)
    y = random.randint(-220,220)
    ball.set_x_speed(3)
    ball.set_y_speed(3)
    ball.glide_to(x, y)
ball_move()

def collision(sprite1, hit_ball):
    x_speed = ball.get_x_speed()
    y_speed = ball.get_y_speed()
    new_x_speed=-1.5*x_speed
    new_y_speed=-1.5*y_speed
    ball.set_x_speed(new_x_speed+0.5)
    ball.set_y_speed(new_y_speed+0.5)
sprite1.event_collision(collision)
