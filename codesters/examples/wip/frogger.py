## FROGGER BY SHIRLEY
## LOCATED HERE: https://www.codesters.com/preview/86a38f1a916adbfd928e4b4d54c758e2782f115a/

import codesters
stage = codesters.Environment()

start_ground = codesters.Rectangle(0, -240, 500, 25, "darkgreen")

mid_ground = codesters.Rectangle(0, 0, 500, 25, "darkgreen")

end_ground = codesters.Rectangle(0, 240, 500, 25, "darkgreen")

global frogger  # GLOBALS
frogger = codesters.Sprite("", 0, -250)
frogger.set_size(0.5)
print frogger.modes


# barrier = codesters.Line(-220, 248, -220, -248, "black")
# barrier2 = codesters.Line(220, 248, 220, -248, "black")

for counter in range(-200, 0, 50):
    road = codesters.Rectangle(0, counter, 500, 20, "gray")
    road.set_opacity(.2)  # IS OPACITY STILL NOT WORKING?

for counter in range(50, 250, 50):
    pond = codesters.Rectangle(0, counter, 500, 20, "blue")
    pond.set_opacity(.2)  # IS OPACITY STILL NOT WORKING?

global make_lilypad
def make_lilypad():
    y_pos = random.randrange(50, 250, 50)
    x_pos = random.choice([-300, 300])
    lilypad = codesters.Circle(x_pos, y_pos, 40, "green")
    lily_spd = random.randint(1, 4)
    lilypad.set_opacity(.3)
    if y_pos % 100 == 0:
        lilypad.set_x_speed(-lily_spd)
    elif y_pos % 100 != 0:
        lilypad.set_x_speed(lily_spd)

global make_car
def make_car():
    car_y_pos = random.randrange(-200, 0, 50)
    car_x_pos = random.choice([-300, 300])
    car_colors = ["red", "gold", "black", "orange"]
    rand_color = car_colors[random.randint(0, 3)]
    car = codesters.Square(car_x_pos, car_y_pos, 40, rand_color)
    car_spd = random.randint(1, 4)
    car.is_hazard()
    if car_y_pos % 100 == 0:
        car.set_x_speed(-car_spd)
    elif car_y_pos % 100 != 0:
        car.set_x_speed(car_spd)

# some cars to start off
make_car()
make_car()

# and some lilypads to start off with

make_lilypad()
make_lilypad()

def interval():
    rand_num = random.randint(1, 2)
    for counter in range(rand_num):
        make_car()
    rand_num = random.randint(1, 3)
    for counter in range(rand_num):
        make_lilypad()
stage.event_interval(interval, 1)

def up_key():
    frogger.set_y(frogger.get_y() + 50)
    print frogger.xcor, frogger.future_x
    print frogger.ycor, frogger.future_y
    frogger.print_corners()
    # add other actions...
stage.event_key("up", up_key)

def down_key():  # EVENT
    frogger.set_y(frogger.get_y() - 50)
    print frogger.xcor, frogger.future_x
    print frogger.ycor, frogger.future_y
    frogger.print_corners()
    # add other actions...
stage.event_key("down", down_key)

def left_key():  # EVENT
    frogger.set_x(frogger.get_x() - 50)
    print frogger.xcor, frogger.future_x
    print frogger.ycor, frogger.future_y
    frogger.print_corners()
    # add other actions...
stage.event_key("left", left_key)

def right_key():  # EVENT
    frogger.set_x(frogger.get_x() + 50)
    print frogger.xcor, frogger.future_x
    print frogger.ycor, frogger.future_y
    frogger.print_corners()
    # add other actions...
stage.event_key("right", right_key)

stage.disable_all_walls()


result = codesters.Text(" ", 0, 0, "red")
global result  # GLOBALS

# detecting what was collided with by color / shape seems like the easiest way
def collision(sprite, hit_sprite): # COLLISIONS MARK REALLY WEIRDLY IN THIS PROJECT. TRYING TO FIGURE THAT OUT.
    # print '############'
    # hit_sprite.get_name()
    # print '############'
    # if frogger hits a lilypad
    if hit_sprite.get_name() == "circle":
        '''
        print frogger.xcor, ', ', sprite.xcor, ',', hit_sprite.xcor  # FOR BUG TESTING
        print frogger.ycor, ', ', sprite.ycor, ',', hit_sprite.ycor  # FOR BUG TESTING
        print frogger.future_x, ', ', sprite.future_x, ',', hit_sprite.future_x  # FOR BUG TESTING
        print frogger.future_y, ', ', sprite.future_y, ',', hit_sprite.future_y  # FOR BUG TESTING
        '''
        frogger.glide_to(hit_sprite.get_x(), hit_sprite.get_y())
        frogger.set_x_speed(hit_sprite.get_x_speed())
    # if frogger hits a car
    elif hit_sprite.get_name() == "square":
        result.set_text("SPLAT!  GAME OVER!")
        print 'SPLAT'
        frogger.reset_animation()
    # if frogger hits the pond
    elif hit_sprite.get_color() == "blue":
        result.set_text("GAME OVER!")
    # if frogger hits the goal area
    elif hit_sprite.get_color() == "darkgreen" and hit_sprite.get_y() == 240:
        result.set_text("YOU WON!")
        result.set_color("lightgreen")
    # if frogger goes off to the side
    if frogger.get_x() > 260 or frogger.get_x() < -260:
        result.set_text("GAME OVER!")
        frogger.reset_animation()
frogger.event_collision(collision)
