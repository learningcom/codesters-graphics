import codesters
stage = codesters.Environment()
stage.set_background("summer")
sprite = Sprite("Alien1")
self.sprite.set_speed(.5)
self.sprite.move_up(100)
self.sprite.turn_left(90)
self.sprite.wait(2)
self.sprite.glide_to(0,0)
self.sprite.wait(3)
self.sprite.right(70)
def moveToMouse(event):
    self.sprite.glide_to(event.x-250, (event.y-250)*-1)
self.stage.event_click(moveToMouse)