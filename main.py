import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    # Returns a Surface object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # pygame.Surface.fill(screen, (0, 0, 0))
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        # Set frame rate to 60 FPS. Pass the return (amt of time passed since last call) as seconds to variable dt
        dt = clock.tick(60)/1000 

if __name__ == "__main__":
    main()
