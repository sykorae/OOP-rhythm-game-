import pygame as pg
from pygame.event import Event
from scene import Scene
from config import *

class MenuScene(Scene): 
    
    def __init__(self, screen: pg.Surface) -> None:
        super().__init__(screen)
        self.options: list[str] = ['Play', 'Options', 'Quit']
        self.selection: int = 0
        self._font = pg.font.Font('Projekt/assets/Freedom-10eM.ttf', MENU_FONTSIZE)

        # Rendered versions of menu options
        self.s_opts = [
            self._font.render(text, True, C['text_normal'])
            for text in self.options
        ]
        self.s_opts_emph = [
            self._font.render(text, True, C['text_emphasis'])
            for text in self.options
        ]

        # Positioning rectangles for each option
        self.r_opts = [
            surf.get_rect(center=(SCREEN_W // 2, ((i + 1) / len(self.options)) * SCREEN_H//1.5))
            for i, surf in enumerate(self.s_opts)
        ]
    
    def _draw(self) -> None:
        for i in range(len(self.options)):
            surface = self.s_opts_emph[i] if i == self.selection else self.s_opts[i]
            self.screen.blit(surface, self.r_opts[i])

    def keydown(self, event: Event) -> None:
        if event.key == pg.K_UP:
            self.selection -= 1
        elif event.key == pg.K_DOWN:
            self.selection += 1
        elif event.key == pg.K_RETURN:
            if self.selection == 0:
                pg.event.post(pg.event.Event(SCENEEVENT, scene_type='game'))
            elif self.selection == 1:
                pg.event.post(pg.event.Event(SCENEEVENT, scene_type='opts'))
            elif self.selection == 2:
                pg.event.post(pg.event.Event(pg.QUIT))

        # Keep selection within valid range (wrap-around)
        self.selection %= len(self.options)

        # Immediately reflect the selection change visually
        self.draw()
    
    def update(self) -> None:
        pass
