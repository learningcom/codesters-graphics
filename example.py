import codesters
import time
stage = codesters.Environment()
stage.set_background("summer")

sprite = codesters.Sprite("Alien1")
#sprite2 = codesters.Sprite('')

#sprite.move_up(100)
# sprite.turn_left(90)
# sprite.wait(2)
#text = sprite.ask("hello: ")
#sprite.say(text)
# print sprite.get_wait_time(), "CHECKER 1"
# sprite.set_speed(4)
#sprite.glide_to(-100,200)
# sprite.wait(3)
# print sprite.get_total_wait_time(), "checker 2"

sprite.set_size(1)

sprite.set_rotation(90)
sprite.glide_to(0,90)
sprite.set_rotation(45)
# sprite.set_size(0.5)
#
# sprite.set_size(0.5)
# sprite.forward(200)
#
# sprite.set_direction(0,0)
# sprite.set_width(0.5)
# sprite.forward(100)
# def moveToMouse(event):
#     global sprite
#     sprite.glide_to(event.x-250, 250-event.y)
# stage.event_click(moveToMouse)

#sprite.gravity_on()
#
# sprite2 = codesters.Sprite("")
# sprite2.set_speed(4)
#
# sprite2.glide_to(0,0)
# sprite2.wait(1)
# sprite2.set_direction(10,-10)
# sprite2.forward(200)
# sprite2.glide_to(0,0)
