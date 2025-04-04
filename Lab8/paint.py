import pygame as pg

pg.init()

W = 1000
H = 600
screen = pg.display.set_mode((W, H))

active_size = 0
active_color = 'white'
active_shape = 0
painting = []


clock = pg.time.Clock()
FPS = 120
pg.display.set_caption("Paint!")

def draw_menu():
    pg.draw.rect(screen, 'gray', [0, 0, W, 100])
    pg.draw.line(screen, 'black', (0, 100), (W, 100), 2)

    xl_brush = pg.draw.rect(screen, 'black', [25,25,50,50])
    pg.draw.circle(screen, 'white', (50,50), 20)
    l_brush = pg.draw.rect(screen, 'black', [90,25,50,50])
    pg.draw.circle(screen, 'white', (115,50), 15)
    m_brush = pg.draw.rect(screen, 'black', [155,25,50,50])
    pg.draw.circle(screen, 'white', (180,50), 10)
    s_brush = pg.draw.rect(screen, 'black', [220,25,50,50])
    pg.draw.circle(screen, 'white', (245,50), 5)

    brush_list = [xl_brush,l_brush,m_brush,s_brush]


    blue = pg.draw.rect(screen, (0,0,255), [W - 50, 25, 25,25])
    green = pg.draw.rect(screen, (0,255,0), [W - 75, 25, 25,25])
    red = pg.draw.rect(screen, (255,0,0), [W - 50, 50, 25,25])
    yellow = pg.draw.rect(screen, (255,255,0), [W - 75 , 50, 25,25])
    pg.draw.rect(screen, 'black', [W - 200, 25, 50,50])
    white = pg.draw.rect(screen, (255,255,255), [W - 195, 30, 40,40])
    rgb_list = [(0,0,255), (0,255,0), (255,0,0), (255,255,0), (255,255,255)]
    color_list = [blue, green, red, yellow, white]

    rectangel = pg.draw.rect(screen, 'black', [400,25,50,50])
    pg.draw.rect(screen, 'white', [405, 30, 40, 40], 3)
    circle = pg.draw.rect(screen, 'black', [455,25,50,50])
    pg.draw.circle(screen, 'white', (480 ,50), 20, 3)
    shape_list = [rectangel, circle]
    shape_name = ["rect", "circle"]


    return brush_list, color_list, rgb_list, shape_list, shape_name



def draw_painting(paint):
    for i in range(len(paint)):
        pg.draw.circle(screen, paint[i][0], paint[i][1], paint[i][2])

drawing = False
drawingshape = False

drawed_shapes = []

run = True
while run:
    screen.fill("white")
    brushes, colors, rgbs, shapes, shapename = draw_menu()
    mouse = pg.mouse.get_pos()
    clicked = pg.mouse.get_pressed()[0]

    if mouse[1] > 100 + active_size:
        pg.draw.circle(screen, active_color, mouse, active_size)
        if clicked and not drawingshape:
            painting.append((active_color, mouse, active_size))
    
    
    for sh in drawed_shapes:
        if sh[0] == "rect":
            pg.draw.rect(screen, sh[1], sh[2], sh[3])
        else:
            pg.draw.circle(screen, sh[1], sh[4], sh[5])

    if drawingshape:
        if clicked and not drawing:
            drawing = True
            start_pos = mouse
        elif not clicked and drawing:
            end_pos = mouse

            x1, y1 = start_pos
            x2, y2 = end_pos

            if y2 < 100:
                y2 = 102
            if y1 < 100:
                y1 = 102

            left = min(x1, x2)
            top = min(y1,y2)
            width = abs(x2-x1)
            height = abs(y2-y1)
            d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

            if y1 - d < 100:
                d = y1 - 102
            drawed_shapes.append((active_shape, active_color, (left, top, width, height), active_size,(x1, y1), d))


            drawing = False
        


        if drawing:
            x1, y1 = start_pos
            x2, y2 = mouse

            if y2 < 100:
                y2 = 102
            if y1 < 100:
                y1 = 102

            left = min(x1, x2)
            top = min(y1,y2)
            width = abs(x2-x1)
            height = abs(y2-y1)

            d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

            if y1 - d < 100:
                d = y1 - 102

            if active_shape == "rect":
                pg.draw.rect(screen, active_color, (left, top, width, height), active_size)
            else:
                pg.draw.circle(screen, active_color,(x1,y1) , d)

            
        

    draw_painting(painting)

    


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    drawingshape = False
                    active_size = 20 - (i * 5)
    
        if event.type == pg.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
    
        if event.type == pg.MOUSEBUTTONDOWN:
            for i in range(len(shapes)):
                if shapes[i].collidepoint(event.pos):
                    drawingshape = True
                    active_shape = shapename[i]
    
    
    



    pg.display.update()
    clock.tick(FPS)
pg.quit()
exit()