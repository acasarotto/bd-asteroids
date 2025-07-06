import pygame.draw

from circleshape import CircleShape

class Shot(CircleShape):
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

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt