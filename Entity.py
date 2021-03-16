import VectorClass
import Spritesheet
from Clock import Clock

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Entity(VectorClass.Vector):
    movement_sprite = None
    # changing death_animation to the helicopter death for the sake of testing
    death_animation = "sprite_assets/player_sprite/HelicopterDeathSS.png"
    remove_request = False
    rotation = 0

    def __init__(self, movement_img_url, movement_columns,
                 movement_rows, movement_frame_duration, movement_dest_centre, movement_dest_size, movement_cells,
                 movement_loop):
        super().__init__(movement_dest_centre[0], movement_dest_centre[1])
        self.movement_sprite = Spritesheet.Spritesheet(movement_img_url, movement_columns,
                                                       movement_rows, movement_frame_duration, super().get_p(),
                                                       movement_dest_size, movement_cells, movement_loop)

    def death(self):
        print(self.death_animation)
        self.movement_sprite.movement_img_url = self.death_animation
        self.movement_sprite.movement_columns = 4
        self.movement_sprite.movement_rows = 5
        self.movement_sprite.movement_frame_duration = Clock.frame_duration
        self.movement_sprite.movement_cells = 20
        self.movement_sprite.movement_loop = False
        self.remove_sprite = True
