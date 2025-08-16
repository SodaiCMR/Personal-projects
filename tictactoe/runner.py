# python
import pygame
from boardLogic import *

pygame.init()
icon = pygame.image.load("assets/tic-tac-toe_39453.ico")
background = pygame.image.load("assets/tictactoe_bg.png")

pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(size)

crosses = []
circles = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coords = getMouseCoord(event.pos[0], event.pos[1])
            if coords is not None:
                crosses.append(coords)

    screen.blit(background, (0, 0))
    for coords in crosses:
        placeCircle(screen, coords)

    pygame.display.flip()

pygame.quit()