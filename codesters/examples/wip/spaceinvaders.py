import codesters

global ship, index_collision, laser

x = -200
y = 210

for row in range(3):
    for column in range(6):
        alien = codesters.Sprite("alien1", x, y)
        alien.set_x_speed(.2)
        alien.set_size(.4)
        x += 75
    y -= 60
    x = -200

stage.set_bounce(1)
stage.set_background("space")
ship = codesters.Sprite("rocket", 0, -215)
ship.set_size(.5)
x = -200
y = 210
for row in range(3):
    for column in range(6):
        alien = codesters.Sprite("alien1", x, y)
        alien.set_x_speed(.2)
        alien.set_size(.4)
        x += 75
    y -= 60
    x = -200

stage.set_bounce(1)
stage.set_background("space")
ship = codesters.Sprite("rocket", 0, -215)
ship.set_size(.5)

def index_collision(index):
    sprite_collided_with = stage.get_sprite_by_index(index)
    sprite_collided_with.go_to(550, 0)
    laser.go_to(500, 500)
    # add any other actions...


def space():
    x = ship.get_x()
    laser = codesters.Circle(x, -190, 8, "red")
    laser.move_up(500)
    laser.event_collision(index_collision)
stage.event_space_key(space)


def left():
    ship.move_left(20)
    # add other actions...
stage.event_left_key(left)
def right():
    ship.move_right(20)
    # add other actions...
stage.event_right_key(right)


def index_collision(index):
    sprite_collided_with = stage.get_sprite_by_index(index)
    sprite_collided_with.go_to(550, 0)
    laser.go_to(500, 500)
    # add any other actions...


def space():
    x = ship.get_x()
    laser = codesters.Circle(x, -190, 8, "red")
    laser.move_up(500)
    laser.event_collision(index_collision)
stage.event_space_key(space)


def left():
    ship.move_left(20)
    # add other actions...
stage.event_left_key(left)
def right():
    ship.move_right(20)
    # add other actions...
stage.event_right_key(right)