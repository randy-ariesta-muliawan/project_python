import pygame as pg
import config as c
import json
from balon import Balon
from world import World
from turret import Turret

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
pg.display.set_caption("Bloons TD Battles")

map_image = pg.image.load('img/BTD1_Map.png').convert_alpha()

cursor_turret = pg.image.load('img/cursor_turret.png').convert_alpha()

balon_image = pg.image.load('img/Better_Red_Bloon.png').convert_alpha()

buy_turret_image = pg.image.load('img/buy_turret.png').convert_alpha

with open('img/level.tmj') as file:
    world_data = json.load(file)

def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
    if world.tile_map[mouse_tile_num] == 7:
        space_is_free = True
        for turret in turret_group:
            if(mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
                space_is_free = False
        if space_is_free:
            new_turret = Turret(cursor_turret, mouse_tile_x, mouse_tile_y)
            turret_group.add(new_turret)

world = World(world_data, map_image)
world.process_data()

balon_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

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
    turret_group.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()
            if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
                create_turret(mouse_pos)

    pg.display.flip()

pg.quit()