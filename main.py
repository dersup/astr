import pygame
from constants import *
from player import *
from asteroids import *
from astroidfield import *
from bullets import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    Player.containers = (updatable, drawable)
    Bullet.containers = (shot, updatable, drawable)
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for ob in updatable:
            ob.update(dt)

        for ob in asteroids:

            for b in shot:

                if ob.collide(b):
                    ob.split()
                    b.kill()

            if ob.collide(player):
                print("GAME OVER!")
                return

        screen.fill("black")

        for ob in drawable:
            ob.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
