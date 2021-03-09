import os
import pygame
import sprite_assets
import VectorClass
import Spritesheet

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Entity(VectorClass.Vector):

    movement_sprite = None
    death_animation = None
    speed = 1

    def __init__(self, movement_imgurl, movement_columns,
                 movement_rows, movement_frame_duration, movement_dest_centre, movement_dest_size, movement_cells, movement_loop,
                 speed=1):

        super().__init__(movement_dest_centre[0], movement_dest_centre[1])

        self.speed = speed

        self.movement_sprite = Spritesheet.Spritesheet(movement_imgurl, movement_columns,
                                                       movement_rows, movement_frame_duration, super().get_p(),
                                                       movement_dest_size, movement_cells, movement_loop)

    def update(self, canvas):
        print(super().get_p())
        self.movement_sprite.draw(canvas, super().get_p())

    def move_up(self):
        super().add(VectorClass.Vector(0, -1).multiply(self.speed))

    def move_down(self):
        super().add(VectorClass.Vector(0, 1).multiply(self.speed))

    def move_right(self):
        super().add(VectorClass.Vector(1, 0).multiply(self.speed))

    def move_left(self):
        super().add(VectorClass.Vector(-1, 0).multiply(self.speed))