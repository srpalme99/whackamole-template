import pygame
import random

GRID_WIDTH, GRID_HEIGHT = 20, 16
SQUARE_SIZE = 32
SCREEN_WIDTH, SCREEN_HEIGHT = GRID_WIDTH * SQUARE_SIZE, GRID_HEIGHT * SQUARE_SIZE


def main():
    try:
        pygame.init()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        mole_image = pygame.image.load("mole.png")
        clock = pygame.time.Clock()
        mole_rect = mole_image.get_rect(topleft=(0, 0))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):
                        new_x = random.randrange(0, GRID_WIDTH) * SQUARE_SIZE
                        new_y = random.randrange(0, GRID_HEIGHT) * SQUARE_SIZE
                        mole_rect.topleft = (new_x, new_y)

            screen.fill((213, 247, 242))

            for x in range(0, SCREEN_WIDTH, SQUARE_SIZE):
                pygame.draw.line(screen, "dark blue", (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, SQUARE_SIZE):
                pygame.draw.line(screen, "dark blue", (0, y), (SCREEN_WIDTH, y))

            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
