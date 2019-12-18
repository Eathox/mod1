#!/usr/bin/env python3
"""Opengl functions"""

from pyglet import gl

from OpenGL.GL import GL_DEPTH_TEST, GL_BLEND, GL_SRC_ALPHA, \
	GL_ONE_MINUS_SRC_ALPHA, glRotate, glEnable, glBlendFunc, glClearColor
from OpenGL.GLU import gluPerspective

from . color import HexColor
from . settings import WINDOW_RATIO, RENDER_FOV, COLOR_WINDOW

def init_opengl():
	"""Setup opengl"""
	gl_config = gl.Config()
	gluPerspective(RENDER_FOV, WINDOW_RATIO, 0.1, 1000)
	glRotate(45, -90, 0, 0)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	color = HexColor(COLOR_WINDOW)
	glClearColor(*color.array(True))
	return gl_config
