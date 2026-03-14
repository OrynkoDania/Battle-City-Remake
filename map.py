import pygame
brick = pygame.image.load("assets/brick.png")

map_data = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,0,0,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1],
    [1,1,1,1,1,1,1,1]
]

def draw_map(screen):
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 1:
                screen.blit(brick, (x*80, y*80))