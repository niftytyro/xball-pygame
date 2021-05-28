from pygame import Rect, draw


class Brick:

    color = (255, 255, 255)
    number_of_rows = 16
    number_of_cols = 12

    def __init__(self, pos, screen):
        self.screen = screen
        col, row = pos
        self.width = (
            screen.get_width() - self.number_of_cols - 1
        ) / self.number_of_cols
        self.height = (
            (screen.get_height() / 2.5) - self.number_of_rows - 1
        ) / self.number_of_rows
        self.x = col * self.width + (col + 1)
        self.y = row * self.height + (row + 1)

    def draw(self):
        draw.rect(
            self.screen, self.color, Rect(self.x, self.y, self.width, self.height)
        )
