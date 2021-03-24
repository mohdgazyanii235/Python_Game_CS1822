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
    parabola_constant = 0.0

    jump_destination = ()

    def __init__(self, enemy_human_sprite, speed):
        self.speed = speed
        super().__init__(enemy_human_sprite)

    def update(self, canvas):

        if self.is_jumping:
            self.jump()
        else:
            super().add(VectorClass.Vector(1, 0).multiply(self.speed))

        self.movement_sprite.draw(canvas, super().get_p())
        coord = super().get_p()
        if coord[0] > 1180:
            super().add(VectorClass.Vector(-1, 0).multiply(self.speed))

    def set_jump_location(self, jump_dest):
        current_x = self.get_p()[0]
        current_y = self.get_p()[1]

        self.jump_destination = jump_dest
        self.parabola_constant = (current_y - self.jump_destination[1]) / ((current_x - self.jump_destination[0]) ** 2)
        # Uses equation of a parabola (y = a(x-h)**2 + k) to find the constant a which is called parabola_constant
        # for the purpose of greater readability. This is done by rearranging into a = (y - k) / (x-h)**2

    def jump(self):

        current_x = self.get_p()[0]
        current_y = self.get_p()[1]

        new_y_component = (self.parabola_constant * ((current_x + 1) - self.jump_destination[0]) ** 2 +
                           self.jump_destination[1]) - current_y

        # This uses the parabolic equation a(x-h)**2 + k to calculate the next y position using the constant
        # derived at the beginning of the jump

        super().add(VectorClass.Vector(self.speed, new_y_component))

        if 2 * self.parabola_constant * (current_x - self.jump_destination[0]) > 0:
            # Uses the first derivative of the standard form of the parabolic equation 2a(x - h)
            # to check if the human is descending

            if current_y >= self.jump_destination[1]:
                # If the current y exceeds the destination y we know it has gone passed the point where the coordinate
                # is, due to the fact that that we are moving along the x axis at a speed greater than one

                displacement = self.jump_destination[1] - current_y
                super().add(VectorClass.Vector(0, displacement))

                # This then adds the displacement between the currently overextend position of the human and the
                # destination position to the human's vector, bring it back ip to where it ought to be.

                self.is_jumping = False

                # The jump is then finished, and the human returns to normal behaviour. This code only happens should
                # the human be descending, as otherwise the human would never ascend if its jumping to a higher
                # position (as in that case the starting y will always be greater than the destination y)




