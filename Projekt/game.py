import pygame as pg, asyncio
from pygame.event import Event
from scene import Scene
from note import Note
from config import *

class GameScene(Scene):

    def __init__(self, screen):
        super().__init__(screen)
        #notes
        self.notes = []
        self.last_spawn = pg.time.get_ticks()
        self.spawn_interval =  beat_interval_ms
        self.speed = fall_speed
        
    def update(self): 
        current_time = pg.time.get_ticks()
        if current_time - self.last_spawn >= self.spawn_interval:
            self.notes.append(Note())
            self.last_spawn = current_time
        
        for note in self.notes[:]:
            note.move()
            if note.pos.y > hit_line_y:
                self.notes.remove(note)
            
    def _draw(self):
        self.screen.fill(C['bg'])
        for note in self.notes:
            note.draw_note(self.screen)
        pg.display.flip()
    
    async def play_music(delay, file_path, loop=False): #spusti hudbu s delayem
        print(f"Waiting for {delay} seconds before starting music...")
        await asyncio.sleep(delay)
        print("playing")
        pg.mixer.music.load(file_path)
        pg.mixer.music.play()
    

        

   
            
    

