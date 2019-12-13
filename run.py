#!/usr/bin/env python3
"""Runs the mod1 program"""

from os import environ
from sys import argv

from pyglet import app

from src import Terrain, get_map_content, validate_map_file, init_window

USAGE = "<Mapfile>"
NAME = "Mod1"

FOV = 75

if __name__ == "__main__":
	"""Read terrain and run simulation"""
	if len(argv) != 2:
		print("Usage: python3", argv[0], USAGE)
		exit(0)

	map_content = get_map_content(argv[1])
	validate_map_file(map_content)
	terrain = Terrain(map_content)

	window, fps_display = init_window(NAME, FOV)
	app.run()
