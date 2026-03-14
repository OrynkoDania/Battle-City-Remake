import pygame
bullet_img = pygame.image.load("assets/bullet.png")

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8
    def update(self):
        self.y -= self.speed
    def draw(self, screen):
        screen.blit(bullet_img, (self.x, self.y))