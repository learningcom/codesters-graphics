import codesters
import random
stage = codesters.Environment()

pipe_speed = 6
pipe_gap = 200
pipe_interval = 1.5
gravity = 3
flappiness = 12

# Stage setup
stage.set_background("moon")
stage.set_gravity(gravity)
stage.disable_all_walls()

# Dino setup
sprite = codesters.Sprite("fox")
sprite.set_size(0.5)
sprite.go_to(-200, 0)

# Score setup
score = 0
score_display = codesters.Text("Flappy Points: ", 0, 200, "white")

game_over = False
pipe_list = []


def space():
    sprite.jump(flappiness)
    # add other actions...
stage.event_space_key(space)

floor = codesters.Rectangle(0, -240, 500, 20, "black")
floor.set_gravity_off()


def interval():
    global score
    if not game_over:
        bottom_pipe = codesters.Rectangle(250, 0, 100, 400, "grey")
        bottom_pipe.set_x_speed(-pipe_speed)
        bottom_pipe.set_gravity_off()
        pipe_height = random.randint(-100, 100)
        bottom_pipe.set_top(pipe_height)
        pipe_list.append(bottom_pipe)

        top_pipe = codesters.Rectangle(250, 0, 100, 400, "grey")
        top_pipe.set_gravity_off()
        top_pipe.set_x_speed(-pipe_speed)
        top_pipe.set_bottom(pipe_height + pipe_gap)
        pipe_list.append(top_pipe)

        score += 1
        score_display.set_text("Flappy Points: " + str(score))
stage.event_interval(interval, pipe_interval)


def collision():
    game_over = True
    sprite.go_to(0, 0)
    sprite.set_y_speed(0)
    sprite.set_gravity_off()
    flappiness = 0

    text = codesters.Text("Game Over!", 0, 100, "red")
    for pipe in pipe_list:
        pipe.set_x_speed(0)
sprite.event_collision(collision)
