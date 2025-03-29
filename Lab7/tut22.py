import pygame
pygame.init()
surface=pygame.display.set_mode((800,480))
is_yellow=False
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                is_yellow=not is_yellow
    if is_yellow:
        surface.fill('yellow')
    else:
        surface.fill('purple')
    
    pygame.display.flip()