import pygame
import Player

WIDTH = 1000
HEIGHT = 700

pygame.init()


window = pygame.display.set_mode((WIDTH, HEIGHT))
# Sets the pygame window

pygame.display.set_caption("Sniper Game Name Placeholder")
# Name will go here

run = True

player = Player.Player()

pygame.display.update()

clock = pygame.time.Clock()

def redrawGameWindow():
    # Graphics updates handled here
    window.fill("Black")
    player.draw_player(window)
    pygame.display.update()

while run:
    # Main Game Loop

    clock.tick(25)
    # Sets Framerate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Add event handlers here (e.g: Object "Update()"s)
    redrawGameWindow()

