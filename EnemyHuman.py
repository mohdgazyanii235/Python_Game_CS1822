import DroneEntity, VectorClass


class EnemyHuman(DroneEntity.Drone):
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False
    queued_direction = ""
    size_multiplier = 1
    direction = 0


    def __init__(self, enemy_human_sprite, frame_width, frame_height, speed):
        super().__init__(enemy_human_sprite, frame_width, frame_height, speed)

    def update(self, canvas):
        super().update(canvas, self.moving_left, self.moving_right, self.moving_up, self.moving_down)
        super().add(VectorClass.Vector(1, 0).multiply(self.speed))

    def get_x(self):
        return super().get_p()[0]

    def get_y(self):
        return super().get_p()[1]

    #Known bug: can only kill enemy[0], if that enemy goes off the screen e.g. human running no other entities can be killed

    def get_x(self):
        return super().get_p()[0]

    def get_y(self):
        return super().get_p()[1]


    def get_direction(self):
        return self.direction

    def set_direction(self, new_direction):
        self.direction = new_direction

    def get_opposite_direction(self):
        return self.direction