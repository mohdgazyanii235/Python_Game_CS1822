import Entity

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Player(Entity.Entity):

    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False

    def __init__(self, movement_imgurl, movement_columns,
                 movement_rows, movement_frame_duration, movement_dest_centre, movement_dest_size, movement_cells,
                 speed=1):
        super().__init__(movement_imgurl, movement_columns,
                         movement_rows, movement_frame_duration, movement_dest_centre, movement_dest_size,
                         movement_cells, speed)

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            super().move_right()
