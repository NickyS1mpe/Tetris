import pygame
from colors import Colors
from game_loop import main


def entrance():
    run = True
    pygame.init()

    screen = pygame.display.set_mode((550, 620))
    pygame.display.set_caption("SSW-500 Tetris")
    screen.fill(Colors.black)
    clock = pygame.time.Clock()
    while run:

        begin = pygame.font.SysFont("Courier New", 30).render("Press Any Key to Start", True, Colors.white)
        screen.blit(begin, (80, 280, 50, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    entrance()
