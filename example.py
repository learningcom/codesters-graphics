import codesters
import time

stage = codesters.Environment()
stage.set_background("summer")


sprite2 = codesters.Sprite("Alien-1")
sprite2.move_up(200)

sprite = codesters.Sprite("Alien-2")
sprite.move_down(200)

sprite3 = codesters.Sprite("")


sprite.physics_on()
sprite.gravity_off()
sprite.set_drag_on()

sprite2.physics_on()
sprite2.gravity_off()
sprite2.set_drag_on()

sprite3.physics_on()
sprite3.gravity_off()
sprite3.set_drag_on()

print codesters.Manager.elements


# IF YOU SWAP SPRITE AND SPRITE2 HERE, WHAT IS PRINTED DOES NOT CHANGE. AT ALL.
sprite.print_corners()
sprite2.print_corners()

def collision():
    sprite.jump(5)
    if (sprite.xspeed < 0):
        sprite.xspeed -= 0.1
    if (sprite.xspeed > 0):
        sprite.xspeed += 0.1
        # add any other actions...


sprite2.event_collision(collision)

sprite2.collision_on()
sprite.collision_on()


# sprite.jump(10)
# sprite.set_x_speed(-4)

stage.enable_all_walls()
stage.set_bounce(0.8)


def moveToMouse(event):
    global sprite
    print event.x - 250, 250 - event.y


stage.event_click(moveToMouse)
