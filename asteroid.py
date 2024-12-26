import pygame, random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

# Asteroid class inheriting from CircleShape
class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20,50)
        spawn_velocity_1 = self.velocity.rotate(split_angle)
        spawn_velocity_2 = self.velocity.rotate(-split_angle)
        spawn_radius = self.radius - ASTEROID_MIN_RADIUS
        
        spawn_1 = Asteroid(self.position.x, self.position.y, spawn_radius)
        spawn_2 = Asteroid(self.position.x, self.position.y, spawn_radius)

        spawn_1.velocity = spawn_velocity_1 * 1.2
        spawn_2.velocity = spawn_velocity_2 * 1.2