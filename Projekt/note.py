import pygame as pg
from parser import parse_sm_file
from config import *

class Note:

    img: pg.Surface = pg.Surface((50,50))
    def __init__(self, timestamp: float, speed: float, screen_h: int):
        self.timestamp = timestamp
        self.speed = speed
        self.screen_h = screen_h
        self.hit_note = False
        self.y = -50

    def get_dt(self, current_time: float) -> float:
        """Returns how far in the future the note is to be played"""
        return self.timestamp - current_time
    
    def update_y(self, current_time: float):
        dt = self.get_dt(current_time)
        self.y = self.screen_h - (dt * self.speed)

    def draw(self,screen: pg.Surface, current_time: float) -> None:
        """Draws note to its current position"""
        if self.hit_note:
            return
        self.update_y(current_time)
        screen.blit(self.img, (self.x, self.y))
    
    def hit(self, current_time: float) -> None: # muze treba vracet score
        """Handles hitting the note."""
        self.hit_note = True

class NoteLeft(Note):
    img: pg.Surface = pg.transform.rotate(Note.img.copy(), 90) # orotuju sipku
    x: float = 150 # offset v ose x

class NoteDown(Note):
    img: pg.Surface = pg.transform.rotate(Note.img.copy(), 180) 
    x: float = 250

class NoteUp(Note):
    img: pg.Surface = pg.transform.rotate(Note.img.copy(), 0) 
    x: float = 350

class NoteRight(Note):
    img: pg.Surface = pg.transform.rotate(Note.img.copy(), -90) 
    x: float = 450

mapping: dict[int: Note] = {
            pg.K_LEFT:NoteLeft, 
            pg.K_RIGHT:NoteRight,
            pg.K_DOWN:NoteDown,
            pg.K_UP:NoteUp
        }