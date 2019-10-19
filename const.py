#!/usr/bin/env python
""" Common constants """

from pathlib import Path

USAGE = "Mapfile"

NAME = "Mod1"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

MIN_HEIGHT = -20
MAX_HEIGHT = 20
MAX_SIZE = 7

class Terrain:
	""" Holds general information about map """

	error = ""
	points = []
	grid = []
	def __init__(self, file_path):
		self.loc = file_path
		self.file = Path(file_path)
