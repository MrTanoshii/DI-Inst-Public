import sys

import pygame
from pygame.locals import *
from constants import Constants as C

from classes.game_manager import GameManager


if __name__ == "__main__":
    # Init PyGame
    pygame.init()

    # Setup the clock and refresh rate
    fps = pygame.time.Clock()
    fps.tick(C.Window.fps)

    # Setup the window
    display_surface = pygame.display.set_mode(C.Window.resolution)
    pygame.display.set_caption(C.Window.title)

    game_manager = GameManager()

    # Main loop
    while True:
        # Update entity loops
        game_manager.update(display_surface)
        pygame.display.update()

        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == C.Hotkey.quit:
                    pygame.quit()
