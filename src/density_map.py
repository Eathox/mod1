#!/usr/bin/env python3
"""Definition of DensityMap"""

from numpy import zeros

from . density_vertex import DensityVertex

class DensityMap:
	"""DensityMap"""

	def __init__(self, width, length, height):
		"""Create a 3Dgrid with dimensions"""
		self._setDimension("width", width)
		self._setDimension("length", length)
		self._setDimension("height", height)
		self.grid_3d = zeros((height, length, width))
		self.__indexWidth = 0
		self.__indexLength = 0
		self.__indexHeight = 0

	def __str__(self):
		"""DensityMap info string"""
		name = self.__class__.__name__
		return f"<{name}: {self.width}, {self.length}, {self.height}>"

	def __getitem__(self, key):
		"""Get the DensityMap key value"""
		if isinstance(key, str):
			return self.__dict__[key]
		else:
			return self.grid_3d[key]

	def __setitem__(self, key, value):
		"""Set the DensityMap key to value"""
		if isinstance(key, str):
			self.__setattr__(key, value)
		else:
			self.grid_3d[key] = value

	def __setattr__(self, key, value):
		"""Set the DensityMap key to value"""
		if self._keyIsDimension(key):
			self._setDimension(key, value)
		else:
			self.__dict__[key] = value

	def __iter__(self):
		"""Define iterator"""
		return self

	def __next__(self):
		"""Get next 3Dgrid element"""
		if self.__indexHeight == self.height:
			self.__indexHeight = 0
			raise StopIteration

		density = self.grid_3d[self.__indexHeight][self.__indexLength][self.__indexWidth]
		vertex = DensityVertex(self.__indexHeight, self.__indexLength, self.__indexWidth, density)
		if self.__indexWidth < (self.width - 1):
			self.__indexWidth += 1
		elif self.__indexLength < (self.length - 1):
			self.__indexWidth = 0
			self.__indexLength += 1
		elif self.__indexHeight < self.height:
			self.__indexWidth = 0
			self.__indexLength = 0
			self.__indexHeight += 1
		return vertex

	def _keyIsDimension(self, key):
		"""Checks if given key is dimension"""
		return key.lower() in ["width", "length", "height"]

	def _setDimension(self, dim, value):
		"""Set DensityMap dimension"""
		if not self._keyIsDimension(dim):
			raise TypeError(f"Unknown terrain dimension: {dim}")
		if not isinstance(value, int) or value <= 0:
			raise TypeError(f"Invalid terrain {dim} value: {value}")
		self.__dict__[dim] = value

	def fill(self, start=0, end=None, value=1):
		"""Fill density map with value from start layer to end layer"""
		if end is None:
			end = self.height
		for layer in range(start, end):
			self.grid_3d[layer] = value

	def empty(self):
		"""Reset density"""
		self.fill(value=0)

	def print(self, vertexFormat=False):
		"""Print density map"""
		if vertexFormat:
			for vertex in self:
				print(vertex)
		else:
			for z in range(self.height):
				print(self.grid_3d[z], end="\n\n")
