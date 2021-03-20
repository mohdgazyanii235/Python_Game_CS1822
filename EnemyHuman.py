import DroneEntity, VectorClass


class EnemyHuman(DroneEntity.Drone):
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False
    queued_direction = ""
    size_multiplier = 1

    def __init__(self, enemy_human_sprite, frame_width, frame_height, speed):
        super().__init__(enemy_human_sprite, frame_width, frame_height, speed)

    def update(self, canvas):
        super().update(canvas, self.moving_left, self.moving_right, self.moving_up, self.moving_down)
        super().add(VectorClass.Vector(1, 0).multiply(self.speed))
