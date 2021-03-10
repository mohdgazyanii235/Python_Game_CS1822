import DroneEntity

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Player(DroneEntity.Drone):

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

    def update(self, canvas):
        super().update(canvas, self.moving_left, self.moving_right, self.moving_up, self.moving_down)

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['left']:
            self.moving_left = True

        if key == simplegui.KEY_MAP['right']:
            self.moving_right = True

        if key == simplegui.KEY_MAP['up']:
            self.moving_up = True

        if key == simplegui.KEY_MAP['down']:
            self.moving_down = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['left']:
            self.moving_left = False

        if key == simplegui.KEY_MAP['right']:
            self.moving_right = False

        if key == simplegui.KEY_MAP['up']:
            self.moving_up = False

        if key == simplegui.KEY_MAP['down']:
            self.moving_down = False
