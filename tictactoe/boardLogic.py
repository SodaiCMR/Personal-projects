import pygame

size = (480, 480)
case_width = size[0] / 3
cross = pygame.image.load("assets/cross.png")
cross = pygame.transform.scale(cross, (size[0] / 6, size[0] / 6))
circle = pygame.image.load("assets/circle.png")
circle = pygame.transform.scale(circle, (size[0] / 6, size[0] / 6))


def getMouseCoord(x, y):
    mouse_pos_x = ((x // case_width) * size[0] / 3) + size[0] / 12
    mouse_pos_y = ((y // case_width) * size[0] / 3) + size[0] / 12
    return mouse_pos_x, mouse_pos_y


def getBoardCoords(x, y):
    return int(x // case_width), int(y // case_width)


def placeCircle(board, coord):
    board.blit(circle, coord)


def placeCross(board, coord):
    board.blit(cross, coord)
