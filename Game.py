import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import Clock
import Menu
import Player
import enemies
import Spritesheet


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
        # Clears any game entities and opens the start menu
        self.player = None
        self.at_start_menu = True
        self.enemies.clear()
        self.level_elements.clear()
        self.game_frame.set_keydown_handler(self.start_menu.keyDown)

    def to_game(self):
        # Closes the start menu and goes to the game
        self.at_start_menu = False
        player_sprite = Spritesheet.Spritesheet("sprite_assets/player_sprite/DroneSSTransparent.png", 4, 8,
                                                self.sprite_clock.frame_duration,
                                                (self.WIDTH / 2, self.HEIGHT / 2), (320, 83.2), 32, True)
        self.player = Player.Player(player_sprite, self.WIDTH, self.HEIGHT, 6.5)
        self.game_frame.set_keyup_handler(self.player.keyUp)
        self.game_frame.set_keydown_handler(self.player.keyDown)

    def update(self, canvas):

        self.sprite_clock.tick()

        if self.at_start_menu:
            # Updates menu screen if menu is open
            if not self.start_menu.start_game_request:
                # If start game hasn't been pressed this flag will be false
                self.start_menu.update(canvas)
            else:
                # Otherwise start the game
                self.start_menu.start_game_request = False
                self.to_game()

            if self.start_menu.exit_request:
                # If the retire button is pressed the game is closed
                self.game_frame.stop()

        else:
            if self.player.exit_request:
                # If x has been pressed this will be true, and it will be returned to the main menu
                self.to_main_menu()

            else:
                self.player.update(canvas)
                for enemy in self.enemies:
                    # Updates all enemies in the game
                    enemy.update()