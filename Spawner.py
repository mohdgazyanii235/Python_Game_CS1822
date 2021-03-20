import EnemyDrone
import random
import Spritesheet

counter = 0


class Spawner:
    spawner_width = 0
    spawner_height = 0
    enemies = []
    counter = 0
    spawn_rate = 0
    maximum = 0
    type = ""
    sprite_clock = 0

    # declaration
    def __init__(self, maximum, spawn_rate, type, spawner_width, spawner_height, frame_duration):
        self.spawn_rate = spawn_rate
        self.maximum = maximum
        self.type = type
        self.spawner_width = spawner_width
        self.spawner_height = spawner_height
        self.frame_duration = frame_duration

    # Updates and when counter passes certain point - enemy spawned and added to list
    def check_spawn(self, current_enemies):
        self.counter += 1
        # if counter gets to 150, drone is created
        if (self.counter % self.spawn_rate == 0) and (len(current_enemies) <= self.maximum):
            # Creating stats
            # Creating spritesheet

            if self.type == "drone":
                x = random.randint(80, self.spawner_width - 80)
                y = random.randint(5, self.spawner_height // 2.5)
                enemy_drone_sprite = Spritesheet.Spritesheet("sprite_assets/enemy_sprites/SimpleEnemyDroneSS.png", 4, 2,
                                                             self.frame_duration, (x, y), (150, 80), 8, True)

                drone = EnemyDrone.EnemyDrone(enemy_drone_sprite, self.spawner_width, self.spawner_height, 5)
                current_enemies.append(drone)


        # if counter % 120 == 0:
        #     # Creating stats
        #     x = random.randint(80, 180)
        #     y = random.randint(self.HEIGHT // 1.2, self.HEIGHT - 20)
        #     speed = (random.randint(10, 60)) * 0.1
        #     enemy_human_sprite = Spritesheet.Spritesheet("sprite_assets/enemy_sprites/HumanSS.png", 4, 2,
        #                                                  self.sprite_clock.frame_duration,
        #                                                  (x, y), (50, 85), 8, True)
        #     human = enemies.enemyHuman(enemy_human_sprite, self.WIDTH, self.HEIGHT, speed)
        #     self.enemies.append(human)

        return current_enemies




