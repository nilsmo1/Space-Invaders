# Main program

from Colors import WHITE, SPACESHIP, RED
from Projectile import Projectile
from Spaceship import Spaceship
import pygame

def in_bounds(spaceship, window_width, spaceship_width, direction=1):
    x = spaceship.get_x()
    if direction:
        return x <= window_width-spaceship_width
    return 0 <= x

def proj_in_bounds(proj, window_height, direction):
    if direction:
        return proj.get_pos()[1] < window_height+70
    return proj.get_pos()[1] > 0

def display_projectile(surface, projectile):
    pos = projectile.get_pos()
    proj = pygame.Surface((40,70))
    proj.fill(RED)
    surface.blit(proj, pos)

def display_spaceship(surface, spaceship):
    pos, size = spaceship.get_pos(), spaceship.get_size()
    ship_bottom = pygame.Surface(size)
    ship_top = pygame.Surface((size[0]//2, size[1]))
    ship_bottom.fill(SPACESHIP)
    ship_top.fill(SPACESHIP)
    surface.blit(ship_bottom, pos)
    surface.blit(ship_top, (pos[0]+size[0]//4, pos[1]-size[1]))

def main():
    pygame.init()
    window_width, window_height = window_size = (800, 1000)
    window = pygame.display
    window_surface = window.set_mode(window_size)
    window.set_caption("Space Invaders")

    move_step_size = .8

    spaceship = Spaceship()
    spaceship_width, spaceship_height = spaceship.get_size()
    spaceship.set_pos((window_width - spaceship_width)/2, window_height - 100)
    Running = True
    projectiles = []
    while Running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key  == pygame.K_q): Running = False
            elif (event.type == pygame.KEYDOWN and
                  event.key  == pygame.K_UP):
                x,y = spaceship.get_pos()
                projectile = Projectile(x-20+spaceship_width//2, y-20,-1)
                projectiles.append(projectile)
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and in_bounds(spaceship, window_width, spaceship_width, 0):
            spaceship.move(move_step_size, -1)
        elif keys[pygame.K_RIGHT] and in_bounds(spaceship, window_width, spaceship_width):
            spaceship.move(move_step_size)

        window_surface.fill(WHITE)
        for projectile in projectiles:
            if not proj_in_bounds(projectile, window_height, 0):
                projectiles.remove(projectile)
                continue
            projectile.move()
            display_projectile(window_surface, projectile)
        display_spaceship(window_surface, spaceship)

        window.update()

if __name__ == "__main__":
    main()
