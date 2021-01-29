import pygame
import player_sprite


class Player:
    sprite_animation = []
    cycle_count = 0

    def __init__(self):
        for x in range(1, 31, 1):
            self.sprite_animation.append(pygame.image.load("player_sprite/Screenshot_" + str(x) + ".png"))
        for x in range(10, 1, -1):
            self.sprite_animation.append(pygame.image.load("player_sprite/Screenshot_" + str(x) + ".png"))

        # Adds the animation cycle from the sprite sheet to an array

    def draw_player(self, window):
        self.cycle_count += 1
        if (self.cycle_count == 39):
            self.cycle_count = 1
        window.blit(pygame.transform.scale((self.sprite_animation[self.cycle_count]), (186, 106)), (500,350))
        # Displays player animation cycle
