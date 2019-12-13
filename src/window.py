#!/usr/bin/env python3
"""Window management"""

from os import environ

from pyglet import gl, window, text
from OpenGL.GL import GL_DEPTH_TEST, GL_BLEND, GL_SRC_ALPHA, \
	GL_ONE_MINUS_SRC_ALPHA, glRotate, glEnable, glBlendFunc
from OpenGL.GLU import gluPerspective

from . color import HexColor
from . settings import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_RATIO, FPS_POS_X, FPS_POS_Y

def init_window(name, fov):
	"""Initialise the application window"""
	gl_config = gl.Config()
	my_window = window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, config=gl_config)
	my_window.set_caption(name)
	fps_display = window.FPSDisplay(my_window)
	fps_display.label = text.Label("", x=FPS_POS_X, y=FPS_POS_Y)

	gluPerspective(fov, WINDOW_RATIO, 0.1, 1000)
	glRotate(45, -90, 0, 0)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	return my_window, fps_display
