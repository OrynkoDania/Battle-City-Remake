import pygame

bullet_img = pygame.image.load("assets/bullet.png").convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (20, 20))

class Bullet:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.speed = 8

    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def draw(self, screen):
        screen.blit(bullet_img, (self.x, self.y))