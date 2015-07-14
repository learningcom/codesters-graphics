import codesters
stage = codesters.Environment()
stage.set_background("summer")
sprite = codesters.Sprite("Alien1")
sprite.set_speed(.5)
sprite.move_up(100)
sprite.turn_left(90)
sprite.wait(2)
sprite.glide_to(0,0)
sprite.wait(3)
sprite.right(70)
def moveToMouse(event):
    sprite.glide_to(event.x-250, (event.y-250)*-1)
stage.event_click(moveToMouse)