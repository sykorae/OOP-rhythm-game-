import pygame as pg
import time
from pygame.event import Event
from scene import Scene
from config import *
from note import *
from note_loader import create_notes

DRAW_TIME_OFFSET = 10
HIT_TIME_OFFSET = 1

# Takhle nejak jsme se o te logice bavili. Neni tady to zabijeni not, ale struktura snad souhlasi.
# Nemusite to nutne cele takto pouzit, jen jsem si to takto predstavil ja.
# Ted to hlavne chce ten NoteBuilder, resp. create_notes.
     
class GameScene(Scene):

    def __init__(self, screen):
        super().__init__(screen)
        self.notes = []
        self.start_time = 0

    def now(self) -> float:
        """Helper metod to get current time with respect to song."""
        return time.time() - self.start_time

    def start(self) -> None:
        self.start_time = time.time() # to se musi synchronizovat nejak se zacatkem te hudby
        self.notes = create_notes("Projekt/FireStarter.sm")
    
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
            if note.y < self.screen.get_height() + 100:
                note.draw(self.screen, now)
        pg.display.flip()


        

   
            
    

