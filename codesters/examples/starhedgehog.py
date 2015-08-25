import codesters
import random
#global hedgey, stage, text
global hedgey, text

stage = codesters.Environment()
stage.set_background("moon")

hedgey = codesters.Sprite("hedgehog")
hedgey.go_to(0, -210)

points = 0
text = codesters.Text(str(points), 190, -65, "black")

def interval():
    x = random.randint(-230,230)
    y = random.randint(0,230)
    star = codesters.Star(x, y, 5, 20, "yellow")
stage.event_interval(interval, 2)


def left():
    hedgey.turn_left(10)
stage.event_left_key(left)

def right():
    hedgey.turn_right(10)
stage.event_right_key(right)

def up():
    hedgey.move_forward(575)
    stage.wait(1)
    hedgey.go_to(0, -210)
stage.event_up_key(up)

def index_collision(index):
    global points
    sprite_collided_with = stage.get_sprite_by_index(index)
    stage.remove_sprite(sprite_collided_with)
    points = points + 1
    text.set_text(str(points))
hedgey.event_collision(index_collision)



