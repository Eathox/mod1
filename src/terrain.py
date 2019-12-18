#!/usr/bin/env python3
"""Validation and reading of map files"""

from OpenGL.GL import glColor3fv, glVertex3f

from . color import HexColor
from . density_map import DensityMap
from . settings import TERRAIN_GRID_PADDING, TERRAIN_MAX_SIZE, \
	TERRAIN_MAX_HEIGHT, TERRAIN_MIN_HEIGHT, RENDER_HEIGHT_WEIGHT, \
	COLOR_TERRAIN_HIGH, COLOR_TERRAIN_MID, COLOR_TERRAIN_LOW, \
	RENDER_COLOR_INTENSITY_WEIGHT

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

	def _draw_vertex(self, vertex):
		"""Draws point with terrain height color"""
		if vertex.z < 0 and vertex.z <= (TERRAIN_MIN_HEIGHT / 2):
			color = COLOR_TERRAIN_LOW
		elif vertex.z > 0 and vertex.z >= (TERRAIN_MAX_HEIGHT / 2):
			color = COLOR_TERRAIN_HIGH
		else:
			color = COLOR_TERRAIN_MID

		if vertex.z < 0:
			minium_intensity = TERRAIN_MIN_HEIGHT / (TERRAIN_MIN_HEIGHT * RENDER_COLOR_INTENSITY_WEIGHT)
			intensity = (vertex.z / ((TERRAIN_MIN_HEIGHT - 1) * RENDER_COLOR_INTENSITY_WEIGHT))
		else:
			minium_intensity = TERRAIN_MAX_HEIGHT / (TERRAIN_MAX_HEIGHT * RENDER_COLOR_INTENSITY_WEIGHT)
			intensity = (vertex.z / ((TERRAIN_MAX_HEIGHT - 1) * RENDER_COLOR_INTENSITY_WEIGHT))
		intensity += minium_intensity

		color = HexColor(color)
		color *= intensity

		glColor3fv(color.array())
		glVertex3f(vertex.x, vertex.y, vertex.z * RENDER_HEIGHT_WEIGHT)
