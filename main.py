from utils.settings import *
from utils import *                 #for some reason VsCode don't read this entire folder so i had to make another import for settings for program to run properly
                               #I will try to resolve this issue later

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("GRA W KÓŁKO I KRZYŻYK")

def draw_grid(win):
    win.fill(BG_COLOR)
    for i in range(1, 3):
        pg.draw.line(win, WHITE, (0, i * 200), (WIDTH, i * 200))
        pg.draw.line(win, WHITE, (i * 200, 0), (i * 200, HEIGHT))
    
    pg.display.update()

run = True
clock = pg.time.Clock()

while run:
    clock.tick(FPS)
    draw_grid(WIN)  
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()

pg.quit()
