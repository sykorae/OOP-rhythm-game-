import pygame as pg
from config import *

class Button():

    def __init__(self, x: int, y: int, width: int, height: int, key: int, color=(200, 200, 200)):
        self.rect = pg.Rect(x, y, width, height)
        self.key = key 
        self.color = color
        self.active = False

    def draw(self, screen):
        pg.draw.rect(screen, self.color if not self.active else (255, 255, 0), self.rect)
