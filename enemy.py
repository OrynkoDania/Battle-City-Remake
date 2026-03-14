import pygame
import math

enemy_img = pygame.image.load("assets/enemy.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (60, 60))

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2

    def update(self, player):
        dx = player.x - self.x
        dy = player.y - self.y

        dist = math.sqrt(dx*dx + dy*dy)

        if dist != 0:
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist

    def draw(self, screen):
        screen.blit(enemy_img, (self.x, self.y))