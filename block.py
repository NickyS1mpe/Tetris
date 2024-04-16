import pygame

from colors import Colors
from position import Position


class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotate_state = 0
        self.colors = Colors().get_cell_colors()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_pos(self):
        tiles = self.cells[self.rotate_state]
        move_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            move_tiles.append(position)
        return move_tiles

    def rotate(self):
        self.rotate_state = (self.rotate_state + 1) % len(self.cells)

    def undo_rotate(self):
        self.rotate_state -= 1
        if self.rotate_state < 0:
            self.rotate_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_pos()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + offset_x, tile.row * self.cell_size + offset_y,
                                    self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
