#!/usr/bin/env python
"""Runs the mod1 program"""

from sys import argv

import pygame

from src import USAGE, Grid3D

if __name__ == "__main__":
	"""Read terrain and run simulation"""
	if len(argv) != 2:
		print("Usage: python3", argv[0], USAGE)
		exit(0)

	terrainGrid = Grid3D(3, 3, 1)
	print (terrainGrid)
	for point in terrainGrid:
		print (point)
	# terrain = const.Terrain(argv[1])
	# terrain.error = map_file.read_map_file(terrain)
	# if terrain.error != "":
	#     print("Error: " + terrain.error)
	#     exit(0)

	# window.init_window(terrain)
	# loop.event_loop_window(terrain)
	pygame.quit()
	quit()
