from typing import Literal
import pygame as pg
from pygame.math import Vector2

#game logic
DRAW_TIME_OFFSET = 10
HIT_TIME_OFFSET = 0.1

#Screen size
SCREEN_W , SCREEN_H= 640, 800
FPS = 60

#Note
FALL_SPEED = 500
HIT_LINE_Y = int(SCREEN_H * 0.75)

#Hit zone
LANE_WIDTH = 64
LANE_HEIGHT = 64
LANE_Y = HIT_LINE_Y
LANE_GAP = 30
NUM_LANES = 4
LANE_START_X = (SCREEN_W - ((LANE_WIDTH * NUM_LANES) + (LANE_GAP * (NUM_LANES - 1)))) // 2

def get_lane_x(lane_index: int) -> int:
    return LANE_START_X + lane_index * (LANE_WIDTH + LANE_GAP)

#score

SCORE_X = 15
SCORE_Y = 20

#Window nae
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
    'button' : (0, 150, 255),
    'hit_button' : (80, 80, 80),
    'score' : (255, 255, 255),
}