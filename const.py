#!/usr/bin/env python
""" Common constants """

from pathlib import Path

USAGE = "Mapfile"

NAME = "Mod1"
# BACKGROUND_COLOR = "#424284"
BACKGROUND_COLOR = "#212121"

TERRAIN_COLOR_HIGH = "#604020"
TERRAIN_COLOR_MID = "#206040"
TERRAIN_COLOR_LOW = "#204060"

FOV = 75
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

GIRD_PADDING = 2
MIN_HEIGHT = -5
MAX_HEIGHT = 5
MAX_SIZE = 7

DRAW_HEIGHT_WEIGHT = 0.6
DRAW_COLOR_INTENSITY_WEIGHT = 1.65

class Terrain:
    """ Holds general information about map """
    error = ""
    points = []
    grid = []
    def __init__(self, file_path):
        self.loc = file_path
        self.file = Path(file_path)
