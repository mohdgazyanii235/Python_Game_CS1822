import Entity
import VectorClass
import math
import random


class EnemyHuman(Entity.Entity):
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False
    queued_direction = ""
    size_multiplier = 1
    direction = 0
    speed = 0

    is_jumping = False
    parabola_constant = 0.0
    jump_destination = ()

    x = 0
    y = 0
    time = 0
    power = 0
    angle = 0
    shoot = False
    start_x = 0
    start_y = 0
    power = 11
    dest_y = 0
    is_descending = False
    jumper = False

    def __init__(self, enemy_human_sprite, speed, death_sprite=None):
        self.speed = speed
        super().__init__(enemy_human_sprite, death_sprite)


    def get_x(self):
        return super().get_p()[0]

    def get_y(self):
        return super().get_p()[1]

    def update(self, canvas):
        if self.is_dying:
            self.death_sprite.draw(canvas, super().get_p())
            if self.death_sprite.cycle_ended:
                self.remove_request = True
        else:
            if self.is_jumping:
                self.jump()
            else:
                super().add(VectorClass.Vector(1, 0).multiply(self.speed))
            self.movement_sprite.draw(canvas, super().get_p())

    def set_jump(self, y_floor, angle):
        self.start_x = super().get_p()[0]
        self.start_y = super().get_p()[1]
        self.dest_y = y_floor
        self.angle = angle
        # self.angle = self.find_angle(super().get_p())
        if self.get_y() != y_floor:
            self.is_jumping = True

    def jump(self):
        if self.is_jumping:  # if user presses mouse button
            self.time += 0.1
            po = self.jump_path(self.time)
            x_component = po[0] - super().get_p()[0]
            y_component = po[1] - super().get_p()[1]
            super().add(VectorClass.Vector(x_component, y_component))
            if y_component > 0 and super().get_p()[1] >= self.dest_y:
                super().add(VectorClass.Vector(0, self.dest_y - super().get_p()[1] ))
                print(super().get_p()[1])
                self.is_jumping = False

    def jump_path(self, time):
        vel_x = math.cos(self.angle) * self.power
        vel_y = math.sin(self.angle) * self.power

        dist_x = vel_x * time
        dist_y = (vel_y * time) + ((-4.9 * time ** 2) / 2)

        new_x = round(dist_x + self.start_x)
        new_y = round(self.start_y - dist_y)

        return new_x, new_y

    def find_angle(self, pos):
        s_x = super().get_p()[0]
        s_y = super().get_p()[1]
        try:
            angle = math.atan((s_y - pos[1]) / (s_x - pos[0]))
        except:
            angle = math.pi / 2

        if pos[1] < s_y and pos[0] > s_x:
            angle = abs(angle)
        elif pos[1] < s_y and pos[0] < s_x:
            angle = math.pi - angle
        elif pos[1] > s_y and pos[0] < s_x:
            angle = math.pi + abs(angle)
        elif pos[1] > s_y and pos[0] > s_x:
            angle = (math.pi * 2) - angle

        return angle

    def set_jumper(self, boolean):
        self.jumper = boolean

    def is_jumper(self):
        return self.jumper
