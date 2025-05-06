import pygame as pg
from config import *
from pygame.math import Vector2
import random


class Note:

    def __init__(self):
        column = random.randint(0, num_columns - 1)
        self.x = column * column_width + (column_width - square_size) // 2
        self.y = -square_size
        self.pos = Vector2(self.x, self.y)
    
    def draw_note(self, screen):
        pg.draw.rect(screen, note_color, (self.pos.x, self.pos.y, square_size, square_size))

    def move(self):
        self.pos += fall_speed

    

        

    

    

    


