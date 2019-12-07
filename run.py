#!/usr/bin/env python3
"""Runs the mod1 program"""

from os import environ
from sys import argv

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from src import Grid3D, get_map_content, validate_map_file

USAGE = "<Mapfile>"
NAME = "Mod1"

if __name__ == "__main__":
	"""Read terrain and run simulation"""
	if len(argv) != 2:
		print("Usage: python3", argv[0], USAGE)
		exit(0)

	map_content = get_map_content(argv[1])
	print(map_content)
	# validate_map_file(map_content)
	# terrain = const.Terrain(argv[1])
	# terrain.error = map_file.read_map_file(terrain)
	# if terrain.error != "":
	#     print("Error: " + terrain.error)
	#     exit(0)

	# window.init_window(terrain)
	# loop.event_loop_window(terrain)
	pygame.quit()
	quit()
