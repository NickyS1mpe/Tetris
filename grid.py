import pygame
from colors import Colors


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 12
        self.cell_size = 30
        self.grid = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.colors = Colors().get_cell_colors()

    # check if block is inside the canvas
    def is_inside(self, row, column):
        return 0 <= row < self.num_rows and 0 <= column < self.num_cols

    # check if the position is empty
    def is_empty(self, row, column):
        return self.grid[row][column] == 0

    # check if the row is full
    def is_row_full(self, row):
        return sum(self.grid[row][col] != 0 for col in range(self.num_cols)) == self.num_cols

    # clear the row
    def clear_row(self, row):
        self.grid[row] = [0] * self.num_cols

    # move down the row
    def row_down(self, row, num_rows):
        for col in range(self.num_cols):
            self.grid[row + num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0

    # calculate how many rows can be cleared
    def clear_full_row(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.row_down(row, completed)
        return completed

    # reset the grid
    def reset(self):
        self.grid = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]

    # draw the grid on canvas
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    def draw_over(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11,
                                        self.cell_size, self.cell_size)
                pygame.draw.rect(screen, self.colors[0], cell_rect)
