import codesters


stage.set_background("baseballfield")
#stage.disable_all_walls()
caught=False
held=False
outatfirst=False
safeatfirst=False
thirdBase = codesters.Sprite("athlete1")
secondBase = codesters.Sprite("athlete1")
#shortstop = codesters.Sprite("athlete1")
firstBase = codesters.Sprite("athlete1")
pitcher = codesters.Sprite("athlete1")
baseball = codesters.Sprite("baseball")
#bat = codesters.Sprite("baseballbat")
#batter=codesters.Sprite("athlete2")
bat=None
batter=None
runner1=None

thirdBase.set_size(0.25)
secondBase.set_size(0.25)
#shortstop.set_size(0.25)
firstBase.set_size(0.25)
pitcher.set_size(0.25)
baseball.set_size(0.25)
#bat.set_size(0.25)
#batter.set_size(0.25)

#bat.go_to(10,-202)
thirdBase.go_to(-198, 21)
secondBase.go_to(11,218)
#shortstop.go_to(-100, 203)
firstBase.go_to(222,28)
#batter.go_to(-5,-210)

def batterSetup():
    global bat
    global batter
    bat = codesters.Sprite("baseballbat")
    batter=codesters.Sprite("athlete2")
    bat.set_size(0.25)
    batter.set_size(0.25)
    bat.go_to(10,-202)
    batter.go_to(-5,-210)
    bat.set_rotation(-45)
    pitcher.go_to(15,-2)
    baseball.go_to(10,10)
    baseball.set_y_speed(-5)
    baseball.collision_on()
    bat.collision_on()
    pitcher.collision_off()
    bat.set_rotation(-45)

batterSetup()



def collision(sprite, hit_sprite):
    #sprite.go_to(0,0)
    global baseball
    if hit_sprite==baseball:

        bat_y_speed = bat.get_y_speed()
        ball_y_speed = baseball.get_y_speed()
        #print(str(bat_y_speed-ball_y_speed))
        batx=bat.get_x()
        ballx=baseball.get_x()
        ball_x_speed=(ballx-batx)/6
        print(str(ballx-batx))
        hit_sprite.set_x_speed(ball_x_speed)
        hit_sprite.set_y_speed(bat_y_speed-ball_y_speed)
        batter.set_y_speed(3)
        batter.set_x_speed(3)
        stage.remove_sprite(bat)
        pitcher.collision_on()

    # add any other actions...
bat.event_collision(collision)

def collision(sprite, hit_sprite):
    global pitcher
    global caught
    global baseball
    global safeatfirst
    global batter
    global held
    if hit_sprite==pitcher:
        caught=True
        baseball.set_y_speed(0)
        baseball.set_x_speed(0)
        pitcher.collision_off()
    if hit_sprite==firstBase:
        held=True
        baseball.set_y_speed(0)
        baseball.set_x_speed(0)
        firstBase.collision_off()
        if safeatfirst == False and outatfirst==False:
            outatfirst==True
            batter.set_y_speed(0)
            batter.set_x_speed(0)
            # text = codesters.Text("text", x, y)
            text = codesters.Text("OUT", 0, 100)
            text.set_size(3)
    if hit_sprite==secondBase:
        held=True
        baseball.set_y_speed(0)
        baseball.set_x_speed(0)
        secondBase.collision_off()
    if hit_sprite==thirdBase:
        held=True
        baseball.set_y_speed(0)
        baseball.set_x_speed(0)
        thirdBase.collision_off()
    # add any other actions...
baseball.event_collision(collision)

def s_key():
    global bat
    #global stage
    bat.set_y_speed(10)
    stage.wait(.1)
    bat.set_y_speed(0)
    stage.remove_sprite(bat)
    # add other actions...
stage.event_key("s", s_key)

def a_key():
    global bat
    bat.move_left(3)
    # add other actions...
stage.event_key("a", a_key)

def d_key():
    global bat
    bat.move_right(3)
    # add other actions...
stage.event_key("d", d_key)

def left_key():
    global baseball
    global pitcher
    global held
    global caught
    thirdBase.collision_on()
    if held==True:
        caught=False
        #print("what")
        baseball.set_y_speed((21-baseball.get_y())/10)
        baseball.set_x_speed((-198-baseball.get_x())/10)
        #print(baseball.get_x_speed())
        #print(baseball.get_y_speed())
    held=False
    # add other actions...
stage.event_key("left", left_key)

def right_key():
    global baseball
    global pitcher
    global held
    global caught
    firstBase.collision_on()
    if held==True:
        caught=False
        #print("what")
        baseball.set_y_speed((28-baseball.get_y())/25)
        baseball.set_x_speed((222-baseball.get_x())/25)
        #print(baseball.get_x_speed())
        #print(baseball.get_y_speed())
    held=False
    # add other actions...
stage.event_key("right", right_key)

def down_key():
    global baseball
    global pitcher
    global held
    global caught
    pitcher.collision_on()
    if held==True:
        caught=False
        #print("what")
        baseball.set_y_speed((-202-baseball.get_y())/25)
        baseball.set_x_speed((10-baseball.get_x())/25)
        #print(baseball.get_x_speed())
        #print(baseball.get_y_speed())
    held=False
    # add other actions...
stage.event_key("down", down_key)


def up_key():
    global baseball
    global pitcher
    global held
    global caught
    secondBase.collision_on()
    if held==True:
        caught=False

        #print("what")
        baseball.set_y_speed((218-baseball.get_y())/25)
        baseball.set_x_speed((20-baseball.get_x())/25)
        #print(baseball.get_x_speed())
        #print(baseball.get_y_speed())
    held=False
    # add other actions...
stage.event_key("up", up_key)


def mouse_move():
    global held
    global caught
    global stage
    x = stage.mouse_x()
    y = stage.mouse_y()
    pitcher.set_position(x, y)
    if caught:
        held=True
        pitcher.collision_off()
        baseball.set_position(x,y)
        if 220<x<230 and -15<y<25:
            if outatfirst==False and safeatfirst==False:
                batter.set_y_speed(0)
                batter.set_x_speed(0)
                # text = codesters.Text("text", x, y)
                text = codesters.Text("OUT", 0, 100)
                text.set_size(3)
                stage.remove_sprite(batter)

    # add other actions...
stage.event_mouse_move(mouse_move)

def interval():
    global safeatfirst
    global outatfirst
    runx=batter.get_x()
    runy=batter.get_y()
    # print(str(runx) + " " +str(runy))
    # print("x?: "+str(220<runx<230))
    # print("y?: "+str(-15<runy<25))
    # print(outatfirst)
    # print(safeatfirst)
    if 220<runx<230 and -15<runy<25:
        if outatfirst==False and safeatfirst==False:
            safeatfirst=True
            batter.set_y_speed(0)
            batter.set_x_speed(0)
            # text = codesters.Text("text", x, y)
            text = codesters.Text("SAFE", 0, 100)
            text.set_size(3)

    # add any other actions...
stage.event_interval(interval, .01)



