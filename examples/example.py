import codesters
#Making a stage
stage = codesters.Environment()


sprite = codesters.Sprite("alien1")


def forever():
    print "blahblahblah"
stage.set_background("summer")
    # add any other actions...
stage.set_background_x(-100)
stage.set_background_y(-100)
stage.move_right(300)
stage.move_up(350)
stage.move_left(400)
stage.move_down(60)
def moveToMouse(event):
    #sprite2.glide_to(event.x-250, 250 - event.y)
    print event.x - 250, 250 - event.y

stage.event_click(moveToMouse)
