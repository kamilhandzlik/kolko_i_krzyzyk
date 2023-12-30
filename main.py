from utils.settings import * 
from utils import *            #for some reason VsCode don't read this entire folder so i had to make another import for settings for program to run properly
                               #I will try to resolve this issue later

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("GRA W KÓŁKO I KRZYŻYK")





run = True
clock = pg.time.Clock()

while run:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False



pg.quit()