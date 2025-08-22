from Ball import *

pygame.init()
screen = pygame.display.set_mode((640, 640))
screen.fill((0, 0, 0))

running = True

ball = Ball((255, 66, 0))
ball2 = Ball((153, 48, 12), 270)
ball3 = Ball((84, 25, 6), 320)

while running:
    # fade = pygame.Surface((640, 640), pygame.SRCALPHA)
    # fade.fill((0, 0, 0, 25))
    # screen.blit(fade, (0, 0))

    ball.draw(screen)
    ball.move()

    ball2.draw(screen)
    ball2.move()

    ball3.draw(screen)
    ball3.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()