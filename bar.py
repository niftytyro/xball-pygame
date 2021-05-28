from pygame import Rect
import pygame
import pygame.draw as draw


class Bar:
    height = 20
    color = (255, 255, 255)

    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width() * 0.2
        self.x = screen.get_width() / 2 - self.width / 2
        self.y = screen.get_height() - self.height - 5

    def draw(self):
        draw.rect(
            self.screen, self.color, Rect(self.x, self.y, self.width, self.height)
        )

    def updatePosition(self):
        self.x = pygame.mouse.get_pos()[0] - self.width / 2
