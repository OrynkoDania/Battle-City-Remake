import pygame
from tank import Tank
from enemy import Enemy
from bullet import Bullet
from map import draw_map

pygame.init()

WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle City Remake")
clock = pygame.time.Clock()

player = Tank(300, 560)
bullets = []
enemies = []
spawn_timer = 0
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullets.append(Bullet(player.x + 15, player.y))

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy = -1
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy = 1
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx = -1
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx = 1

    player.move(dx, dy)

    spawn_timer += 1
    if spawn_timer > 120:
        import random
        enemies.append(Enemy(random.randint(0, 600), 0))
        spawn_timer = 0

    for bullet in bullets: bullet.update()
    for enemy in enemies: enemy.update()

    screen.fill((0, 0, 0))
    draw_map(screen)
    player.draw(screen)
    for bullet in bullets: bullet.draw(screen)
    for enemy in enemies: enemy.draw(screen)
    pygame.display.update()

pygame.quit()