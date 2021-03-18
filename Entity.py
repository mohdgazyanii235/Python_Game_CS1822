import VectorClass
import Spritesheet
from Clock import Clock
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Entity(VectorClass.Vector):
    movement_sprite = None
    # changing death_animation to the helicopter death for the sake of testing
    death_animation = "sprite_assets/player_sprite/HelicopterDeathSS.png"
    remove_request = False
    rotation = 0

    def __init__(self, sprite):
        super().__init__(sprite.dest_centre[0], sprite.dest_centre[1])
        self.movement_sprite = sprite

    def death(self):
        print(self.death_animation)
        self.movement_sprite.movement_img_url = self.death_animation
        self.movement_sprite.movement_columns = 4
        self.movement_sprite.movement_rows = 5
        self.movement_sprite.movement_frame_duration = Clock.frame_duration
        self.movement_sprite.movement_cells = 20
        self.movement_sprite.movement_loop = False
        self.remove_request = True
