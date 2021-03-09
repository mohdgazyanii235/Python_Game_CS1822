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
    movement_cycle = []
    death_cycle = []
    movement_sprite = None
    death_animation = None
    movement_count = 0
    death_count = 0

    def __init__(self, movement_imgurl, movement_columns,
                 movement_rows, movement_frame_duration, movement_dest_centre, movement_dest_size, movement_cells):

        super().__init__(movement_dest_centre[0], movement_dest_centre[1])
        self.movement_sprite = Spritesheet.Spritesheet(movement_imgurl, movement_columns,
                                                       movement_rows, movement_frame_duration, super().get_p(),
                                                       movement_dest_size, movement_cells)

    def draw(self, canvas):
        self.move_up()
        print(super().get_p())
        self.movement_sprite.draw(canvas, super().get_p())

    def move_up(self):
        super().add(VectorClass.Vector(1, 0))