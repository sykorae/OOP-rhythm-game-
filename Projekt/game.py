import pygame as pg
import time
from pygame.event import Event
from scene import Scene
from config import *
from note import *
from note_loader import create_notes

class GameScene(Scene):

    def __init__(self, screen):
        super().__init__(screen)
        self.notes = []
        self.start_time = 0
        self.active_lanes = [False, False, False, False]
        self.font = pg.font.SysFont("Arial", 25)
        self.lane_labels = ["G", "H", "K", "L"]
        self.score = 0
        
    def now(self) -> float:
        """Helper metod to get current time with respect to song."""
        return time.time() - self.start_time

    def start(self) -> None:
        self.start_time = time.time() 
        pg.mixer.music.load("Projekt/FireStarter.ogg")
        pg.mixer.music.play()
        self.notes = create_notes("Projekt/FireStarter.sm")
    
    def keydown(self, event) -> None:
        current_time = self.now()
        for note in self.notes:
            if note.get_dt(current_time) > HIT_TIME_OFFSET:
                break
            try: 
                if isinstance(note, mapping[event.key]):
                    note.hit(current_time)
                    self.score += 300
                    
                    
            except:
                pass
        
            if event.key == pg.K_g:
                self.active_lanes[0] = True
            elif event.key == pg.K_h:
                self.active_lanes[1] = True
            elif event.key == pg.K_k:
                self.active_lanes[2] = True
            elif event.key == pg.K_l:
                self.active_lanes[3] = True
            
    def keyup(self, event): 
        if event.key == pg.K_g:
            self.active_lanes[0] = False
        elif event.key == pg.K_h:
            self.active_lanes[1] = False
        elif event.key == pg.K_k:
            self.active_lanes[2] = False
        elif event.key == pg.K_l:
            self.active_lanes[3] = False

    def _draw(self):
        self.screen.fill(C['bg'])
        now = self.now()
        for i in range(4): #draw buttons
            x = LANE_START_X + i * (LANE_WIDTH + LANE_GAP) 
            color = (C['button']) if self.active_lanes[i] else (C['hit_button'])
            pg.draw.rect(self.screen, color, (x, LANE_Y, LANE_WIDTH, LANE_HEIGHT))

            label_surface = self.font.render(self.lane_labels[i], True, (C['text_emphasis']))
            label_rect = label_surface.get_rect(center=(x + LANE_WIDTH // 2, LANE_Y + LANE_HEIGHT // 2))
            self.screen.blit(label_surface, label_rect)

            score_text = self.font.render(f"Score: {self.score}", True, C['score'])
            self.screen.blit(score_text, (SCORE_X, SCORE_Y))

        for note in self.notes:
            if note.get_dt(now) > DRAW_TIME_OFFSET:
                break
            if note.y < self.screen.get_height() + 100:
                note.draw(self.screen, now)
        pg.display.flip()


        

   
            
    

