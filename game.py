import random
import pygame
from blocks import *
from grid import Grid


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.cur_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.clear_sound = pygame.mixer.Sound("Sounds/Clear.ogg")
        self.rotate_sound = pygame.mixer.Sound("Sounds/sounds_rotate.wav")
        pygame.mixer.music.load("Sounds/Tetris.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    # get a random block
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    # draw blocks on canvas
    def draw(self, screen):
        self.grid.draw(screen)
        self.cur_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 305, 350)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 305, 340)
        else:
            self.next_block.draw(screen, 320, 330)

    # draw the game over interface
    def draw_game_over(self, screen):
        pygame.mixer.music.pause()
        self.grid.draw_over(screen)

    # moving block left
    def move_left(self):
        self.cur_block.move(0, -1)
        # if the left position is illegal
        if not self.block_inside() or not self.block_fits():
            self.cur_block.move(0, 1)

    # moving block right
    def move_right(self):
        self.cur_block.move(0, 1)
        # if the right position is illegal
        if not self.block_inside() or not self.block_fits():
            self.cur_block.move(0, -1)

    # moving block down
    def move_down(self):
        self.cur_block.move(1, 0)
        # if the position below is illegal
        if not self.block_inside() or not self.block_fits():
            self.cur_block.move(-1, 0)
            # lock the block
            self.lock_block()

    def lock_block(self):
        tiles = self.cur_block.get_cell_pos()
        for pos in tiles:
            self.grid.grid[pos.row][pos.column] = self.cur_block.id
        self.cur_block = self.next_block
        self.next_block = self.get_random_block()
        rows_clear = self.grid.clear_full_row()
        # if there are rows completed, clear these rows and update the score
        if rows_clear > 0:
            self.clear_sound.play()
            self.update_score(rows_clear, 0)
        if not self.block_fits():
            self.game_over = True

    # reset the game
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.cur_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        pygame.mixer.music.unpause()

    # rotate the block
    def rotate(self):
        rotate_success = True
        self.cur_block.rotate()
        # if the position after rotation is illegal
        if not self.block_inside() or not self.block_fits():
            self.cur_block.undo_rotate()
            rotate_success = False
        if rotate_success:
            self.rotate_sound.play()

    def update_score(self, lines_clear, move_down):
        if lines_clear == 1:
            self.score += 100
        if lines_clear == 2:
            self.score += 300
        if lines_clear == 3:
            self.score += 500
        if lines_clear == 4:
            self.score += 1000
        self.score += move_down

    # check if position is legal
    def block_fits(self):
        tiles = self.cur_block.get_cell_pos()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    # check if position is legal
    def block_inside(self):
        tiles = self.cur_block.get_cell_pos()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True
