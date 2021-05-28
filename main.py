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
        (col, row),
        screen,
    )
    for row in range(Brick.number_of_rows)
    for col in range(Brick.number_of_cols)
]

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 0, 0))
    ball.draw()
    ball.updatePosition()
    brickIdx = ball.checkBrickHit(bricks)
    if brickIdx < 0:
        running = ball.updateVelocity((bar.x, bar.x + bar.width), bar.y)
    else:
        bricks.pop(brickIdx)

    bar.draw()
    bar.updatePosition()

    for brick in bricks:
        brick.draw()

    pygame.display.flip()

    if len(bricks) == 0:
        running = False

pygame.quit()
