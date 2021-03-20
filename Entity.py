import VectorClass
import Spritesheet
from Clock import Clock
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Entity(VectorClass.Vector):
    movement_sprite = None
    # changing death_animation to the helicopter death for the sake of testing
    death_sprite = None
    remove_request = False
    rotation = 0

    def __init__(self, movement_sprite):
        super().__init__(movement_sprite.dest_centre[0], movement_sprite.dest_centre[1])
        self.movement_sprite = movement_sprite

    def death(self):
        pass
