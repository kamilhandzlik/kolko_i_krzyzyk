import pygame as pg
pg.init()

WHITE = (255, 255, 255)         # X and O
BLACK = (0, 0, 0)               #lines and text
RED = (255, 0, 0)               #loser
BLUE = (0, 255, 0)              #background color
GREEN = (0, 0, 255)             #winner


FPS = 60

WIDTH, HEIGHT = 600, 600

ROWS = COLS = 100

PIXEL_SIZE = PIXEL_SIZE = WIDTH // COLS

BG_COLOR = BLUE

def grt_font():
    pg.font.SysFont("Calibri", 20)