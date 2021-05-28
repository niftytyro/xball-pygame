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
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2

    def draw(self):
        draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def updatePosition(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def checkBrickHit(self, bricks):
        for (idx, brick) in enumerate(bricks):
            if (
                self.x < brick.x + brick.width
                and self.y - self.radius + 5 <= brick.y + brick.height
            ):
                self.y_velocity = self.speed
                return idx
        return -1

    def updateVelocity(self, bar_x, bar_y):
        if self.x >= self.screen.get_width() - self.radius + 5:
            self.x_velocity = -self.speed
        elif self.x <= self.radius - 5:
            self.x_velocity = self.speed

        if bar_x[0] < self.x and bar_x[1] > self.x and (self.y + self.radius) >= bar_y:
            self.speed += 0.01
            self.y_velocity = -self.speed
        elif self.y >= self.screen.get_height() + self.radius + 5:
            return False
        elif self.y <= self.radius - 5:
            self.y_velocity = self.speed
        return True
