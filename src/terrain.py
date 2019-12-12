#!/usr/bin/env python3
"""Validation and reading of map files"""

from . density_map import DensityMap

MAX_SIZE = 7
GRID_PADDING = 2 # Grid border badding
MIN_HEIGHT = -5
MAX_HEIGHT = 5

class Terrain(DensityMap):
	"""Terrain grid"""

	def __init__(self, map_content=None):
		"""Parse file content in to a terrain grid"""
		self.padding = GRID_PADDING
		self.size = MAX_SIZE + (self.padding * 2)
		self.height = (abs(MIN_HEIGHT) + abs(MAX_HEIGHT)) + 2 # To account for overflow on top and bottom
		DensityMap.__init__(self, self.size, self.size, self.height)
		self.fill(abs(MIN_HEIGHT))
		if map_content is not None:
			self._parse_map_content(map_content)

	def __str__(self):
		"""Terrain info string"""
		name = self.__class__.__name__
		return f"<{name}: {self.size}, {self.height}, {self.padding}>"

	def _put_point_in_map(self, x, y, value):
		"""Set a point in density map"""
		min_height = abs(MIN_HEIGHT)
		for layer in range(self.height):
			if value >= (layer - min_height):
				self[layer][y][x] = 1
			else:
				self[layer][y][x] = 0

	def _parse_map_content(self, map_content):
		"""Parse map_content to density map"""
		y = GRID_PADDING
		lines = map_content.splitlines()
		for line in lines:
			x = GRID_PADDING
			for value in line.split():
				self._put_point_in_map(x, y, int(value))
				x += 1
			y += 1
