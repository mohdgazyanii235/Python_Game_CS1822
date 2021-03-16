import Player
import enemies
import random

#prevent from crash
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Clock:
    frame_duration = 1

    def __init__(self):
        self.time = 0
        frame_duration = 1

    def tick(self):
        self.time += 1

    def transition(self, frame_duration):
        if self.tick == frame_duration:
            return True

#used for drones
counter = 0

class Menu:
    start_btn = None
    retire_btn = None
    selector = None
    selection_num = 0
    button_selected = False

    def __init__(self, width, height):
        self.start_btn = simplegui._load_local_image("sprite_assets/menu_assets/PyGameStartBtn.png")
        self.retire_btn = simplegui._load_local_image("sprite_assets/menu_assets/PyGameRetireBtn.png")
        self.selector = simplegui._load_local_image("sprite_assets/menu_assets/PyGameMenuSelector.png")
        self.width = width
        self.height = height

    def update(self, canvas):
        button_dimensions = (self.start_btn.get_width(), self.start_btn.get_height())

        canvas.draw_image(self.start_btn, (button_dimensions[0] / 2, button_dimensions[1] / 2), button_dimensions,
                          (self.width / 2, self.height / 2 - 60), button_dimensions)

        canvas.draw_image(self.retire_btn, (button_dimensions[0] / 2, button_dimensions[1] / 2), button_dimensions,
                          (self.width / 2, self.height / 2 + 60), button_dimensions)

        selector_dimensions = (self.selector.get_width(), self.selector.get_height())

        if self.selection_num == 0:
            canvas.draw_image(self.selector, (selector_dimensions[0] / 2, selector_dimensions[1] / 2),
                              selector_dimensions, (self.width / 2 - button_dimensions[0] - 35, self.height / 2 - 60),
                              button_dimensions)
            if self.button_selected:
                self.button_selected = False
                start_game()

        elif self.selection_num == 1:
            canvas.draw_image(self.selector, (selector_dimensions[0] / 2, selector_dimensions[1] / 2),
                              selector_dimensions, (self.width / 2 - button_dimensions[0] - 35, self.height / 2 + 60),
                              button_dimensions)
            if self.button_selected:
                frame.stop()

    def keyDown(self, key):

        if key == simplegui.KEY_MAP['up']:
            if self.selection_num == 0:
                self.selection_num = 1
            else:
                self.selection_num -= 1

        if key == simplegui.KEY_MAP['down']:
            if self.selection_num == 1:
                self.selection_num = 0
            else:
                self.selection_num += 1

        if key == simplegui.KEY_MAP['space']:
            self.button_selected = True


WIDTH = 1200
HEIGHT = 750

entities = []

frame = simplegui.create_frame("Name Of The Game...", WIDTH, HEIGHT)
Clock()


def open_menu():
    for i in range(len(entities)):
        entities.pop(i)

    menu = Menu(WIDTH, HEIGHT)
    frame.set_keydown_handler(menu.keyDown)
    entities.append(menu)

#enemy drone. Randoms location and sets it there
def draw_drone():
    width = random.randint(80, WIDTH-80)
    height = random.randint(5, HEIGHT // 2.5)
    drone = enemies.enemyDrone("sprite_assets/helicopter_assets/HelicopterSS.png", 4, 8, Clock.frame_duration,
                           (width, height), (320, 83.2), 32, True, 1)
    return drone


def start_game():
    player = Player.Player("sprite_assets/player_sprite/DroneSSTransparent.png", 4, 8, Clock.frame_duration,
                           (WIDTH / 2, HEIGHT / 2), (320, 83.2), 32, True, 1)

    entities.pop(0)
    #draws the drone and adds it to the entities
    drone = draw_drone()
    entities.append(drone)
    entities.append(player)
    frame.set_keydown_handler(player.keyDown)
    frame.set_keyup_handler(player.keyUp)


def draw_entities(canvas):
    #after 300 miliseconds, new helicopter is created and counter resets
    global counter
    counter += 1
    if counter == 300:
        drone = draw_drone()
        entities.append(drone)
        counter = 0


    if isinstance(entities[0], Player.Player) and entities[0].get_exit_request():
        open_menu()

    for entity in entities:
        entity.update(canvas)


frame.set_canvas_background('white')
frame.set_draw_handler(draw_entities)

open_menu()

frame.start()