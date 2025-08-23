import pygame
from utils import *

class Bar():

    def __init__(self):
        self.color = (255, 255, 255)
        self.x = 320
        self.y = 480
        self.w = 50
        self.h = 10
        self.velocity = 15
        self.trajectory = []

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

    def move_right(self):
        if self.x <= WIDTH - self.w - WALL_WIDTH:
            self.x += self.velocity

    def move_left(self):
        if self.x > WALL_WIDTH:
            self.x -= self.velocity

    def getTrajectory(self):
        if len(self.trajectory) == 10:
            self.trajectory.pop(0)
        self.trajectory.append(self.x)

        return self.trajectory