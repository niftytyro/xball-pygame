from brick import Brick
import pygame
import pygame.display as display
from ball import Ball
from bar import Bar

pygame.init()

screen_resolution = display.Info()
screen_w, screen_h = screen_resolution.current_w, screen_resolution.current_h
screen = display.set_mode((screen_w, screen_h), pygame.RESIZABLE)


running = True

ball = Ball(screen)
bar = Bar(screen)
bricks = [
    Brick(
        (
            col * (screen_w - 13) / 12 + ((col + 1)),
            row * ((screen_h / 2.5) - 13) / 12 + ((row + 1)),
        ),
        screen,
    )
    for row in range(10)
    for col in range(12)
]

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 0, 0))
    ball.draw()
    ball.updatePosition()
    running = ball.updateVelocity((bar.x, bar.x + bar.width), bar.y)

    bar.draw()
    bar.updatePosition()

    for brick in bricks:
        brick.draw()

    pygame.display.flip()

pygame.quit()
