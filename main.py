import pygame as pg
import config as c
import json
from balon import Balon
from world import World
from turret import Turret

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Bloons TD Battles")

map_image = pg.image.load('img/level.png').convert_alpha()

cursor_turret = pg.image.load('img/turret.png').convert_alpha()

balon_image = pg.image.load('img/Better_Red_Bloon.png').convert_alpha()

with open('img/level.tmj') as file:
    world_data = json.load(file)

world = World(world_data, map_image)
world.process_data()

balon_group = pg.sprite.Group()

balon = Balon(world.waypoints, balon_image)
balon_group.add(balon)

run = True
while run:
    clock.tick(c.FPS)
    screen.fill("white")

    world.draw(screen)

    pg.draw.lines(screen, "grey0", False, world.waypoints)

    balon_group.update()
    balon_group.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()

pg.quit()