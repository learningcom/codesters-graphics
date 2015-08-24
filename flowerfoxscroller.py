import codesters
stage = codesters.Environment()

# we need a really long background like this field of flowers
stage.set_background('flower_field')

# Make a character, we'll use a fox
global fox
fox = codesters.Sprite('fox', -200, 0)

# Add some gravity so our fox doesn't float away
stage.set_gravity(10)
stage.set_bounce(0.3)


# Let's make the fox jump if you push the space bar
def space_key():
    fox.jump(10)
stage.event_key('space', space_key)

# Let's make something for the fox to find
# How about some presents, maybe it's the fox's birthday
# Here's an empty list that will hold the presents
presents = []

for i in range(10):  # making 10 presents

    present = codesters.Sprite('present1', 200 * i, -100)

    # Turn gravity off so it doesn't fall
    present.set_gravity_off()

    # make a is_goal attribute that we can look for later
    present.is_goal = True

    # add it to our list of presents
    presents.append(present)


# In a side scroller game, the background moves
# and the character does not move.

# If the player pushes an arrow key, we will
# make the background and the presents move
# and it will look like the fox is moving instead

# make a function for when a key is pressed
def stage_move_right():
    global stage
    global presents

    # move the stage
    stage.move_right(20)

    # move every present in our list
    for p in presents:
        p.set_x(p.get_x() + 20)
stage.event_key('left', stage_move_right)  # The left key makes the stage move right


# Do the same thing for the other direction
def stage_move_left():
    global stage
    global presents
    stage.move_left(20)
    for p in presents:
        p.set_x(p.get_x() - 20)
stage.event_key('right', stage_move_left)


# We can give the fox points when the fox gets a present
points = 0
points_text = codesters.Text(str(points), -220, 200)


# Make a function for when the fox finds a present
def get_present(fox, present):

    # the present disappears
    global stage
    stage.remove_sprite(present)

    # the fox spins
    fox.left(720)

    # we get a point
    global points
    points = points + 1

    # update our score text
    global points_text
    points_text.set_text(points)

# tell the fox to run the get_presents
# function when it hits something else
fox.event_collision(get_present)
