from boardUtils import *
from tictactoe import *

pygame.init()
icon = pygame.image.load("assets/tictactoe_logo.ico")
background = pygame.image.load("assets/tictactoe_bg.png")
end_bg = pygame.image.load("assets/tictactoe_win.png")
draw_bg = pygame.image.load("assets/tictactoe_draw.png")
start_bg = pygame.image.load("assets/tictactoe_start.png")

pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(size)

crosses = []
circles = []
board = initial_state()
bot = None
main_player = None
game_started = False
x_start = X_start()
o_start = O_start()
restart = Restart()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_started:
            if o_start.rect.collidepoint(pygame.mouse.get_pos()):
                main_player, bot = O, X
                game_started = True
            elif x_start.rect.collidepoint(pygame.mouse.get_pos()):
                main_player, bot = X, O
                game_started = True

        elif event.type == pygame.MOUSEBUTTONDOWN and game_started:
            coords = getMouseCoord(event.pos[0], event.pos[1])
            board_coords = getBoardCoords(event.pos[0], event.pos[1])
            if coords is not None and board[board_coords[0]][board_coords[1]] is None and player(board) == main_player:
                board[board_coords[0]][board_coords[1]] = main_player
                if board[board_coords[0]][board_coords[1]] == X:
                    crosses.append(coords)
                elif board[board_coords[0]][board_coords[1]] == O:
                    circles.append(coords)
            elif restart.rect.collidepoint(pygame.mouse.get_pos()):
                board = initial_state()
                game_started = False
                bot, main_player = None, None
                screen.blit(background, (0, 0))
                crosses, circles = [], []


        elif player(board) == bot and not terminal(board):
            bot_coords = minimax(board)
            board_bot_coords = BotBoardCoords(bot_coords[0], bot_coords[1])
            board[bot_coords[0]][bot_coords[1]] = bot
            if bot == O:
                circles.append(board_bot_coords)
            else:
                crosses.append(board_bot_coords)

    # updating the screen
    if game_started:
        screen.blit(background, (0, 0))
        for coords in crosses:
            placeCross(screen, coords)
        for coords in circles:
            placeCircle(screen, coords)
    else:
        screen.blit(start_bg, (0, 0))
        screen.blit(o_start.image, (-20, 120))
        o_start.rect.x, o_start.rect.y = -20, 120
        screen.blit(x_start.image, (260, 120))
        x_start.rect.x, x_start.rect.y = 260, 120

    # endgame screen
    if terminal(board):
        screen.blit(end_bg, (0, 0))
        if winner(board) == X:
            placeCross(screen, (200, 80))
        elif winner(board) == O:
            placeCircle(screen, (200, 80))
        else:
            screen.blit(draw_bg, (0, 0))
            screen.blit(restart.image, (120, 240))
            restart.rect.x, restart.rect.y = 120, 240

    pygame.display.flip()

pygame.quit()
