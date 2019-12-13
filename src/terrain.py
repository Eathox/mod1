#!/usr/bin/env python3
"""Validation and reading of map files"""

from . density_map import DensityMap
from . settings import TERRAIN_GRID_PADDING, TERRAIN_MAX_SIZE, \
	TERRAIN_MAX_HEIGHT, TERRAIN_MIN_HEIGHT

class Terrain(DensityMap):
	"""Terrain grid"""

	def __init__(self, map_content=None):
		"""Parse file content in to a terrain grid"""
		self.padding = TERRAIN_GRID_PADDING
		self.size = TERRAIN_MAX_SIZE + (self.padding * 2)
		self.height = (abs(TERRAIN_MIN_HEIGHT) + abs(TERRAIN_MAX_HEIGHT)) + 2 # To account for overflow on top and bottom
		super(Terrain, self).__init__(self.size, self.size, self.height)
		self.fill(abs(TERRAIN_MIN_HEIGHT))
		if map_content is not None:
			self._parse_map_content(map_content)

	def __str__(self):
		"""Terrain info string"""
		name = self.__class__.__name__
		return f"<{name}: {self.size}, {self.height}, {self.padding}>"

	def _put_point_in_map(self, x, y, value):
		"""Set a point in density map"""
		min_height = abs(TERRAIN_MIN_HEIGHT)
		for layer in range(self.height):
			if value >= (layer - min_height):
				self[layer][y][x] = 1
			else:
				self[layer][y][x] = 0

	def _parse_map_content(self, map_content):
		"""Parse map_content to density map"""
		y = TERRAIN_GRID_PADDING
		lines = map_content.splitlines()
		for line in lines:
			x = TERRAIN_GRID_PADDING
			for value in line.split():
				self._put_point_in_map(x, y, int(value))
				x += 1
			y += 1
