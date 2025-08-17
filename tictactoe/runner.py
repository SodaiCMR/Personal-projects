# python
from boardLogic import *
from tictactoe import *

pygame.init()
icon = pygame.image.load("assets/tic-tac-toe_39453.ico")
background = pygame.image.load("assets/tictactoe_bg.png")
end_bg = pygame.image.load("assets/tictactoe_endg.png")

pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(size)

crosses = []
circles = []

running = True
board = initial_state()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coords = getMouseCoord(event.pos[0], event.pos[1])
            board_coords = getBoardCoords(event.pos[0], event.pos[1])
            if coords is not None:
                board[board_coords[0]][board_coords[1]] = player(board)
                crosses.append(coords) if player(board) == X else circles.append(coords)

    # updating the screen
    screen.blit(background, (0, 0))
    for coords in crosses:
        placeCross(screen, coords)
    for coords in circles:
        placeCircle(screen, coords)

    if terminal(board):
        screen.blit(end_bg, (0, 0))
        screen.blit(cross, (200, 80)) if winner(board) == X else screen.blit(circle, (200, 80))

    pygame.display.flip()

pygame.quit()