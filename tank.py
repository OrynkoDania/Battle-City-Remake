import pygame
player_img = pygame.image.load("assets/player.png")

class Tank:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.rotation = 0

    def move(self, dx, dy):
        if dx!=0 and dy!=0:
            dx=0
        
        self.x += dx * self.speed
        self.y += dy * self.speed

        if dx==0 and dy==-1:
            self.rotation = 0
        elif dx == 1 and dy == 0:
            self.rotation = -90
        elif dx == 0 and dy == 1:
            self.rotation = 180
        elif dx == -1 and dy == 0:
            self.rotation = 90

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(player_img, self.rotation)
        rect = rotated_image.get_rect(center=(self.x, self.y))
        screen.blit(rotated_image, rect.topleft)