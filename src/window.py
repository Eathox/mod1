#!/usr/bin/env python3
"""Window management"""

from os import environ

from pyglet import gl, window

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_RATIO = (WINDOW_WIDTH / WINDOW_HEIGHT)

class Window:
	""""""

	def __init__(self, name, fov):
		"""Initialise the application window"""
		gl_config = gl.Config()
		window.Window(WINDOW_HEIGHT, WINDOW_WIDTH, config=gl_config)
