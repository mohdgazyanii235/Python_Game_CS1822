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
        self.movement_sprite = Spritesheet.Spritesheet(movement_imgurl, movement_columns,
                                                       movement_rows, movement_frame_duration, movement_dest_centre,
                                                       movement_dest_size, movement_cells)

    def draw(self, canvas):
        print("Ran in entity")
        self.movement_sprite.draw(canvas)
        # if self.movement_count == len(self.movement_cycle):
        #     self.movement_count = 1
        #
        # window.blit(pygame.transform.scale((self.movement_cycle[self.movement_count]), (186, 106)), (500, 350))
        #
        # self.movement_count += 1
