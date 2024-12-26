# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Init pygame
    pygame.init()

    # Init variables
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add items to relevant groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create relevant objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        for updatable_item in updatable:
            updatable_item.update(dt)
        for asteroid in asteroids:
            if(asteroid.is_colliding(player)):
                print("Game over!")
                exit()
            for shot in shots:
                if(asteroid.is_colliding(shot)):
                    asteroid.kill()
                    shot.kill()
        for drawable_item in drawable:
            drawable_item.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

# Make sure we only run this if we are calling the specific file
if __name__ == "__main__":
    main()