import codesters
import time

stage = codesters.Environment()
stage.set_background("summer")


sprite = codesters.Sprite()
global sprite
#sprite.move_left(200)
sprite.left(-90)
sprite.left(90)

sprite3 = codesters.Sprite("Alien-2")
global sprite3
sprite3.left(45)
sprite3.left(45)
sprite3.right(90)

sprite2 = codesters.Sprite("Alien-1")
global sprite2
sprite2.move_right(200)

sprite.physics_on()
#sprite.gravity_off()
#sprite.set_drag_on()

sprite2.physics_on()
#sprite2.gravity_off()
#sprite2.set_drag_on()

sprite3.physics_on()
#sprite3.gravity_off()
#sprite3.set_drag_on()

# print codesters.Manager.elements

sprite.print_corners()
sprite2.print_corners()
sprite3.print_corners()


def collision():
    sprite2.debug()
    sprite3.debug()
    sprite2.yspeed = -abs(sprite2.yspeed) - 1
    if (sprite2.xspeed < 0):
        sprite2.xspeed -= 0.1
    if (sprite2.xspeed > 0):
        sprite2.xspeed += 0.1

        # add any other actions...

sprite2.event_collision_goal(collision)

sprite3.is_goal()


# def click():
#     print "hello"
# sprite.event_click(click)
#
# def click2():
#     print "hello2"
# sprite2.event_click(click2)
#
# def click3():
#     print "hello3"
# sprite2.event_click(click3)

def up():
    sprite.jump(16)
sprite.event_key('up', up)

def left():
    sprite.xspeed -= 1
sprite.event_key('left', left)

def right():
    sprite.xspeed += 1
sprite.event_key('right', right)

sprite3.collision_on()
sprite2.collision_on()
#sprite.collision_on()

stage.enable_all_walls()
stage.set_bounce(0.6)

def moveToMouse(event):
    #sprite2.glide_to(event.x-250, 250 - event.y)
    print event.x - 250, 250 - event.y

stage.event_click(moveToMouse)
