import Entity
import VectorClass


class Drone(Entity.Entity):

    skid_value = 0

    def __init__(self, movement_imgurl, movement_columns,
                 movement_rows, movement_frame_duration, movement_dest_centre, movement_dest_size, movement_cells,
                 movement_loop, speed):

        super().__init__(movement_imgurl, movement_columns,
                         movement_rows, movement_frame_duration, movement_dest_centre, movement_dest_size,
                         movement_cells, movement_loop)

        self.speed = speed

    def update(self, canvas, moving_left=False, moving_right=False, moving_up=False, moving_down=False):

        if moving_left:
            self.move_left()

        if moving_right:
            self.move_right()

        if moving_up:
            self.move_up()

        if moving_down:
            self.move_down()

        self.skid()

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
        if self.skid_value > 0:
            super().add(VectorClass.Vector(1, 0).multiply(self.skid_value))
            self.skid_value -= 0.25
            if self.skid_value < 0:
                self.skid_value = 0
        elif self.skid_value < 0:
            super().add(VectorClass.Vector(1, 0).multiply(self.skid_value))
            self.skid_value += 0.25
            if self.skid_value > 0:
                self.skid_value = 0



