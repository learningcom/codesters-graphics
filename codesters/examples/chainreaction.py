import codesters
import random
stage = codesters.Environment()

#  Globals
level_running = False
circle_grow_multiplier = 4
small_circle_size = 20


class LevelManager(object):
    def __init__(self):
        self.levels = []
        self.current_level = -1

    def add_level(self, level):
        self.levels.append(level)

    def next_level(self):
        self.current_level += 1
        self.restart_level()

    def restart_level(self):
        if self.current_level < len(self.levels):
            l = self.levels[self.current_level]
            l.display_start_button()
        else:
            end_text = codesters.Text('Game Over', 0, 0)

lm = LevelManager()


class Level(object):

    def __init__(self, num_circles, num_goal):
        self.num_circles = num_circles
        self.num_goal = num_goal

        # Sprite Management
        self.sprites = []
        self.circles = []

        # Score Textbox
        self.score = 0
        self.score_text = None

        self.user_has_clicked = False

    def display_start_button(self):
        start_square = codesters.Rectangle(0, -80, 100, 50, 'green')
        start_square.event_click(self.start_level)
        self.sprites.append(start_square)

        button_text = codesters.Text('Start', 0, -80)
        button_text.set_color('#ffffff')
        self.sprites.append(button_text)

        goal_text = codesters.Text('Goal: ' + str(self.num_goal) + ' points')
        goal_text.set_color('#ffffff')
        self.sprites.append(goal_text)

    def start_level(self):
        self.clean_up()
        global level_running
        level_running = True
        
        self.score = 0

        self.score_text = codesters.Text('0', -230, 205)
        self.score_text.set_color('#ffffff')
        self.sprites.append(self.score_text)

        goal_text = codesters.Text('Goal: ' + str(self.num_goal) + ' points', -180, 230)
        goal_text.set_color('#ffffff')
        self.sprites.append(goal_text)

        self.make_circles()
        stage.event_click(self.click_circle)
        self.user_has_clicked = False
        # Game is now running, waiting for a click

    def circle_collision(self, sprite, hit_sprite):
        if hit_sprite.is_big and not sprite.is_big:
            sprite.set_size(circle_grow_multiplier)
            sprite.set_x_speed(0)
            sprite.set_y_speed(0)
            sprite.is_big = True
            sprite.event_collision(None)
            sprite.event_delay(self.remove_sprite, 2)
            self.score += 1
            self.score_text.set_text(str(self.score))

    def random_color(self):
        r = random.randint(128, 255)
        g = random.randint(128, 255)
        b = random.randint(128, 255)
        return r, g, b

    def click_circle(self):
        if level_running and not self.user_has_clicked:
            print('clicked')
            self.user_has_clicked = True
            x = stage.click_x()
            y = stage.click_y()
            circle_size = small_circle_size * circle_grow_multiplier
            circle = codesters.Circle(x, y, circle_size)
            circle.is_big = True
            self.sprites.append(circle)
            self.circles.append(circle)
            circle.event_delay(self.remove_sprite, 2)

    def remove_sprite(self, sprite):
        self.sprites.remove(sprite)
        self.circles.remove(sprite)
        stage.remove_sprite(sprite)
        big_sprite = False
        for s in self.circles:
            if s.is_big:
                big_sprite = True
        if not big_sprite:
            self.end_level()

    def next_level(self):
        self.clean_up()
        global lm
        lm.next_level()

    def restart_level(self):
        self.clean_up()
        global lm
        lm.restart_level()

    def end_level(self):
        self.clean_up()
        if self.score >= self.num_goal:
            end_text = codesters.Text('You Win!')
            self.sprites.append(end_text)
            next_button = codesters.Rectangle(0, -80, 100, 50, 'green')
            next_button.event_click(self.next_level)
            self.sprites.append(next_button)
            button_text = codesters.Text('Continue', 0, -80)
            button_text.set_color('#ffffff')
            self.sprites.append(button_text)
        else:
            end_text = codesters.Text('Close! Try again.')
            self.sprites.append(end_text)
            next_button = codesters.Rectangle(0, -80, 100, 50, 'green')
            next_button.event_click(self.restart_level)
            self.sprites.append(next_button)
            button_text = codesters.Text('Restart', 0, -80)
            button_text.set_color('#ffffff')
            self.sprites.append(button_text)

    def make_circles(self):
        for i in range(self.num_circles):
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            circle = codesters.Circle(x, y, small_circle_size)
            rgb = self.random_color()
            circle.set_color(rgb[0], rgb[1], rgb[2])
            velx = random.randint(-3, 3)
            velx = 1 if velx == 0 else velx
            vely = random.randint(-3, 3)
            vely = 1 if vely == 0 else vely
            circle.set_x_speed(velx)
            circle.set_y_speed(vely)
            circle.is_big = False
            circle.event_collision(self.circle_collision)
            self.sprites.append(circle)
            self.circles.append(circle)

    def clean_up(self):
        global level_running
        level_running = False
        for s in self.sprites:
            stage.remove_sprite(s)
        self.circles = []
        self.sprites = []
        stage.event_click(None)

for i in range(10):
    l = Level(10 + i * 2, 3 + i * 2)
    lm.add_level(l)
lm.next_level()


