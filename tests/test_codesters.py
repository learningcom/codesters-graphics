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
