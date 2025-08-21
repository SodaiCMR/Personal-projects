from Ball import *

pygame.init()
screen = pygame.display.set_mode((640, 640))
screen.fill((0, 0, 0))

running = True

ball = Ball()

while running:
    fade = pygame.Surface((640, 640), pygame.SRCALPHA)
    fade.fill((0, 0, 0, 25))
    screen.blit(fade, (0, 0))

    ball.draw(screen)
    ball.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()