import pygame, sys
from game import Game
from colors import Colors
from score import Score


# game loop
def main():
    # initialize pygame
    pygame.init()

    font = pygame.font.SysFont("OCR A Extended", 30, bold=False)
    font1 = pygame.font.SysFont("OCR A Extended", 40, bold=True)
    score_surface = font.render("Score", True, Colors.white)
    score = Score()
    max_score = score.get_max_score()
    max_score_surface = font.render("Max Score", True, Colors.white)
    next_surface = font.render("Next Cube", True, Colors.white)
    game_over_surface = pygame.font.Font(None, 60).render("GAME OVER", True, Colors.white)
    game_over = pygame.font.Font(None, 30).render("Press Any Key to Continue", True, Colors.white)

    score_rect = pygame.Rect(370, 55, 170, 60)
    max_score_rect = pygame.Rect(370, 165, 170, 60)
    next_rect = pygame.Rect(320, 275, 170, 180)

    screen = pygame.display.set_mode((550, 620))
    pygame.display.set_caption("SSW-500 Tetris")

    # initialize clock and game
    clock = pygame.time.Clock()
    game = Game()

    # set update frequency
    game_update = pygame.USEREVENT
    pygame.time.set_timer(game_update, 250)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # if game is over, record the score and reset the game
                if game.game_over:
                    game.game_over = False
                    score.update_score(game.score)
                    max_score = score.get_max_score()
                    game.reset()
                if not game.game_over:
                    # capture inputs from keyboard
                    if event.key == pygame.K_DOWN:
                        game.move_down()
                        game.update_score(0, 1)
                    if event.key == pygame.K_LEFT:
                        game.move_left()
                    if event.key == pygame.K_RIGHT:
                        game.move_right()
                    if event.key == pygame.K_UP:
                        game.rotate()
            # fall blocks automatically
            if event.type == game_update and not game.game_over:
                game.move_down()

        # drawing the game canvas
        screen.fill(Colors.black)

        current_score = font1.render(str(game.score), True, Colors.white)
        screen.blit(max_score_surface, (375, 130, 50, 50))
        m_score = font1.render(str(max_score), True, Colors.white)
        screen.blit(score_surface, (375, 20, 50, 50))
        screen.blit(next_surface, (375, 260, 50, 50))

        # if game is over, show the game over interface
        if game.game_over:
            game.draw_game_over(screen)
            screen.blit(game_over_surface, (50, 230, 50, 50))
            screen.blit(game_over, (50, 280, 50, 50))

        pygame.draw.rect(screen, Colors.black, score_rect, 0, 10)
        screen.blit(current_score, current_score.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
        pygame.draw.rect(screen, Colors.black, max_score_rect, 0, 10)
        screen.blit(m_score, m_score.get_rect(centerx=max_score_rect.centerx, centery=max_score_rect.centery))
        # pygame.draw.rect(screen, Colors.black, next_rect, 0, 10)

        # if game is not over, draw the blocks on canvas
        if not game.game_over:
            game.draw(screen)

        # update the canvas display
        pygame.display.update()
        clock.tick(60)
