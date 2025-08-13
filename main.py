import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Returns a Surface object
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collisionCheck(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collisionCheck(shot):
                    asteroid.split()
                    shot.kill()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000 # Sets frame rate to 60 FPS

if __name__ == "__main__":
    main()
