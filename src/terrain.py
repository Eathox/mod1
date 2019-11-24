#!/usr/bin/env python3
"""Validation and reading of map files"""

from . grid3d import Grid3D

MAX_SIZE = 7
GRID_PADDING = 2 # Grid border badding
MIN_HEIGHT = -5
MAX_HEIGHT = 5

TERRAIN_COLOR_HIGH = "#604020"
TERRAIN_COLOR_MID = "#206040"
TERRAIN_COLOR_LOW = "#333333"

class Terrain:
	"""Terrain grid"""

	def __init__(self, file_path):
		"""Parse file content in to a terrain grid"""
		self.file_path = file_path
		self.padding = GRID_PADDING
		self.size = MAX_SIZE + (self.padding * 2)
		self.height = (abs(MIN_HEIGHT) + abs(MAX_HEIGHT)) + 2 # To account for overflow on top and bottom
		self.grid_3d = Grid3D(self.size, self.size, self.height)
		_parse_map_to_3d(file_path, self.grid_3d)

	def __str__(self):
		"""Terrain info string"""
		name = self.__class__.__name__
		return f"<{name}: {self.size}, {self.height}, {self.padding}>"

	def __getitem__(self, key):
		"""Get the Terrain key value"""
		return self.__dict__[key]

	def __setitem__(self, key, value):
		"""Set the Terrain key to value"""
		self.__dict__[key] = value

	def __iter__(self):
		"""Define iterator"""
		return self.grid_3d.__iter__()

	def _grid_to_3d(terrain):
		min_height = abs(MIN_HEIGHT)
		for layer in range(terrain.height_3d):
			for row in range(terrain.size):
				for point in range(terrain.size):
					if terrain.grid[row][point] >= (layer - min_height):
						terrain.grid_3d[layer][row][point] = 1
					else:
						terrain.grid_3d[layer][row][point] = 0

	def read_map_file(terrain):
		"""Reads file into terrain format"""
		terrain.error = _validate_map_file(terrain)
		if terrain.error != "":
			return terrain.error

		row = GRID_PADDING
		for line in terrain.points:
			i = GRID_PADDING
			for point in line:
				terrain.grid[row][i] = point
				i += 1
			row += 1
		terrain.grid = terrain.grid[::-1]
		_grid_to_3d(terrain)
		return ""
