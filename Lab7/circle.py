import pygame as pg


pg.init()


WIDTH, HEIGHT = 500, 500
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Moving Ball")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


RADIUS = 25
x, y = WIDTH // 2, HEIGHT // 2
STEP = 20  


running = True
while running:
    screen.fill(WHITE)  

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT] and x - RADIUS - STEP >= 0:
        x -= STEP
    if keys[pg.K_RIGHT] and x + RADIUS + STEP <= WIDTH:
        x += STEP
    if keys[pg.K_UP] and y - RADIUS - STEP >= 0:
        y -= STEP
    if keys[pg.K_DOWN] and y + RADIUS + STEP <= HEIGHT:
        y += STEP

   
    pg.draw.circle(screen, RED, (x, y), RADIUS)

    
    pg.display.update()
    pg.time.delay(50)  

pg.quit()