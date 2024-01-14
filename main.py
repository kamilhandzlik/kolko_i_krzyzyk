from utils.settings import *
from utils import *                 #for some reason VsCode don't read this entire folder so i had to make another import for settings for program to run properly
                                    #I will try to resolve this issue later

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("GRA W KÓŁKO I KRZYŻYK")

markers = []
clicked = False
pos = []
player = 1
line_width = 6
run = True
clock = pg.time.Clock()

def draw_grid(win):
    win.fill(BG_COLOR)
    for i in range(1, 3):
        pg.draw.line(win, WHITE, (0, 100 * i), (WIDTH, 100 * i), line_width)
        pg.draw.line(win, WHITE, (100 * i, 0), (100 * i, HEIGHT), line_width)
    
    pg.display.update()



for i in range(3):
    row = [0]*3
    markers.append(row)

def draw_markers(win):
    x_pos = 0
    for row in markers:  
        y_pos = 0
        for marker in row:  
            if marker == 1:
                pg.draw.line(win, RED, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pg.draw.line(win, RED, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
            if marker == -1:
                pg.draw.circle(win, GREEN, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1


while run:
    clock.tick(FPS)
    draw_grid(WIN)
    draw_markers(WIN)  
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pg.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pg.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if markers[cell_x // 100][cell_y // 100] == 0:
                markers[cell_x // 100][cell_y // 100] = player
                player *= -1


    pg.display.update()

pg.quit()
