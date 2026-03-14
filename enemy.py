import pygame
enemy_img = pygame.image.load("assets/enemy.png")

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
    def update(self):
        self.y += self.speed
    def draw(self, screen):
        screen.blit(enemy_img, (self.x, self.y))