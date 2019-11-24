#!/usr/bin/env python3
"""Definition of density vertex"""

class DensityVertex:
	"""DensityVertex"""

	def __init__(self, x, y, z, density=0):
		"""Create a DensityVertex with x, y, z, density"""
		self.x = x
		self.y = y
		self.z = z
		self.density = density

	def __str__(self):
		"""Color info string"""
		name = self.__class__.__name__
		return f"<{name}: {self.x}, {self.y}, {self.z}, {self.density}>"

	def __getitem__(self, key):
		"""Get the DensityVertex key value"""
		return self.__dict__[key]

	def __setitem__(self, key, value):
		"""Set the DensityVertex key to value"""
		self.__dict__[key] = value

	def __mul__(self, other):
		"""Multiplication of DensityVertex"""
		density = self.density * other
		return DensityVertex(self.x, self.y, self.z, density)

	def __add__(self, other):
		"""Addition of DensityVertex"""
		density = self.density + other
		return DensityVertex(self.x, self.y, self.z, density)

	def __sub__(self, other):
		"""Subtraction of DensityVertex"""
		density = self.density - other
		return DensityVertex(self.x, self.y, self.z, density)

	def array(self, density=True):
		"""Get DensityVertex in array from"""
		array = [self.x, self.y, self.z]
		if density == True:
			array.append(self.density)
		return array
