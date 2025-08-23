from pygame.draw_py import draw_line

WIDTH = 640
HEIGHT = 640
WALL_COLOR = (255, 255, 255)
WALL_WIDTH = 5

def draw_walls(screen):
    wall_left = draw_line(screen, WALL_COLOR, (0, 0), (0, HEIGHT), WALL_WIDTH)
    wall_bottom = draw_line(screen, WALL_COLOR, (0, HEIGHT), (WIDTH, HEIGHT), WALL_WIDTH)
    wall_right = draw_line(screen, WALL_COLOR, (WIDTH, 0), (WIDTH, HEIGHT), WALL_WIDTH)

    return [wall_left, wall_bottom, wall_right]
