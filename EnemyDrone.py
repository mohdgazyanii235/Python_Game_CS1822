import DroneEntity
import random


class EnemyDrone(DroneEntity.Drone):
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False
    queued_direction = ""
    size_multiplier = 1
    direction = 0
    direction_duration = 0

    fire_rate = 20
    fire_count = 0
    is_firing = False
    fire_radius = 0
    fire_accuracy = 0

    def __init__(self, enemy_drone_sprite, frame_width, frame_height, speed, death_sprite=None):
        super().__init__(enemy_drone_sprite, frame_width, frame_height, speed, death_sprite)

    def get_x(self):
        return super().get_p()[0]

    def get_y(self):
        return super().get_p()[1]

    def get_direction(self):
        return self.direction

    def set_direction(self, new_direction):
        self.direction = new_direction

    def move_opposite(self, canvas):
        super().update(canvas, not self.moving_left, not self.moving_right, not self.moving_up, not self.moving_down)

    def direction_setter(self, direction):
        if direction == 1:
            self.moving_up = True

        elif direction == 2:
            self.moving_up = True
            self.moving_right = True

        elif direction == 3:
            self.moving_right = True

        elif direction == 4:
            self.moving_right = True
            self.moving_down = True

        elif direction == 5:
            self.moving_down = True

        elif direction == 6:
            self.moving_down = True
            self.moving_left = True

        elif direction == 7:
            self.moving_left = True

        elif direction == 8:
            self.moving_left = True
            self.moving_up = True

        self.direction_duration -= 1

        # limits drones height
        if super().get_p()[1] > 750 / 2:
            self.moving_down = False

    def update(self, canvas):

        if self.is_dying:
            self.death_sprite.draw(canvas, super().get_p())
            if self.death_sprite.cycle_ended:
                self.remove_request = True
        else:
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

            self.direction_setter(self.direction)

            self.fire_count += 1

            if self.fire_count % self.fire_rate == 0:
                self.is_firing = True

            super().update(canvas, self.moving_left, self.moving_right, self.moving_up, self.moving_down)
