#!/usr/bin/env python3
"""Window management"""

from pyglet import gl, window, text

from . settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS_POS_X, FPS_POS_Y, \
	PROGRAM_NAME

def init_window(gl_config):
	"""Initialise the application window"""
	my_window = window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, config=gl_config)
	my_window.set_caption(PROGRAM_NAME)
	fps_display = window.FPSDisplay(my_window)
	fps_display.label = text.Label("", x=FPS_POS_X, y=FPS_POS_Y)
	return my_window, fps_display
