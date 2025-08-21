import pygame

class Bar():

    def __init__(self):
        self.color = (255, 255, 255)
        self.w = 50
        self.h = 10
        self.velocity = 15
        self.img = pygame.Surface((70, 30))
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y  = 320, 480
        pygame.draw.rect(self.img, self.color, (0, 0, self.w, self.h))

    def move_right(self):
        if self.rect.x <= 640 - (self.w + 2 * self.h):
            self.rect.x += self.velocity

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.velocity