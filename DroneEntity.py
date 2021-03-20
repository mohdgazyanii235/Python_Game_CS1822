import Entity
import VectorClass
import math


class Drone(Entity.Entity):

    skid_value = 0
    skid_value_y = 0
    bob_range = 6
    bob_value = 0
    bob_ascending = True
    frame_width = 0
    frame_height = 0
    speed = 0
    fire_allowed = False

    def __init__(self, sprite, frame_width, frame_height, speed):

        self.drone_dimensions = sprite.dest_size
        super().__init__(sprite)

        self.frame_width = frame_width
        self.frame_height = frame_height

        self.speed = speed
        self.ORIGINAL_SPEED = self.speed

    def collision_checker(self, enemy_list):
        for i in enemy_list:
            aim_x = super().get_p()[0]
            aim_y = super().get_p()[1]
            player_left_x = i.get_x()-75
            player_right_x = i.get_x()+75
            player_top_y = i.get_y() - 40
            player_bottom_y = i.get_y() + 40

            if player_left_x <= aim_x <= player_right_x and player_top_y <= aim_y <= player_bottom_y:
                return True

    def update(self, canvas, moving_left=False, moving_right=False, moving_up=False, moving_down=False):

        if super().get_p()[0] - self.drone_dimensions[0] / 2 - 6 < 0:
            # Checks if leftmost point of drone less than five pixels from the left screen boundary
            moving_left = False
            self.skid_value = 0
            # Ensures drone can't skid outside the screen boundary

        if super().get_p()[0] + self.drone_dimensions[0] / 2 + 6 > self.frame_width:
            moving_right = False
            self.skid_value = 0

        if super().get_p()[1] - self.drone_dimensions[1] / 2 - 6 < 0:
            moving_up = False
            self.skid_value_y = 0

        if super().get_p()[1] + self.drone_dimensions[1] / 2 + 6 > self.frame_height:
            moving_down = False
            self.skid_value_y = 0

        if moving_left:
            self.rotation = -math.radians(12)
            self.move_left()

        if moving_right:
            self.rotation = math.radians(12)
            self.move_right()

        if moving_up:
            self.move_up()

        if moving_down:
            self.move_down()

        if not (moving_left or moving_right):
            self.rotation = 0
            self.skid()
            # By having calling skid only when the drone isn't moving we prevent it from disrupting snappy direction
            # changes
            self.bob()
            # Starts bobbing motion when drone is stationary

        self.movement_sprite.draw(canvas, super().get_p(), self.rotation)


    def move_up(self):
        super().add(VectorClass.Vector(0, -1).multiply(self.speed))

    def move_down(self):
        super().add(VectorClass.Vector(0, 1).multiply(self.speed))

    def move_right(self):
        super().add(VectorClass.Vector(1, 0).multiply(self.speed))

    def move_left(self):
        super().add(VectorClass.Vector(-1, 0).multiply(self.speed))



    def skid(self):
        # Skid value comes from the speed; by moving at slower increments of the skid value it gives the sense
        # of skidding to a halt
        if self.skid_value > 0:
            super().add(VectorClass.Vector(1, 0).multiply(self.skid_value))
            self.skid_value -= 0.3
            # A higher value deducted from the skid_value will result in a shorter skid, a smaller value results in
            # a longer one

            if self.skid_value < 0:
                self.skid_value = 0
                # Ensures that is taking 0.25 sends the skid_value the elif statement won't run (so the drone doesn't
                # get stuck eternally skidding back and forth)

        elif self.skid_value < 0:
            super().add(VectorClass.Vector(1, 0).multiply(self.skid_value))
            self.skid_value += 0.25
            if self.skid_value > 0:
                self.skid_value = 0

        self.speed = self.ORIGINAL_SPEED

    def bob(self):

        if self.bob_ascending:
            self.bob_value += 0.2

            super().add(VectorClass.Vector(0, -0.2))

            if self.bob_value >= self.bob_range / 2:
                self.bob_ascending = False

        else:
            self.bob_value -= 0.2

            super().add(VectorClass.Vector(0, 0.2))

            if self.bob_value <= -self.bob_range / 2:
                self.bob_ascending = True
