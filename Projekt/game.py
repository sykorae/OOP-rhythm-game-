import pygame as pg, asyncio #LM: tohle se nedela, co knihovna to radek
import time
from pygame.event import Event
from scene import Scene
from note import Note
from config import *

DRAW_TIME_OFFSET = 10
HIT_TIME_OFFSET = 1

# Takhle nejak jsme se o te logice bavili. Neni tady to zabijeni not, ale struktura snad souhlasi.
# Nemusite to nutne cele takto pouzit, jen jsem si to takto predstavil ja.
# Ted to hlavne chce ten NoteBuilder, resp. create_notes.

class Note:
    img: pg.Surface # base img sipky
    def __init__(self):
        self.timestamp: float
        self.hit = False
    def get_dt(self, current_time: float) -> float:
        """Returns how far in the future the note is to be played"""
    def draw(self, current_time: float) -> None:
        """Draws note to its current position"""
    def hit(self, current_time: float) -> None: # muze treba vracet score
        """Handles hitting the note."""
        self.hit = True

class NoteLeft(Note):
    img: pg.Surface = pg.transform.rotate(Note.img, ...) # orotuju sipku
    x: float # offset v ose x

mapping: dict[int: Note] = {
            pg.K_LEFT:NoteLeft, 
        }

class GameScene(Scene):

    def __init__(self, screen):
        super().__init__(screen)
        def create_notes(self, filename: str) -> list[Note]:
            from parser import parse_sm_file
            # tohle nebude tady, ale spolu s notami v jinem souboru
        self.notes = create_notes("FireStarter.sm")
    
    def now(self) -> float:
        """Helper metod to get current time with respect to song."""
        return time.time() - self.start_time

    def start(self) -> None:
        self.start_time = time.time() # to se musi synchronizovat nejak se zacatkem te hudby
    
    def keydown(self, event) -> None:
        current_time = self.now()
        for note in self.notes:
            if note.get_dt(current_time) > HIT_TIME_OFFSET:
                break
            if isinstance(note, mapping[event.key]):
                note.hit(current_time)
            
       
    def _draw(self):
        self.screen.fill(C['bg'])

        now = self.now()
        for note in self.notes:
            if note.get_dt(now) > DRAW_TIME_OFFSET:
                break
            note.draw(now)
        pg.display.flip()
    
    
    

        

   
            
    

