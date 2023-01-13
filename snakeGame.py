import pygame as pg
from random import randrange

pg.init()
window = 1000
tile_size = 50
pg.display.set_caption('Snake Game')

gameOver = False

while not gameOver:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            gameOver=True
    screen.fill('black')
    #draw the snake, percorrendo a lista de segmentos e desenhar cada segmento da snake em verde usando a função draw.rect
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
    
    clock.tick(60)