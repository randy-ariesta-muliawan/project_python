import pygame as pg
import config as c
from balon import Balon

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Bloons TD Battles")

balon_image = pg.image.load('img/Better_Red_Bloon.png').convert_alpha()
balon_group = pg.sprite.Group()

balon = Balon((200, 300), balon_image)
balon_group.add(balon)

run = True
while run:
    clock.tick(c.FPS)
    balon_group.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()

pg.quit()