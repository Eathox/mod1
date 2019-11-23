#!/usr/bin/env python
"""Definition of grid3d"""

from numpy import zeros

class Grid3D:
	"""3d density grid"""

	def __init__(self, width, length, height):
		"""Create a grid with dimensions"""
		self._setDimension("width", width)
		self._setDimension("length", length)
		self._setDimension("height", height)
		self.grid = zeros((height, length, width))
		self.indexWidth = 0
		self.indexLength = 0
		self.indexHeight = 0

	def __str__(self):
		"""Grid3D info string"""
		name = self.__class__.__name__
		return f"<{name}: {self.width}, {self.length}, {self.height}>"

	def __getitem__(self, key):
		"""Get the Grid3D key value"""
		return self.__dict__[key]

	def __setitem__(self, key, value):
		"""Set the Grid3D key to value"""
		if self._keyIsDimension(key):
			self._setDimension(key, value)
		else:
			self.__dict__[key] = value

	def __iter__(self):
		"""Define iterator"""
		return self

	def __next__(self):
		"""Get next grid element"""
		if self.indexHeight == self.height:
			self.indexHeight = 0
			raise StopIteration

		density = self.grid[self.indexHeight][self.indexLength][self.indexWidth]
		vertex = (self.indexHeight, self.indexLength, self.indexWidth, density)
		if self.indexWidth < (self.width - 1):
			self.indexWidth += 1
		elif self.indexLength < (self.length - 1):
			self.indexWidth = 0
			self.indexLength += 1
		elif self.indexHeight < self.height:
			self.indexWidth = 0
			self.indexLength = 0
			self.indexHeight += 1
		return vertex

	def _keyIsDimension(self, key):
		"""Checks if given key is dimension"""
		return key.lower() in ["width", "length", "height"]

	def _setDimension(self, dim, value):
		"""Set Grid3D dimension"""
		if not self._keyIsDimension(dim):
			raise TypeError(f"Unknown terrain dimension: {dim}")
		if not isinstance(value, int) or value <= 0:
			raise TypeError(f"Invalid terrain {dim} value: {value}")
		self.__dict__[dim] = value


