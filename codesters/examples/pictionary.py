import codesters
global stage
stage = codesters.Environment()

global sprite, colors, block_width, announcer, words, word


words = ["boat", "tiger", "flower", "bee", "tshirt", "smiley face", "horse", "cat", "dog", "fish", "book", "nose", "mouth", "eyes"]


colors = ["pink", "red", "orangered", "yellow", "green", "lime", "aqua", "blue", "purple", "brown", "black", "white"]
block_width = 500/len(colors)
x = -250 + block_width / 2
y = 250 - block_width / 2
for col in colors:
    color_pick = codesters.Square(x, y, block_width, col)
    x += block_width

announcer = codesters.Sprite("kitten")
announcer.set_size(.5)
announcer.go_to(0, -225)

rand_index = random.randint(0, len(words)-1)
word = words[rand_index]
announcer.say("Okay player 2, look away!")
stage.wait(2)
announcer.say("Player 1, the word is " + word)
stage.wait(2)
announcer.say(" ")

sprite = codesters.Point(0, 0, 8, "black")

def click():
    if stage.click_y() > 250 - block_width:
        index = int((stage.click_x()+ 250) / block_width)
        # print index
        sprite.pen_up()
        color = colors[index]
        sprite.set_color(color)
        # print(color)
    elif stage.click_x() < 250 - block_width:
        is_drawing = sprite.get_pen_down()
        if is_drawing:
            sprite.pen_up()
        if not is_drawing:
            sprite.pen_down()
stage.event_click(click)

def mouse_move():
    x = stage.mouse_x()
    y = stage.mouse_y()
    sprite.set_position(x, y)
    # add other actions...
stage.event_mouse_move(mouse_move)

finish_bg = codesters.Rectangle(-150, -225, 100, 30, None, "black")
finish_btn = codesters.Text("Done drawing?", -150, -225)
finish_btn.set_size(.7)

def click_finish():
    sprite.pen_up()
    print("done")
    announcer.say("Time to guess!")
    stage.wait(1)
    guess = " "
    while guess != word:
        stage.wait(1)
        guess = announcer.ask("What is the word?")
        if guess != word:
            announcer.say("Sorry, that's wrong!")
        else:
            announcer.say("Great job, you got it!")
finish_btn.event_click(click_finish)