import pygame

pygame.init()
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)
    pygame.display.flip()