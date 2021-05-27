# Main program

from Colors import WHITE, SPACESHIP
from Spaceship import Spaceship
import pygame

def display_spaceship(surface, spaceship):
    pos, size = spaceship.get_pos(), spaceship.get_size()
    ship = pygame.Surface(size)
    ship.fill(SPACESHIP)
    surface.blit(ship, pos)

def main():
    pygame.init()
    window_width, window_height = window_size = (800, 1000)
    window = pygame.display
    window_surface = window.set_mode(window_size)
    window.set_caption("Space Invaders")

    spaceship = Spaceship()
    spaceship_width, spaceship_height = spaceship.get_size()
    spaceship.set_pos((window_width - spaceship_width)/2, window_height - 100)
    Running = True
    while Running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key  == pygame.K_q): quit()

        window_surface.fill(WHITE)
        display_spaceship(window_surface, spaceship)

        window.update()

if __name__ == "__main__":
    main()
