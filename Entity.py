import os
import pygame
import sprite_assets


class Entity:
    movement_cycle = []
    death_cycle = []

    movement_count = 0
    death_count = 0

    def __init__(self, folder_name):
        # folder_name is the name of what is containing the sprite assets

        asset_path = "sprite_assets" + "/" + folder_name + "/movement_cycle"
        for filename in sorted(os.listdir(asset_path)):
            # Will loop through files in alphabetical order
            self.movement_cycle.append(pygame.image.load(asset_path + "/" + filename))

    def draw(self, window):
        if self.movement_count == len(self.movement_cycle):
            self.movement_count = 1

        window.blit(pygame.transform.scale((self.movement_cycle[self.movement_count]), (186, 106)), (500, 350))

        self.movement_count += 1
