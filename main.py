# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player.containers = (updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        for updatable_item in updatable:
            updatable_item.update(dt)
        for drawable_item in drawable:
            drawable_item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()