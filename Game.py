import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import Clock
import Menu
import Player
import EnemyDrone
import Spritesheet
import EnemyShot
import Spawner


class Game:
    WIDTH = 1200
    HEIGHT = 750

    start_menu = None
    at_start_menu = True

    game_over_menu = None
    player = None
    enemy_drones = []
    enemy_humans = []
    early_warning_targets = []
    level_elements = []

    enemy_drone_spawner = None
    enemy_human_spawner = None

    spawner = None

    sprite_clock = None

    game_frame = None

    level_background = None

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
        self.enemy_drones.clear()
        self.level_elements.clear()
        self.game_frame.set_keydown_handler(self.start_menu.keyDown)

    def to_game(self):
        # Closes the start menu and goes to the game
        # It only makes first spawn
        self.at_start_menu = False
        player_sprite = Spritesheet.Spritesheet("sprite_assets/player_sprite/DroneSSTransparent.png", 4, 8,
                                                self.sprite_clock.frame_duration,
                                                (self.WIDTH / 2, self.HEIGHT / 2), (320, 83.2), 32, True)
        self.player = Player.Player(player_sprite, self.WIDTH, self.HEIGHT, 6.5)

        # Adds a player

        self.game_frame.set_keyup_handler(self.player.keyUp)
        self.game_frame.set_keydown_handler(self.player.keyDown)

        # Sets key handlers to player functions

        self.level_up()
        # Runs first level_up() to add spawners

        self.level_background = simplegui._load_local_image("sprite_assets/level_backgrounds/PyGameCityBackground.png")

    def level_up(self):
        # Where we will put any level ups which change the spawners
        self.enemy_drone_spawner = Spawner.Spawner(10, 300, "drone", self.WIDTH, self.HEIGHT / 2,
                                                   self.sprite_clock.frame_duration)
        # Creates a spawner for the drones

    def enemy_collision_prevent(self):
        for subject in self.enemy_drones:
            subject_enemy_left_x = subject.get_x() - 50
            # Added a padding on both sides of the enemy drones so they don't actually collide.
            subject_enemy_right_x = subject.get_x() + 50
            subject_enemy_top_y = subject.get_y() - 85
            subject_enemy_bottom_y = subject.get_y() + 85
            for comparison in self.enemy_drones:
                comparison_enemy_left_x = comparison.get_x() - 50
                comparison_enemy_right_x = comparison.get_x() + 50
                comparison_enemy_top_y = comparison.get_y() - 85
                comparison_enemy_bottom_y = comparison.get_y() + 85
                if ((subject_enemy_right_x >= comparison_enemy_left_x) and
                    (subject_enemy_right_x <= comparison_enemy_right_x)) and \
                        ((subject_enemy_bottom_y >= comparison_enemy_top_y) and
                         (subject_enemy_bottom_y <= comparison_enemy_bottom_y)):
                    subject.set_direction(subject.get_opposite_direction())
                    comparison.set_direction(comparison.get_opposite_direction())
                elif ((subject_enemy_left_x <= comparison_enemy_right_x) and
                      (subject_enemy_left_x >= comparison_enemy_left_x)) and \
                    ((subject_enemy_bottom_y >= comparison_enemy_top_y) and
                     (subject_enemy_bottom_y <= comparison_enemy_bottom_y)):
                    subject.set_direction(subject.get_opposite_direction())
                    comparison.set_direction(comparison.get_opposite_direction())

    i_dont_know_what_to_call_this_variable = 0
    # Just please don't ask me why I put this here, trust me even I don't know. Let's just say it brings me good luck.

    def update(self, canvas):
        self.sprite_clock.tick()

        if self.i_dont_know_what_to_call_this_variable > 0:
            index_of_hit = self.player.player_drone_collision(self.enemy_drones)
            if index_of_hit is not None and self.player.is_firing:
                print(len(self.enemy_drones))
                self.enemy_drones.pop(index_of_hit)
            # Checks if player has shot a drone, then removes it

            self.player.is_firing = False
            self.enemy_collision_prevent()

        if self.at_start_menu:
            # Updates menu screen if menu is open
            if not self.start_menu.start_game_request:
                # If start game hasn't been pressed this flag will be false
                self.start_menu.update(canvas)
            else:
                # Otherwise start the game
                self.start_menu.start_game_request = False
                self.to_game()
                self.i_dont_know_what_to_call_this_variable += 1
                print(self.player.player_drone_collision(self.enemy_drones))

            if self.start_menu.exit_request:
                # If the retire button is pressed the game is closed
                self.game_frame.stop()

        # this is where the game loop is.
        else:
            canvas.draw_image(self.level_background, (self.level_background.get_width() / 2,
                                                      self.level_background.get_height() / 2),
                              (self.level_background.get_width(), self.level_background.get_height()),
                              (self.WIDTH / 2, self.HEIGHT / 2), (self.WIDTH * 0.9, self.HEIGHT * 0.9))

            index_of_hit = self.player.player_drone_collision(self.enemy_drones)
            if index_of_hit is not None and self.player.is_firing:
                print(len(self.enemy_drones))
                self.enemy_drones.pop(index_of_hit)
            # Checks if player has shot a drone, then removes it

            self.player.is_firing = False


            if self.player.exit_request:
                # If x has been pressed this will be true, and it will be returned to the main menu
                self.to_main_menu()

            else:
                self.enemy_drones = self.enemy_drone_spawner.check_spawn(self.enemy_drones)

                for i in range(len(self.enemy_drones)):
                    # Updates all enemy drones in the game

                    # Updates remove request for when enemies are off the screen, e.g. humans running off screen
                    if self.enemy_drones[i].get_x() >= self.WIDTH:
                        self.enemy_drones[i].remove_request = True 

                    if self.enemy_drones[i].remove_request:
                        # Removes any drones with a removal request set to true
                        self.enemy_drones.pop(i)
                    else:
                        # Updates the enemy drone currently pointed at
                        self.enemy_drones[i].update(canvas)

                self.player.update(canvas)

                for i in range(len(self.early_warning_targets)):
                    # Loops through any of the enemy's shots
                    if self.early_warning_targets[i].remove_request:
                        # Removes any shots with a removal request set to true
                        self.early_warning_targets.pop(i)
                    else:
                        # Updates the current enemy shot
                        self.early_warning_targets[i].update(canvas)
