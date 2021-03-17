import DroneEntity
import random
import VectorClass

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#counts until spawn new enemy
counter = 0
#randoms and pulls out one of 4 options
options = 0

class enemyDrone(DroneEntity.Drone):
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False
    queued_direction = ""
    exit_request = False
    size_multiplier = 1

    def __init__(self, movement_imgurl, movement_columns,
                 movement_rows, movement_frame_duration, movement_dest_centre, movement_dest_size, movement_cells,
                 movement_loop, speed):

        super().__init__(movement_imgurl, movement_columns,
                         movement_rows, movement_frame_duration, movement_dest_centre, (movement_dest_size[0] *
                                                                                        self.size_multiplier,
                                                                                        movement_dest_size[1] *
                                                                                        self.size_multiplier),
                         movement_cells, movement_loop, speed)

        self.frame_width = movement_dest_centre[0] * 2
        self.frame_height = movement_dest_centre[1] * 2

    def update(self, canvas):
        global counter, options
        counter += 1
        super().update(canvas, self.moving_left, self.moving_right, self.moving_up, self.moving_down)
        #Spawn new drone every 180 milisec
        if counter == 180:
            options = random.randint(1, 4)
            counter = 0
        if options == 1:
            self.moving_left = True
            self.moving_right = False
            self.moving_up = False
            self.moving_bottom = False
        if options == 2:
            self.moving_left = False
            self.moving_right = True
            self.moving_up = False
            self.moving_bottom = False
        if options == 3:
            self.moving_left = False
            self.moving_right = False
            self.moving_up = True
            self.moving_bottom = False
        if options == 4:
            self.moving_left = False
            self.moving_right = False
            self.moving_up = False
            self.moving_down = True


#to do: enemy human should inherit enemyDrone all except update()
class enemyHuman(DroneEntity.Drone):
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False
    queued_direction = ""
    exit_request = False
    size_multiplier = 1

    def __init__(self, movement_imgurl, movement_columns,
                 movement_rows, movement_frame_duration, movement_dest_centre, movement_dest_size, movement_cells,
                 movement_loop, speed):

        super().__init__(movement_imgurl, movement_columns,
                         movement_rows, movement_frame_duration, movement_dest_centre, (movement_dest_size[0] *
                                                                                        self.size_multiplier,
                                                                                        movement_dest_size[1] *
                                                                                        self.size_multiplier),
                         movement_cells, movement_loop, speed)

        self.frame_width = movement_dest_centre[0] * 2
        self.frame_height = movement_dest_centre[1] * 2

    def update(self, canvas):
        super().update(canvas, self.moving_left, self.moving_right, self.moving_up, self.moving_down)
        super().add(VectorClass.Vector(1, 0).multiply(self.speed))