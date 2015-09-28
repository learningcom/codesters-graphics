import codesters
import random
#global backpack_box, counter_text, pollution_box, pollution_image, pollution_text, timer_text, timer_box, sprite, update_backpack, update_pollution, goal, add_prize, prize
stage = codesters.Environment()

stage.set_background('park')
sprite = codesters.Sprite("person1")

recyclable = "sodacan"
prize = "bike"
goal = 5

# This section creates the backpack, show_backpack(),
# and update_backpack()
counter = 0
backpack_box = codesters.Rectangle(300, 230, 100, 30, "lightgrey")
counter_text = codesters.Text(str(counter), 300, 230, "black")

def add_backpack(counter):
    backpack_box.set_x(-200)
    backpack_image = codesters.Sprite(recyclable, -230, 230)
    backpack_image.set_size(.25)
    counter_text.set_x(-180)

def update_backpack(counter):
    counter_text.set_text(counter)

# This section creates the pollution counter, show_pollution(),
# and update_pollution()
pollution = 0
pollution_box = codesters.Rectangle(300, 190, 100, 30, "lightgrey")
pollution_image = codesters.Rectangle(300, 190, 20, 20, "black")
pollution_text = codesters.Text(str(pollution), 300, 190, "black")

def show_pollution(pollution):
    pollution_box.set_x(-200)
    pollution_image.set_x(-230)
    pollution_text.set_x(-180)

def update_pollution(pollution):
    pollution_text.set_text(pollution)

# This section creates the timer and show_timer(),
# the timer is updated in the interval function
timer = 100
timer_box = codesters.Rectangle(300, 150, 100, 30, "lightgrey")
timer_text = codesters.Text("Time: " + str(timer), 300, 150, "red")
timer_text.set_size(.8)

def show_timer(time_limit):
    global timer
    timer = time_limit
    timer_text.set_text("Time: " + str(timer))
    timer_box.set_x(-200)
    timer_text.set_x(-200)

# This function creates the time loop that adds the recyclable sprites
# It also counts down the timer and adds to the polution counter
def add_recyclables(which_object):
    def interval():
        global timer
        global pollution
        x = random.randint(-225, 225)
        y = random.randint(-225, 0)
        new_recyclable = codesters.Sprite(which_object, x, y)
        new_recyclable.set_size(.3)
        timer -= 1
        timer_text.set_text("Time: " + str(timer))
        pollution += 1
        pollution_text.set_text(str(pollution))
    stage.event_interval(interval, 2)

# This section adds the prizes and makes them dragable
def add_prize(which_prize):
    my_prize = codesters.Sprite(prize, 200, 0)
    my_prize.set_size(.5)
    my_prize.set_drag_on()
    my_prize.collision_off()
    global counter
    counter -= goal
    update_backpack(counter)



# stage.set_background("park")
# sprite = codesters.Sprite("person1")
sprite.set_size(.5)
sprite.set_position(-100, -100)

def left():
    sprite.move_left(20)
    # add other actions...
stage.event_left_key(left)
def right():
    sprite.move_right(20)
    # add other actions...
stage.event_right_key(right)
def up():
    sprite.move_up(20)
    # add other actions...
stage.event_up_key(up)
def down():
    sprite.move_down(20)
    # add other actions...
stage.event_down_key(down)

# recyclable = "sodacan"
# prize = "bike"
# goal = 2
counter =  0
pollution = 0

add_recyclables(recyclable)
add_backpack(counter)
show_pollution(pollution)
show_timer(100)

def index_collision(index):
    global counter
    global pollution
    sprite_collided_with = stage.get_sprite_by_index(index)
    sprite_collided_with.go_to(500, 0)
    counter += 1
    update_backpack(counter)
    pollution -= 1
    update_pollution(pollution)
    if counter == goal:
        add_prize(prize)
sprite.event_collision(index_collision)





