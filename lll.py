import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Egors game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

running = True

while running:
    # screen.fill('#34ebc3')

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill("#eb3459")

