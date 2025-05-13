import pygame as pg, asyncio
from pygame.event import Event
from scene import Scene
from note import Note
from config import *

class GameScene(Scene):

    def __init__(self, screen):
        super().__init__(screen)
        
            
    def _draw(self):
        self.screen.fill(C['bg'])
        pg.display.flip()
    
    
    

        

   
            
    

