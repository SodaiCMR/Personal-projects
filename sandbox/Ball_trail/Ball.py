import pygame
from math import cos, sin, radians

class Ball:

    def __init__(self, color = (255, 255, 255), trajectory_radius = 200):
        self.color = color
        self.center = [480.0, 320.0]
        self.radius = 25
        self.trajectory_radius = trajectory_radius
        self.theta = 0
        self.step = 15
        self.frame_center = (320, 320)
        self.trail = []
        self.max_trail = 25
        self.tours = 0

    def draw(self, screen):
        alpha = 255
        pygame.draw.circle(screen, self.color, self.center, self.radius)
        for ball in self.trail:
            s = pygame.Surface((640, 640), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 255, 255, alpha), ball, self.radius)
            alpha -= 15 if alpha > 0 else 0
        if self.trajectory_radius > 0 and self.theta == 0:
            self.trajectory_radius -= 10
        elif self.trajectory_radius == 0:
            self.trajectory_radius = 200

    def move(self):
        theta_rad = radians(self.theta)
        x = self.trajectory_radius * cos(theta_rad) + self.frame_center[0]
        y = - self.trajectory_radius * sin(theta_rad) + self.frame_center[1]
        self.trail.append((x, y))
        if len(self.trail) == self.max_trail:
            self.trail.pop(0)
        self.center[0], self.center[1] = x, y
        self.theta = (self.theta + self.step) % 360