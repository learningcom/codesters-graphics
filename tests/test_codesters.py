import codesters

def go_to(x,y):
    sprite = codesters.Sprite()
    sprite.go_to(x,y)
    return [sprite.get_x(),sprite.get_y()]

def test_go_to():
    coords = go_to(200,300)
    x = coords[0]
    y = coords[1]
    assert x == 200 and y == 300

def right(amount):
    sprite = codesters.Sprite()
    sprite.move_right(amount)
    return sprite.get_x()

def test_right():
    amount_to_move_right = 79
    new_x = right(amount_to_move_right)
    assert amount_to_move_right == new_x

def left(amount):
    sprite = codesters.Sprite()
    sprite.move_left(amount)
    return sprite.get_x()

def test_left():
    amount_to_move_left = -100
    new_x = left(amount_to_move_left)
    assert amount_to_move_left == -new_x

def down(amount):
    sprite = codesters.Sprite()
    sprite.move_down(amount)
    return sprite.get_y()

def test_down():
    amount_to_move_down = 54
    new_y = down(amount_to_move_down)
    assert amount_to_move_down == -new_y

def up(amount):
    sprite = codesters.Sprite()
    sprite.move_up(amount)
    return sprite.get_y()

def test_up():
    amount_to_move_up = 63
    new_y = up(amount_to_move_up)
    assert amount_to_move_up == new_y

def clockwise(amount):
    sprite = codesters.Sprite()
    sprite.turn_clockwise(amount)
    return sprite.get_rotation()

def test_clockwise():
    amount_to_turn_clockwise = 78
    new_heading = clockwise(amount_to_turn_clockwise)
    assert new_heading == -amount_to_turn_clockwise

def counterclockwise(amount):
    sprite = codesters.Sprite()
    sprite.turn_counterclockwise(amount)
    return sprite.get_rotation()

def test_counterclockwise():
    amount_to_turn_counterclockwise = -0
    new_heading = counterclockwise(amount_to_turn_counterclockwise)
    assert new_heading == amount_to_turn_counterclockwise

sprite = codesters.Sprite()
sprite.wait(1)
sprite.left(78)
print sprite.width