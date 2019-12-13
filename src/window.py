#!/usr/bin/env python3
"""Window management"""

from os import environ

from pyglet import gl, window

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_RATIO = (WINDOW_WIDTH / WINDOW_HEIGHT)

def init_window(name, fov):
	"""Initialise the application window"""
	gl_config = gl.Config()
	my_window = window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, config=gl_config)
	my_window.set_caption(name)
	fps_display = window.FPSDisplay(my_window)
	return my_window, fps_display
