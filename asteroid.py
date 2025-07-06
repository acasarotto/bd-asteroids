import pygame.draw
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        self.rotation = 0
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
        pass

    def rotate(self, dt):
        self.rotation += dt
        pass

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, dt):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(0-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            Asteroid1.velocity = vector1 * 1.2
            Asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            Asteroid2.velocity = vector2 * 1.2


