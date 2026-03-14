import pygame

player_img = pygame.image.load("assets/player.png")
player_img = pygame.transform.scale(player_img, (80, 80))

class Tank:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

    def draw(self, screen):
        screen.blit(player_img, (self.x, self.y))