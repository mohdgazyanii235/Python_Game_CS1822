import Entity
import VectorClass


class EnemyHuman(Entity.Entity):
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False
    queued_direction = ""
    size_multiplier = 1
    direction = 0
    speed = 0

    def __init__(self, enemy_human_sprite, speed):
        self.speed = speed
        super().__init__(enemy_human_sprite)

    def update(self, canvas):
        super().add(VectorClass.Vector(1, 0).multiply(self.speed))
        self.movement_sprite.draw(canvas, super().get_p())
        coord = super().get_p()
        if coord[0] > 1180:
            super().add(VectorClass.Vector(-1, 0).multiply(self.speed))

