import pygame
pygame.init()
surface=pygame.display.set_mode((800,480))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()