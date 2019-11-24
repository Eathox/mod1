#!/usr/bin/env python3
"""Runs the mod1 program"""

from sys import argv

import pygame

from src import USAGE, Grid3D, validate_map_file

if __name__ == "__main__":
	"""Read terrain and run simulation"""
	if len(argv) != 2:
		print("Usage: python3", argv[0], USAGE)
		exit(0)

	validate_map_file(argv[1])
	# terrain = const.Terrain(argv[1])
	# terrain.error = map_file.read_map_file(terrain)
	# if terrain.error != "":
	#     print("Error: " + terrain.error)
	#     exit(0)

	# window.init_window(terrain)
	# loop.event_loop_window(terrain)
	pygame.quit()
	quit()
