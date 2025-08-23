import pygame
from Bar import Bar
from Ball import Ball
from utils import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
fps = 60
running = True
bar = Bar()
ball = Ball()
bind_pressed = {}

while running:
    screen.fill((0, 0, 0))
    walls = draw_walls(screen)
    bar.draw(screen)
    ball.draw(screen)
    bar.trajectory = bar.getTrajectory()
    ball.trajectory = ball.getTrajectory()
    ball.move()
    ball.x_speed = ball.newton()[0]
    ball.y_speed = ball.newton()[1]

    if checkBallBarTouch(ball, bar):
        ball.x_speed += 2 * (bar.trajectory[-1] - bar.trajectory[0]) / len(bar.trajectory)
        ball.y_speed *= - 1.12

    if bind_pressed.get(pygame.K_RIGHT):
        bar.move_right()
    elif bind_pressed.get(pygame.K_LEFT):
        bar.move_left()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            bind_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            bind_pressed[event.key] = False

    pygame.display.flip()
    delta = clock.tick(fps)
