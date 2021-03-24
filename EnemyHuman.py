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
    is_jumping = True

    run_once = True
    a = 0.0

    vertex = (700, 200)

    def __init__(self, enemy_human_sprite, speed):
        self.speed = speed
        super().__init__(enemy_human_sprite)

    def update(self, canvas):

        if self.is_jumping:
            self.jump()
        else:
            super().add(VectorClass.Vector(1, 0).multiply(self.speed))

        self.movement_sprite.draw(canvas, super().get_p())

    def jump(self):

        current_x = self.get_p()[0]
        current_y = self.get_p()[1]

        if self.run_once:
            self.a = (current_y - self.vertex[1]) / ((current_x - self.vertex[0])**2)
            self.run_once = False

        new_y_componant = (self.a * ((current_x + 1) - self.vertex[0])**2 + self.vertex[1]) - current_y

        super().add(VectorClass.Vector(1, new_y_componant))


