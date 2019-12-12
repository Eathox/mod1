#!/usr/bin/env python3
"""Validation and reading of map files"""

from . density_map import DensityMap

MAX_SIZE = 7
GRID_PADDING = 2 # Grid border badding
MIN_HEIGHT = -5
MAX_HEIGHT = 5

class Terrain:
	"""Terrain grid"""

	def __init__(self, map_content=None):
		"""Parse file content in to a terrain grid"""
		self.padding = GRID_PADDING
		self.size = MAX_SIZE + (self.padding * 2)
		self.height = (abs(MIN_HEIGHT) + abs(MAX_HEIGHT)) + 2 # To account for overflow on top and bottom
		self.density_map = DensityMap(self.size, self.size, self.height)
		if map_content is not None:
			self._parse_map_content(map_content)

	def __str__(self):
		"""Terrain info string"""
		name = self.__class__.__name__
		return f"<{name}: {self.size}, {self.height}, {self.padding}>"

	def __getitem__(self, key):
		"""Get the DensityMap key value"""
		if isinstance(key, str):
			return self.__dict__[key]
		else:
			return self.density_map[key]

	def __setitem__(self, key, value):
		"""Set the DensityMap key to value"""
		if isinstance(key, str):
			self.__setattr__(key, value)
		else:
			self.density_map[key] = value

	def __setattr__(self, key, value):
		"""Set the Terrain key to value"""
		self.__dict__[key] = value

	def __iter__(self):
		"""Define iterator"""
		return self.density_map.__iter__()

	def _put_point_in_map(self, x, y, value):
		"""Set a point in density map"""
		min_height = abs(MIN_HEIGHT)
		for layer in range(self.height):
			if value >= (layer - min_height):
				self.density_map[layer][y][x] = 1
			else:
				self.density_map[layer][y][x] = 0

	def _parse_map_content(self, map_content):
		"""Parse map_content to density map"""
		y = 0
		lines = map_content.splitlines()
		for line in lines:
			x = 0
			for value in line.split():
				self._put_point_in_map(x, y, int(value))
				x += 1
			y += 1

	def empty(self):
		"""Reset density"""
		self.density_map.empty()

	def print(self, vertexFormat=False):
		"""Print terrain density map"""
		self.density_map.print(vertexFormat)
