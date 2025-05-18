import pygame as pg
from parser import parse_sm_file
from config import *

class Note:

    img: pg.Surface = pg.Surface((LANE_WIDTH,LANE_HEIGHT))
    img.fill(pg.Color("white"))
    def __init__(self, timestamp: float, speed: float, screen_h: int):
        self.timestamp = timestamp
        self.speed = speed
        self.screen_h = screen_h
        self.hit_note = False
        self.y = -5

    def get_dt(self, current_time: float) -> float:
        """Returns how far in the future the note is to be played"""
        return self.timestamp - current_time
    
    def update_y(self, current_time: float):
        dt = self.get_dt(current_time)
        self.y = HIT_LINE_Y - (dt * self.speed)

    def draw(self,screen: pg.Surface, current_time: float) -> None:
        """Draws note to its current position"""
        if self.hit_note:
            return
        self.update_y(current_time)
        screen.blit(self.img, (self.x, self.y))
    
    def hit(self, current_time: float) -> None: 
        """Handles hitting the note."""
        self.hit_note = True
        

class NoteLeft(Note):
    img: pg.Surface = pg.transform.rotate(Note.img.copy(), 90) 
    x: float = get_lane_x(0)

class NoteDown(Note):
    img: pg.Surface = pg.transform.rotate(Note.img.copy(), 180) 
    x: float = get_lane_x(1)
class NoteUp(Note):
    img: pg.Surface = pg.transform.rotate(Note.img.copy(), 0) 
    x: float = get_lane_x(2)

class NoteRight(Note):
    img: pg.Surface = pg.transform.rotate(Note.img.copy(), -90) 
    x: float = get_lane_x(3)

mapping: dict[int: Note] = {
            pg.K_g:NoteLeft, 
            pg.K_l:NoteRight,
            pg.K_h:NoteDown,
            pg.K_k:NoteUp
        }