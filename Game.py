import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import Clock
import Menu
import Player


class Game:

    WIDTH = 1200
    HEIGHT = 750

    start_menu = None
    at_start_menu = True

    game_over_menu = None
    player = None
    enemies = []
    level_elements = []

    sprite_clock = None

    game_frame = None

    def __init__(self):

        self.start_menu = Menu.Menu(self.WIDTH, self.HEIGHT)

        self.sprite_clock = Clock.Clock()

        self.game_frame = simplegui.create_frame("Name Of The Game...", self.WIDTH, self.HEIGHT)

        self.game_frame.set_canvas_background('white')
        self.game_frame.set_draw_handler(self.update)
        self.to_main_menu()
        self.game_frame.start()

    def to_main_menu(self):
        self.player = None
        self.at_start_menu = True
        self.enemies.clear()
        self.level_elements.clear()
        self.game_frame.set_keydown_handler(self.start_menu.keyDown)

    def to_game(self):
        self.at_start_menu = False
        self.player = Player.Player("sprite_assets/player_sprite/DroneSSTransparent.png", 4, 8,
                                    self.sprite_clock.frame_duration,
                                    (self.WIDTH / 2, self.HEIGHT / 2), (320, 83.2), 32, True, 6.5)
        self.game_frame.set_keyup_handler(self.player.keyUp)
        self.game_frame.set_keydown_handler(self.player.keyDown)

    def update(self, canvas):

        self.sprite_clock.tick()

        if self.at_start_menu:

            if not self.start_menu.start_game_request:
                self.start_menu.update(canvas)
            else:
                self.start_menu.start_game_request = False
                self.to_game()

            if self.start_menu.exit_request:
                self.game_frame.stop()

        else:
            if self.player.exit_request:
                self.to_main_menu()
            else:
                self.player.update(canvas)
                for enemy in self.enemies:
                    enemy.update()




