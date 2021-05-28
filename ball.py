import pygame.draw as draw


class Ball:
    radius = 10
    color = (255, 255, 255)
    x = radius - 5
    y = radius - 5
    speed = 0.3
    x_velocity = speed
    y_velocity = speed

    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def updatePosition(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def updateVelocity(self, bar_x, bar_y):
        if self.x >= self.screen.get_width() - self.radius + 5:
            self.x_velocity = -self.speed
        elif self.x <= self.radius - 5:
            self.x_velocity = self.speed

        if bar_x[0] < self.x and bar_x[1] > self.x and (self.y + self.radius) >= bar_y:
            self.y_velocity = -self.speed
        elif self.y >= self.screen.get_height() + self.radius + 5:
            return False
        elif self.y <= self.radius - 5:
            self.y_velocity = self.speed
        return True
