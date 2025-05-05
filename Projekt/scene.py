import pygame as pg
from pygame.event import Event
from abc import ABC, abstractmethod
from config import *

class Scene(ABC):
    
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.process = {
            pg.KEYDOWN: self.keydown,
            pg.KEYUP: self.keyup,
            TIMEEVENT: self.timestep,
            FPSEVENT:self.fps,
        }

    @abstractmethod
    def _draw(self) -> None:
        """
        Internal method to draw scene-specific content.
        Must be implemented by every concrete scene subclass.
        """

    def draw(self) -> None:
        self.screen.fill(C['bg'])
        self._draw()
        pg.display.flip()

    def keydown(self, event: Event) -> None:
        """
        Handle keydown events. Override in subclasses to define behavior.

        Args:
            event (Event): The Pygame keydown event.
        """

    def keyup(self, event:Event) -> None:
        """
        Handle keyup events. Override in subclasses to define bahavior.

        Args:
            event (Event): The Pygame keyup event.
        """

    def fps(self, event: Event) -> None:
        """
        Handle redraw trigger events (FPSEVENT). Override as needed.

        Args:
            event (Event): The frame redraw timer event.
        """  

    def timestep(self, event: Event) -> None:
        """
        Handle time-step updates (TIMEEVENT), such as physics or animation.
        Override in subclasses to define behavior.

        Args:
            event (event): The periodic timer event.
        """
        print('tick')  # Default implementation for debugging purposes

    def start(self) -> None:
        """
        Called when the scene becomes active.

        Sets the allowed event types in the global event queue
        to just those handled by this scene.
        """
        pg.event.set_blocked(None)
        pg.event.set_allowed([pg.QUIT, SCENEEVENT, *self.process.keys()])

    def stop(self) -> None:
        """
        Called when the scene becomes inactive.
        Override in subclasses to define cleanup logic.
        """  
    
    