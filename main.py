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

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 0, 0))
    ball.draw()
    ball.updatePosition()
    running = ball.updateVelocity()

    pygame.display.flip()

pygame.quit()
