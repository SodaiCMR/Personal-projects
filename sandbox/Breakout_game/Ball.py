import pygame
import random
from utils import *


class Ball:

    def __init__(self):
        self.color = (255, 0, 0)
        self.radius = 35
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, 240)
        self.x_speed = 0
        self.y_speed = 0
        self.gravity = 0.2
        self.bounce_stop = 0.2
        self.retention = 0.8
        self.trajectory = []

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def newton(self):

        if self.y < (HEIGHT - self.radius - WALL_WIDTH):
            self.y_speed += self.gravity
        else:
            if self.y_speed > self.bounce_stop:
                self.y_speed *= - self.retention
            elif abs(self.y_speed) < self.bounce_stop:
                self.y_speed = 0
        if (self.x_speed > 0 and self.x > (WIDTH - self.radius - WALL_WIDTH)) or (
                self.x_speed < 0 and self.x < self.radius + WALL_WIDTH):
            self.x_speed *= - self.retention
            if abs(self.x_speed) < self.bounce_stop:
                self.x_speed = 0

        return self.x_speed, self.y_speed

    def getTrajectory(self):
        if len(self.trajectory) == 5:
            self.trajectory.pop(0)
        self.trajectory.append(self.y)

        return self.trajectory
