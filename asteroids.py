import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            newv1 = self.velocity.rotate(rand_angle)
            newv2 = self.velocity.rotate(-rand_angle)
            newR = self.radius - ASTEROID_MIN_RADIUS
            aster1 = Asteroid(self.position.x, self.position.y, newR)
            aster1.velocity = newv1 * 1.2
            aster2 = Asteroid(self.position.x, self.position.y, newR)
            aster2.velocity = newv2 * 1.2
