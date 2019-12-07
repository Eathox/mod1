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
		self.grid_3d = DensityMap(self.size, self.size, self.height)
		if map_content is not None:
			self._parse_map_content(map_content)

	def __str__(self):
		"""Terrain info string"""
		name = self.__class__.__name__
		return f"<{name}: {self.size}, {self.height}, {self.padding}>"

	def __getitem__(self, key):
		"""Get the Terrain key value"""
		return self.__dict__[key]

	def __setitem__(self, key, value):
		"""Set the Terrain key to value"""
		self.__setattr__(key, value)

	def __setattr__(self, key, value):
		"""Set the Terrain key to value"""
		self.__dict__[key] = value

	def __iter__(self):
		"""Define iterator"""
		return self.grid_3d.__iter__()

	def _parse_map_content(self, map_content):
		""""""
		pass
