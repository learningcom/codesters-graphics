## VOLLEYBALL BY SHIRLY
## LOCATED HERE: https://www.codesters.com/preview/2abfa838e59334f3c287194a0ecc8fbf625f9e3a/

import codesters
stage = codesters.Environment()

global ball, start_txt, win_text, player1, player2, barrier, net, player1_area, player2_area
start_txt = codesters.Text("PRESS SPACE TO START", 0, 75, "red")
ball = codesters.Circle(0, 0, 40, "blue")
ball.set_gravity_off()
win_text = codesters.Text(" ", 0, 175, "black")
def space_bar():
    ball.set_x_speed(random.randint(-6, 6) + 1)
    ball.set_gravity_on()
    start_txt.hide()
    win_text.hide()
stage.event_key("space", space_bar)


player1 = codesters.Sprite("hedgehog", -210, -225)
player1.set_size(.6)

player2 = codesters.Sprite("kitten", 210, -225)
player2.set_size(.5)
player2.flip_right_left()
barrier = codesters.Line(0, 250, 0, -250, "gray")
barrier.set_gravity_off()
net = codesters.Rectangle(0, -210, 20, 80, "darkgray")
net.set_gravity_off()
player1_area = codesters.Rectangle(-130, -250, 235, 10, "purple")
player1_area.set_gravity_off()
player2_area = codesters.Rectangle(130, -250, 235, 10, "blue")
player2_area.set_gravity_off()



def w_key():
    player1.move_up(30)
    # add other actions...
stage.event_key("w", w_key)

def a_key():
    player1.move_left(30)
    # add other actions...
stage.event_key("a", a_key)

def d_key():
    player1.move_right(30)
    # add other actions...
stage.event_key("d", d_key)


def up_key():
    player2.move_up(30)
    # add other actions...
stage.event_key("up", up_key)
def left_key():
    player2.move_left(30)
    # add other actions...
stage.event_key("left", left_key)
def right_key():
    player2.move_right(30)
    # add other actions...
stage.event_key("right", right_key)



stage.set_gravity(4)

def collision(player1, hit_sprite):
    if hit_sprite.get_name() == "circle":
        hit_sprite.set_x_speed(4)
        hit_sprite.set_y_speed(player1.get_y_speed() + 4)
    elif hit_sprite.get_color() == "gray":
        player1.set_x_speed(-1)
player1.event_collision(collision)



def collision(player_sprite, hit_sprite):
    if hit_sprite.get_name() == "circle":
        hit_sprite.set_x_speed(-4)
        hit_sprite.set_y_speed(player2.get_y_speed() + 4)
    # add any other actions...
    elif hit_sprite.get_color() == "gray":
        player2.set_x_speed(1)
player2.event_collision(collision)


def collision(ball, hit_sprite):
    if hit_sprite.get_color() == "darkgray":
        if ball.get_y() > -180:
            ball.set_y_speed(-ball.get_y_speed() + 1)
        elif ball.get_y() < -180:
            ball.set_x_speed(-ball.get_x_speed())
    elif hit_sprite.get_color() == "purple":
        ball.go_to(0, 0)
        ball.set_gravity_off()
        win_text.show()
        win_text.set_text("Player 2 wins!")
        start_txt.show()
    elif hit_sprite.get_color() == "blue":
        ball.go_to(0, 0)
        ball.set_gravity_off()
        win_text.show()
        win_text.set_text("Player 1 wins!")
        start_txt.show()
    # add any other actions...
ball.event_collision(collision)

