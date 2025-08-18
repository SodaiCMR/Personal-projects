from boardLogic import *
from tictactoe import *

pygame.init()
icon = pygame.image.load("assets/tictactoe_logo.ico")
background = pygame.image.load("assets/tictactoe_bg.png")
end_bg = pygame.image.load("assets/tictactoe_win.png")
draw_bg = pygame.image.load("assets/tictactoe_draw.png")

pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(size)

crosses = []
circles = []
board = initial_state()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coords = getMouseCoord(event.pos[0], event.pos[1])
            board_coords = getBoardCoords(event.pos[0], event.pos[1])
            if coords is not None and board[board_coords[0]][board_coords[1]] is None:
                board[board_coords[0]][board_coords[1]] = player(board)
                if board[board_coords[0]][board_coords[1]] == X:
                    crosses.append(coords)
                elif board[board_coords[0]][board_coords[1]] == O:
                    circles.append(coords)

    # updating the screen
    screen.blit(background, (0, 0))
    for coords in crosses:
        placeCross(screen, coords)
    for coords in circles:
        placeCircle(screen, coords)

    # endgame screen
    if terminal(board):
        screen.blit(end_bg, (0, 0))
        if winner(board) == X:
            placeCross(screen, (200, 80))
        elif winner(board) == O:
            placeCircle(screen, (200, 80))
        else:
            screen.blit(draw_bg, (0, 0))

    pygame.display.flip()

pygame.quit()