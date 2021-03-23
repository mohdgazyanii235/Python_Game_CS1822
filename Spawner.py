import EnemyDrone
import EnemyHuman
import random
import Spritesheet
import Platforms

class Spawner:
    spawner_width = 0
    spawner_height = 0
    enemies = []
    counter = 0
    spawn_rate = 0
    maximum = 0
    type = ""
    sprite_clock = 0
    WIDTH = 1200
    HEIGHT = 750

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

        if (self.counter % self.spawn_rate == 0) and (len(current_enemies) <= self.maximum):
            # Every time the spawn_rate is reached and the current number of entities is less than the maximum
            # add an entity of the corresponding type to the list

            if self.type == "drone":
                # Adds a drone if the spawner is set to spawn them
                x = random.randint(80, self.spawner_width - 80)
                y = random.randint(5, self.spawner_height // 2.5)
                enemy_drone_sprite = Spritesheet.Spritesheet("sprite_assets/enemy_sprites/SimpleEnemyDroneSS.png", 4, 2,
                                                             self.frame_duration, (x, y), (150, 80), 8, True)

                drone = EnemyDrone.EnemyDrone(enemy_drone_sprite, self.spawner_width, self.spawner_height, 5)
                current_enemies.append(drone)
                #Adds it to the local list

        return current_enemies

    def initial_spawn(self):
        #spawn platforms
        platforms = []
        #spawn 4 platforms
        for i in range (0, 4):
            x = random.randint(80, 180)
            y = random.randint(self.HEIGHT // 1.2, self.HEIGHT - 20)
            platform_sprite = Spritesheet.Spritesheet("sprite_assets/environment_sprites/BlockSS.png", 4, 3,
                                                         self.frame_duration, (x, y), (50, 85), 12, True)
            platform = Platforms.platform(platform_sprite, self.WIDTH, self.HEIGHT)
            platforms.append(platform)
        return platforms





