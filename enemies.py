import DroneEntity
import random
import VectorClass
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class enemyDrone(DroneEntity.Drone):
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False
    queued_direction = ""
    size_multiplier = 1

    direction = 0
    direction_duration = 0

    def __init__(self, enemy_drone_sprite, frame_width, frame_height, speed):

        super().__init__(enemy_drone_sprite, frame_width, frame_height, speed)

    def get_x(self):
        return super().get_p()[0]

    def get_y(self):
        return super().get_p()[1]

    def update(self, canvas):

        if self.direction_duration == 0:

            self.moving_up = False
            self.moving_down = False
            self.moving_right = False
            self.moving_left = False

            self.direction = random.randint(0, 8)
            if self.direction == 0:
                self.direction_duration = 30
            else:
                self.direction_duration = random.choice([25, 50, 75])

        if self.direction == 1:
            self.moving_up = True

        elif self.direction <= 2:
            self.moving_up = True
            self.moving_right = True

        elif self.direction == 3:
            self.moving_right = True

        elif self.direction == 4:
            self.moving_right = True
            self.moving_down = True

        elif self.direction == 5:
            self.moving_down = True

        elif self.direction == 6:
            self.moving_down = True
            self.moving_left = True

        elif self.direction == 7:
            self.moving_left = True

        elif self.direction == 8:
            self.moving_left = True
            self.moving_up = True

        self.direction_duration -= 1

        # limits drones height
        if super().get_p()[1] > 750 / 2:
            self.moving_down = False

        super().update(canvas, self.moving_left, self.moving_right, self.moving_up, self.moving_down)



# to do: enemy human should inherit enemyDrone all except update()
class enemyHuman(DroneEntity.Drone):
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
