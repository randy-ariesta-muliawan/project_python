import pygame as pg

class Balon(pg.sprite.Sprite):
    def __init__(self, pos, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos