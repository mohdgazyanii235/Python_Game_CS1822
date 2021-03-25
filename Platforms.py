import Entity
import VectorClass


class Platforms(Entity.Entity):
    queued_direction = ""
    direction = 0
    speed = 0

    def __init__(self, platform_sprite, speed):
        self.speed = speed
        super().__init__(platform_sprite)

    def update(self, canvas):
        super().add(VectorClass.Vector(-1, 0).multiply(self.speed))
        self.movement_sprite.draw(canvas, super().get_p())
