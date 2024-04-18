# store different colors
class Colors:
    dark_grey = (50, 50, 50)
    green = (0, 255, 127)
    red = (255, 58, 58)
    orange = (226, 116, 17)
    yellow = (255, 182, 0)
    purple = (84, 0, 255)
    cyan = (21, 204, 209)
    blue = (47, 100, 214)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)
    white = (255, 255, 255)
    grey = (155, 155, 155)
    black = (0, 0, 0)

    def get_cell_colors(self):
        return [self.dark_grey, self.green, self.red, self.orange, self.yellow, self.purple, self.cyan, self.blue]
