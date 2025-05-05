from typing import Literal
import pygame as pg
from pygame.math import Vector2

#Screen size
SCREEN_W , SCREEN_H= 600, 800

FPS = 60

#Note
num_columns = 4
square_size = 50
column_width = SCREEN_W // num_columns
hit_line_y = SCREEN_H - 100 #vyska zasahu
fall_speed = Vector2(0,15)
BPM = 130.5
beat_interval_ms = 60000 / BPM

#Button
button_w = 100
button_h = 20

#Window name
CAPTION = "osu!mania clone"

#Menu font-size
MENU_FONTSIZE = 52

# Custom event identifiers
TIMEEVENT = pg.USEREVENT + 1   # For periodic updates (e.g., physics)
SCENEEVENT = pg.USEREVENT + 2  # For switching between scenes
FPSEVENT = pg.USEREVENT + 3    # For triggering redraws at a fixed rate

# Scene identifiers (used with SCENEEVENT)
SceneType = Literal['menu', 'stgs' ,'game']

# Color palette and sprite styles
C = {
    'bg': (15, 20, 35),              # Background color
    'text_normal': (240, 235, 220),  # Default text color
    'text_emphasis': (200, 200, 100),# Highlighted text
}