import pygame

class Ball:

    def __init__(self):
        self.color = (255, 0, 0)
        self.w = 70
        self.img = pygame.Surface((self.w + 10, self.w + 10))
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = 320, 160
        pygame.draw.circle(self.img, self.color, (40, 40), self.w / 2)

    def drop(self, other_rect):
        if not self.rect.colliderect(other_rect) and self.rect.y <= (640 - self.w):
            self.rect.y += 5
        if self.rect.colliderect(other_rect):
            self.rect.y -= 200

    # def bounce(self, other_rect):
    #     if self.rect.colliderect(other_rect):
    #         self.rect.y -= 100