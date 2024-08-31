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
    score = 0
    game_font = pygame.font.SysFont("Comic Sans MS", 30)
    end_font = pygame.font.SysFont("Comic Sans MS", 70)
    end_size = end_font.size("GAMEOVER PRESS ENTER")
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
    score_counter = game_font.render(f"Score: {score}", False, "whitesmoke")
    player_alive = True

    while True:
        keys = pygame.key.get_pressed()
        screen.fill("black")
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
                    score += int(100 // (ob.radius / ASTEROID_MIN_RADIUS))
                    score_counter = game_font.render(f"Score: {score}", False, "whitesmoke")

            if ob.collide(player):
                player.kill()
                score_counter = end_font.render(f"Score: {score}", False, "red1")
                player_alive = False
        if not player_alive:
            screen.blit(end_font.render("GAMEOVER PRESS ENTER", False, "red1"), (end_size[0] / 2., end_size[1] / 2.5))
            if keys[pygame.K_RETURN]:
                score = 0
                score_counter = game_font.render(f"Score: {score}", False, "whitesmoke")
                for ob in drawable:
                    ob.kill()
                player_alive = True
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                screen.fill("black")
        screen.blit(score_counter, (1, 0))

        for ob in drawable:
            ob.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
