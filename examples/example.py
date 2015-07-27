import codesters
import random # I DONT KNOW WHERE TO IMPORT THIS FOR IT TO WORK OUTSIDE OF THIS FILE
#Making a stage
stage = codesters.Environment()

pipe_speed = 6
pipe_gap = 140
pipe_interval = 1.5
gravity = 10
flappiness = 5

stage.set_background("underwater")
sprite = codesters.Sprite("Fish_1")
sprite.set_size(1)
sprite.go_to(-200, 0)

stage.set_gravity(gravity)
stage.disable_all_walls()

score = 0
game_over = False

score_display = codesters.Text("Flappy Points: ", 0, 200, "yellow")

def space():
    sprite.jump(flappiness)
    # add other actions...
stage.event_space_key(space)

floor = codesters.Rectangle(0, -240, 500, 20, "black")
floor.set_gravity_off()

pipe_list = []
def interval():
    global score
    if game_over == False:
        # sprite = codesters.Rectangle(x, y, width, height, "color")
        bottom_pipe = codesters.Rectangle(250, 0, 100, 400, "blue")
        bottom_pipe.set_x_speed(-pipe_speed)
        bottom_pipe.set_gravity_off()
        pipe_height = random.randint(-100, 100)
        bottom_pipe.set_top(pipe_height)
        pipe_list.append(bottom_pipe)

        # sprite = codesters.Rectangle(x, y, width, height, "color")
        top_pipe = codesters.Rectangle(250, 0, 100, 400, "blue")
        top_pipe.set_gravity_off()
        top_pipe.set_x_speed(-pipe_speed)
        top_pipe.set_bottom(pipe_height + pipe_gap)
        pipe_list.append(top_pipe)

        score += 1
        score_display.set_text("Flappy Points: " + str(score))
stage.event_interval(interval, pipe_interval)

def collision():
    game_over = True
    sprite.go_to(0,0)
    sprite.set_y_speed(0)
    sprite.set_gravity_off()
    flappiness = 0

    # text = codesters.Text("text", x, y, "color")
    text = codesters.Text("Game Over!", 0, 100, "yellow")
    for pipe in pipe_list:
        pipe.set_x_speed(0)
sprite.event_collision(collision)
