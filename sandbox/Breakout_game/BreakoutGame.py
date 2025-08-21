import pygame
from Bar import Bar
from Ball import Ball

pygame.init()
screen = pygame.display.set_mode((640, 640))
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
    screen.blit(bar.img, bar.rect)
    screen.blit(ball.img, ball.rect)
    ball.drop(bar)
    # ball.bounce(bar)

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