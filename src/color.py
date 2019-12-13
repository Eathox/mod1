#!/usr/bin/env python
"""Color Management"""

class Color:
	"""Color class"""

	def __init__(self, r, g, b, a=1):
		"""Color in rgba range 0 to 1"""
		self.r = r
		self.g = g
		self.b = b
		self.a = a

	def __getitem__(self, channel):
		"""Get the color channel value"""
		return self.__dict__[channel]

	def __setitem__(self, channel, value):
		"""Set the color channel to value"""
		if value < 0 or value > 1:
			raise TypeError("Channel value must be in range of 0 to 1")
		self.__dict__[channel] = value

	def __str__(self):
		"""Color info string"""
		name = self.__class__.__name__
		return f"<{name}: {self.r}, {self.g}, {self.b}, {self.a}>"

	def __mul__(self, other):
		"""Multiplication of color"""
		r = self.r * other
		g = self.g * other
		b = self.b * other
		a = self.a * other
		return Color(r, g, b, a)

	def array(self, alpha=False):
		"""get color in array from"""
		array = [self.r, self.g, self.b]
		if alpha == True:
			array.append(self.a)
		return array

class HexColor(Color):
	"""Proxy of Color class in hex format"""
	def __init__(self, hex):
		"""Convert hex to color"""
		if not hex.startswith("#"):
			raise TypeError("Invalid hex")

		self._hex_pair_to_float("r", hex[1:3])
		self._hex_pair_to_float("g", hex[3:5])
		self._hex_pair_to_float("b", hex[5:7])
		if len(hex) >= 9:
			self._hex_pair_to_float("a", hex[7:9])
		else:
			self.a = 1

	def _hex_pair_to_float(self, channel, pair):
		"""Convert hex pair to color range 0 to 1"""
		num = int(pair, 16)
		self[channel] = (num / 255)
