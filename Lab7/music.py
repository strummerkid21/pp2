import pygame as pg
from sys import exit


pg.mixer.init()
pg.init()


W, H = 500, 500
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Music Player")


imgs = [
    pg.transform.scale(pg.image.load("musics/keshi.jpeg"), (W, H)),
    pg.transform.scale(pg.image.load("musics/UntitledUnmastered.jpg"), (W, H)),
    pg.transform.scale(pg.image.load("musics/fm.jpeg"), (W, H)),
    pg.transform.scale(pg.image.load("musics/compass.jpg"), (W, H))
]


musics = [
    "musics/keshi - GABRIEL.mp3",
    "musics/untitled05.mp3",
    "musics/Flawed Mangoes - The Beginning.mp3",
    "musics/The Neighbourhood - Compass.mp3"
]

playdm = 0
isplaying = False
lenz = len(musics)
key_pressed = {"left": False, "right": False, "space": False, "s": False}

def play_music():
    global isplaying
    pg.mixer.music.stop()  
    pg.mixer.music.load(musics[playdm])
    pg.mixer.music.play()
    pg.mixer.music.set_volume(0.1)
    isplaying = True

def stop_music():
    global isplaying
    pg.mixer.music.stop()
    isplaying = False

def play_next():
    global playdm
    playdm = (playdm + 1) % lenz
    play_music()

def play_prev():
    global playdm
    playdm = (playdm - 1) % lenz
    play_music()


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((18, 18, 18))
    screen.blit(imgs[playdm], (0, 0))

    keys = pg.key.get_pressed()

    
    if keys[pg.K_LEFT] and not key_pressed["left"]:
        play_prev()
        key_pressed["left"] = True
    elif not keys[pg.K_LEFT]:
        key_pressed["left"] = False

    if keys[pg.K_RIGHT] and not key_pressed["right"]:
        play_next()
        key_pressed["right"] = True
    elif not keys[pg.K_RIGHT]:
        key_pressed["right"] = False

    if keys[pg.K_SPACE] and not key_pressed["space"]:
        if isplaying:
            pg.mixer.music.pause()
            isplaying = False
        else:
            pg.mixer.music.unpause()
            isplaying = True
        key_pressed["space"] = True
    elif not keys[pg.K_SPACE]:
        key_pressed["space"] = False

    if keys[pg.K_s] and not key_pressed["s"]:
        stop_music()
        key_pressed["s"] = True
    elif not keys[pg.K_s]:
        key_pressed["s"] = False

    pg.display.update()

pg.quit()