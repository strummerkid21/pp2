import pygame as pg
import datetime as dt
from sys import exit

pg.init()

W, H = 800, 600

clock = pg.time.Clock()
screen = pg.display.set_mode((W, H))
bg = pg.image.load("images/clock.png")

min_hand = pg.image.load("images/min_hand.png")
sec_hand = pg.image.load("images/sec_hand.png")

def rotate(surf, img, angle, pos):
    rotated_img = pg.transform.rotate(img, -angle)
    new_rect = rotated_img.get_rect(center=pos) 
    surf.blit(rotated_img, new_rect.topleft)

pg.display.set_caption("Clock!")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    
    
    curtime = dt.datetime.now()
    minutes = curtime.minute
    seconds = curtime.second

    screen.fill("BLACK")
    screen.blit(bg, (0, 0))  


    rotate(screen, sec_hand, seconds * 6, (400, 300))  
    rotate(screen, min_hand, minutes * 6, (400, 300))  

    pg.display.update()
    clock.tick(60)