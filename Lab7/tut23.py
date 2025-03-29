import pygame
pygame.init()
surface=pygame.display.set_mode((800,480))
WIDTH=800
HEIGHT=480
is_yellow=False
running=True

mov_speed=10
circle_pos=(WIDTH//2, HEIGHT//2)
circle_x=WIDTH//2
circle_y=HEIGHT//2
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                is_yellow=not is_yellow
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                is_yellow=not is_yellow
    
            
    if is_yellow:
        surface.fill('yellow')
        pygame.draw.circle(surface, 'purple', circle_pos, 40)
    else:
        surface.fill('purple')
        pygame.draw.circle(surface, 'yellow', circle_pos, 40)

    
    pygame.display.flip()