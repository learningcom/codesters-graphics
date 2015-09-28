import codesters
import random
stage = codesters.Environment()

stage.set_background("underwater")
stage.set_gravity(2)
stage.disable_floor()

sprite = codesters.Sprite("fish1", 0, -220)
sprite.gravity_off()

score = 0
score_board = codesters.Display(score)


def left():
    sprite.move_left(20)
    # add other actions...
stage.event_left_key(left)


def right():
    sprite.move_right(20)
    # add other actions...
stage.event_right_key(right)


def interval():
    x = random.randint(-260, 260)
    food = codesters.Circle(x, 230, 10, "sienna")
    # add any other actions...
stage.event_interval(interval, 2)


def index_collision(index):
    global score
    score += 1
    score_board.update(score)
    sprite_collided_with = stage.get_sprite_by_index(index)
    sprite_collided_with.go_to(500, 0)
    sprite.turn_right(360)
    # add any other actions...
sprite.event_collision(index_collision)


