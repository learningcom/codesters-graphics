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


# sprite.set_size(1)
# sprite.physics_on()
# sprite.jump(10)
#
# sprite.set_x_speed(4)
#
# stage.set_bounce(1)
#
# stage.enable_all_walls()
#
# sprite.set_drag_on()
sprite.left(50)
sprite.flip_horizontal()
sprite.wait(5)
sprite.flip_vertical()
sprite.wait(5)
sprite.flip_left_right()
sprite.wait(5)
sprite.face_backward()
sprite.wait(5)
sprite.face_rightside_up()


# sprite.set_height(500)
# sprite.set_width(100)

#sprite.set_top(200)
#sprite.set_opacity(.5)
#sprite.left(50)
# print sprite.get_rotation()
# print sprite.get_top()
# print sprite.get_right()
# print sprite.get_bottom()
# print sprite.get_left()


#sprite.set_size(0.5)
#sprite.forward(200)

#sprite.set_direction(0,0)
#sprite.setwidth(0.5)
#sprite.forward(100)

def moveToMouse(event):
    global sprite
    print event.x-250, 250-event.y
stage.event_click(moveToMouse)

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
