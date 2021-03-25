# import Player
# import enemies
# import random
# import EnemyShot
# import Clock
# import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
#
# WIDTH = 1200
# HEIGHT = 750
#
# entities = []
#
# frame = simplegui.create_frame("Name Of The Game...", WIDTH, HEIGHT)
# Clock()
#
#
#
#
# # enemy drone. Randoms location and sets it there
# def draw_drone():
#     width = random.randint(80, WIDTH - 80)
#     height = random.randint(5, HEIGHT // 2.5)
#
#     return enemies.enemyDrone("sprite_assets/helicopter_assets/HelicopterSS.png", 4, 8, Clock.frame_duration,
#                                (width, height), (320, 70.2), 32, True, 6.5)
#
#
# def draw_human():
#     width = random.randint(80, 180)
#     height = random.randint(HEIGHT//1.2, HEIGHT-20)
#     speed = (random.randint(10,60))*0.1
#     #For Josh - check. Could you please optimise image. - FIXED, was to do with dimensions of image and rows & columns
#     #Know bug - human goes for some reason stops - FIXED
#     return enemies.enemyHuman("sprite_assets/enemy_sprites/HumanSS.png", 4, 3, Clock.frame_duration,
#                                (width, height), (50, 85), 12, True, speed)
#
#
# def start_game():
#     player = Player.Player("sprite_assets/player_sprite/DroneSSTransparent.png", 4, 8, Clock.frame_duration,
#                            (WIDTH / 2, HEIGHT / 2), (320, 83.2), 32, True, 6.5)
#
#     entities.pop(0)
#     entities.append(player)
#     frame.set_keydown_handler(player.keyDown)
#     frame.set_keyup_handler(player.keyUp)
#
#
# def draw_entities(canvas):
#     # Runs once per frame
#     # after 150 miliseconds, new human is created
#     # after 300 miliseconds, new helicopter is created and counter resets
#     global counter
#     counter += 1
#     if counter % 150 == 0:
#         entities.append(draw_human())
#     if counter == 300:
#         entities.append(draw_drone())
#         counter = 0
#
#
#     for entity in entities:
#         # Updates everything in the array
#         entity.update(canvas)
#
#
# frame.set_canvas_background('white')
# frame.set_draw_handler(draw_entities)
# frame.start()

import Game
from pygame import mixer

mixer.init()
mixer.music.load("audio_assets/level_music/tyrant-by-kevin-macleod-from-filmmusic-io.mp3")
mixer.music.play(loops=-1)
mixer.music.set_volume(0.06)

Game.Game()

