import enemies
import random
import Spritesheet

counter = 0

class Spawner:

    WIDTH = 1200
    HEIGHT = 750

    #declaration
    def __init__(self):
        self.enemies = []

    #Updates and when counter passes certain point - enemy spawned and added to list
    def update(self):
        global counter, index
        counter += 1
        #if counter gets to 150, drone is created
        if counter == 200:
            counter = 0
            #Creating stats
            x = random.randint(80, self.WIDTH - 80)
            y = random.randint(5, self.HEIGHT // 2.5)
            #Creating spritesheet
            enemy_drone_sprite = Spritesheet.Spritesheet("sprite_assets/enemy_sprites/SimpleEnemyDroneSS.png", 4, 2,
                                                         self.sprite_clock.frame_duration,
                                                         (x, y), (150, 80), 8, True)
            drone = enemies.enemyDrone(enemy_drone_sprite, self.WIDTH, self.HEIGHT, 5)
            self.enemies.append(drone)
        #if counter gets to 300, human is created
        if counter % 120 == 0:
            #Creating stats
            x = random.randint(80, 180)
            y = random.randint(self.HEIGHT // 1.2, self.HEIGHT - 20)
            speed = (random.randint(10, 60)) * 0.1
            enemy_human_sprite = Spritesheet.Spritesheet("sprite_assets/enemy_sprites/HumanSS.png", 4, 2,
                                                         self.sprite_clock.frame_duration,
                                                         (x, y), (50, 85), 8, True)
            human = enemies.enemyHuman(enemy_human_sprite, self.WIDTH, self.HEIGHT, speed)
            self.enemies.append(human)

    #returns list of enemies
    def get(self):
        return self.enemies

    #deletes all enemies
    def delete_all(self):
        self.enemies = []

    #deletes particular enemy accroding to index
    def delete(self, index):
        alive_enemies = []
        for i in self.enemies:
            if i != index:
                alive_enemies.append[i]
        self.enemies = alive_enemies