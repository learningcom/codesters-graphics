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
