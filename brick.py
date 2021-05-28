from pygame import Rect, draw


class Brick:

    color = (255, 255, 255)

    def __init__(self, pos, screen):
        self.screen = screen
        self.x, self.y = pos
        self.width = (screen.get_width() - 13) / 12
        self.height = (screen.get_height() / 2.5 - 13) / 12

    def draw(self):
        draw.rect(
            self.screen, self.color, Rect(self.x, self.y, self.width, self.height)
        )
