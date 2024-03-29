import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import Clock
import EnemyHuman
import Menu
import Player
import EnemyDrone
import Spritesheet
import EnemyShot
import Spawner
import random
import ScoreBoard
import math


class Game:
    WIDTH = 1200
    HEIGHT = 750

    start_menu = None
    at_start_menu = True
    at_high_score = False
    game_over_menu = None

    player = None
    enemy_drones = []
    enemy_humans = []
    early_warning_targets = []
    level_elements = []

    enemy_drone_spawner = None
    enemy_human_spawner = None

    sprite_clock = None

    game_frame = None

    level_background = None
    score = 0

    mixer = None

    game_over_img = simplegui._load_local_image("sprite_assets/game_over_screen/PyGameDeathScreen.png")

    def __init__(self):

        self.start_menu = Menu.Menu(self.WIDTH, self.HEIGHT)

        self.sprite_clock = Clock.Clock()

        self.game_frame = simplegui.create_frame("ASSASSCIINATION", self.WIDTH, self.HEIGHT)

        self.game_frame.set_canvas_background('white')
        self.game_frame.set_draw_handler(self.update)
        self.to_main_menu()
        self.game_frame.start()
        self.score = 0

    def to_main_menu(self):
        # Clears any game entities and opens the start menu
        self.player = None
        self.at_start_menu = True
        self.enemy_drones.clear()
        self.level_elements.clear()
        self.enemy_humans.clear()
        self.early_warning_targets.clear()
        self.game_frame.set_keydown_handler(self.start_menu.keyDown)

    def to_game(self):
        # Closes the start menu and goes to the game
        # It only makes first spawn
        self.at_start_menu = False
        player_sprite = Spritesheet.Spritesheet("sprite_assets/player_sprite/DroneSSTransparent.png", 4, 10,
                                                self.sprite_clock.frame_duration,
                                                (self.WIDTH / 2, self.HEIGHT / 2), (320 * 0.7, 83.2 * 0.7), 40, True)
        self.player = Player.Player(player_sprite, self.WIDTH, self.HEIGHT, 6.5)

        # Adds a player

        self.game_frame.set_keyup_handler(self.player.keyUp)
        self.game_frame.set_keydown_handler(self.player.keyDown)

        # Sets key handlers to player functions

        self.load_level()
        # Runs first level_up() to add spawners

        self.level_background = simplegui._load_local_image("sprite_assets/level_backgrounds/PyGameCityBackground.png")

    def load_level(self):
        # Where we will put any level ups which change the spawners
        self.enemy_drone_spawner = Spawner.Spawner(10, 300, "drone", self.WIDTH, self.HEIGHT / 2,
                                                   self.sprite_clock.frame_duration)

        self.enemy_human_spawner = Spawner.Spawner(10, 100, "human", self.WIDTH, self.HEIGHT / 2,
                                                   self.sprite_clock.frame_duration)

        self.platform = Spawner.Spawner(20, 300, "platform", self.WIDTH, self.HEIGHT / 2,
                                        self.sprite_clock.frame_duration)

        self.score = 0

        # Creates a spawner for the drones

    @staticmethod
    def collision_checker(x1, y1, x2, y2):
        constant = 150
        if ((x1 + constant >= x2 - constant) and (x1 + constant <= x2 + constant)) and (
                (y2 - constant <= y1 + constant <= y2 + constant) or (
                y2 + constant >= y1 - constant >= y2 - constant)):
            return True
        elif ((x1 - constant <= x2 + constant) and (x1 - constant >= x2 - constant)) and (
                (y2 - constant <= y1 + constant <= y2 + constant) or (
                y2 + constant >= y1 - constant >= y2 - constant)):
            return True
        else:
            return False

    def enemy_collision_prevent(self, canvas):
        for index1, subject in enumerate(self.enemy_drones):
            subject_x = subject.get_x()
            subject_y = subject.get_y()
            for index2, comparison in enumerate(self.enemy_drones):
                if index1 == index2:
                    continue
                else:
                    comparison_x = comparison.get_x()
                    comparison_y = comparison.get_y()
                    if self.collision_checker(subject_x, subject_y, comparison_x,
                                              comparison_y):  # True if there is a collision.

                        subject.move_opposite(canvas)
                        comparison.move_opposite(canvas)

    def check_player_hit(self, shot_pos, radius):
        player_pos = self.player.get_p()
        if (player_pos[0] - shot_pos[0]) ** 2 + (player_pos[1] - shot_pos[1]) ** 2 < radius ** 2:
            self.player.take_damage()

    @staticmethod
    def find_angle(human, platform):
        start_x = human.get_x()
        start_y = human.get_y()+25
        try:
            angle = math.atan((start_y - platform.get_y()-30) / (start_x - platform.get_x()))
        except:
            angle = math.pi / 2

        if platform.get_y()-30 < start_y and platform.get_x() > start_x:
            angle = abs(angle)
        elif platform.get_y()-30 < start_y and platform.get_x() < start_x:
            angle = math.pi - angle
        elif platform.get_y()-30 > start_y and platform.get_x() < start_x:
            angle = math.pi + abs(angle)
        elif platform.get_y()-30 > start_y and platform.get_x() > start_x:
            angle = (math.pi * 2) - angle

        return angle*1.2

    def make_enemies_jump(self):
        jump_height_constant = 200
        jump_width_constant = 100
        for enemy_human in self.enemy_humans:
            for platform in self.level_elements:
                if enemy_human.get_x() >= platform.get_x()+80:
                    continue
                if enemy_human.get_y()+25 - jump_height_constant > platform.get_y()-20:
                    continue
                if (platform.get_x()-80) - enemy_human.get_x() > jump_width_constant:
                    continue
                else:
                    enemy_human.set_jump(platform.get_y()-40, self.find_angle(enemy_human, platform))

    def add_enemy_shot(self):
        x_accuracy = random.randint(-300, 300)
        y_accuracy = random.randint(-300, 300)
        shot_direction = random.randint(0, 2)
        new_shot_pos = list(self.player.get_p())

        if shot_direction == 0:
            new_shot_pos[0] += x_accuracy
        elif shot_direction == 1:
            new_shot_pos[1] += y_accuracy
        elif shot_direction == 2:
            new_shot_pos[0] += x_accuracy
            new_shot_pos[1] += y_accuracy

        self.early_warning_targets.append(EnemyShot.enemyShot(50, 100, tuple(new_shot_pos)))

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
                # print(self.player.player_drone_collision(self.enemy_drones))

            if self.start_menu.exit_request:
                # If the retire button is pressed the game is closed
                self.game_frame.stop()

        # this is where the game loop is.
        elif self.player is None:
            self.to_main_menu()
            self.start_menu.current_screen = "highscore"
            self.start_menu.highscore_game_over = True
            self.start_menu.highscore_got_highscore = self.start_menu.highscore_board.compare_new_score(self.score)
        else:
            canvas.draw_image(self.level_background, (self.level_background.get_width() / 2,
                                                      self.level_background.get_height() / 2),
                              (self.level_background.get_width(), self.level_background.get_height()),
                              (self.WIDTH / 2, self.HEIGHT / 2), (self.WIDTH * 0.9, self.HEIGHT * 0.9))

            # Checks if player has shot a drone, then removes it
            if len(self.enemy_humans) > 0: # enemy humans have started to come in.
                self.make_enemies_jump()

            index_of_hit_drone = self.player.player_drone_collision(self.enemy_drones)
            index_of_hit_human = self.player.player_drone_collision(self.enemy_humans)
            if index_of_hit_drone is not None and self.player.is_firing:
                self.enemy_drones[index_of_hit_drone].death()
                self.score += 10
                hit = simplegui._load_local_sound('audio_assets/sound_effects/hit2.wav')
                hit.play()


            elif index_of_hit_human is not None and self.player.is_firing:
                self.enemy_humans[index_of_hit_human].death()
                self.score += 20
                hit = simplegui._load_local_sound('audio_assets/sound_effects/hit.wav')
                hit.play()



            # Checks if player has shot a drone, then removes it

            self.player.is_firing = False
            #self.enemy_collision_prevent(canvas)

            self.player.is_firing = False

            if self.player.exit_request:
                # If x has been pressed this will be true, and it will be returned to the main menu
                self.to_main_menu()


            else:
                self.enemy_drones = self.enemy_drone_spawner.check_spawn(self.enemy_drones)
                self.enemy_humans = self.enemy_human_spawner.check_spawn(self.enemy_humans)
                self.level_elements = self.platform.check_spawn(self.level_elements)

                for index, i in enumerate(self.enemy_drones):
                    # Updates all enemy drones in the game

                    # Updates remove request for when enemies are off the screen, e.g. humans running off screen
                    if i.get_x() >= self.WIDTH:
                        i.remove_request = True

                    if i.remove_request:
                        # Removes any drones with a removal request set to true
                        self.enemy_drones.pop(index)
                    else:
                        # Updates the enemy drone currently pointed at
                        i.update(canvas)
                        if i.is_firing:
                            self.add_enemy_shot()
                            i.is_firing = False

                for index, i in enumerate(self.enemy_humans):
                    if i.get_p()[0] > self.WIDTH + 30:
                        i.remove_request = True
                        self.score -= 20
                    if i.remove_request:
                        self.enemy_humans.pop(index)
                    i.update(canvas)

                for index, i in enumerate(self.level_elements):
                    if i.get_p()[0] < -200:
                        self.level_elements.pop(index)
                    i.update(canvas)

                floor = "_" * self.WIDTH
                canvas.draw_text(floor, (0, self.HEIGHT - 55), 10, "Black", "monospace")

                self.player.update(canvas)

                for index, i in enumerate(self.early_warning_targets):
                    # Loops through any of the enemy's shots
                    if i.remove_request:
                        # Removes any shots with a removal request set to true
                        self.early_warning_targets.pop(index)
                    else:
                        # Updates the current enemy shot
                        i.update(canvas)
                        if i.is_detonated:
                            self.check_player_hit(i.get_p(), i.radius)

                if self.score < 0:
                    self.score = 0

                canvas.draw_text("Score:" + str(self.score), (10, self.HEIGHT - 10), 25, "Black", "monospace")
                canvas.draw_text("Lives:" + str(self.player.lives), (self.WIDTH - 130, self.HEIGHT - 10), 25,
                                 "Black", "monospace")

                if self.player.remove_request:
                    self.player = None
