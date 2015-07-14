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
<<<<<<< HEAD
sprite.right(70)
sprite.forward(100)

sprite2 = codesters.Sprite("")
sprite2.go_to(200,200)
sprite2.backward(400)
sprite2.move_down(400)
sprite2.forward(200)
sprite2.set_direction(0,0)
sprite2.forward(200)
=======
sprite.right(45)
sprite.forward(100)
def moveToMouse(event):
    sprite.glide_to(event.x-250, (event.y-250)*-1)
stage.event_click(moveToMouse)
>>>>>>> 5806db577ae4514104da756f0c24749d23da2a53
