#!/usr/bin/env python3
"""Window management"""

from os import environ

import pygame
from pygame.locals import DOUBLEBUF, OPENGL, RESIZABLE
from OpenGL.GL import GL_DEPTH_TEST, GL_BLEND, GL_SRC_ALPHA, \
    GL_ONE_MINUS_SRC_ALPHA, glTranslate, glRotate, glEnable, glBlendFunc, \
    glClearColor
from OpenGL.GLU import gluPerspective

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_RATIO = (WINDOW_WIDTH / WINDOW_HEIGHT)

class Window:
	""""""

	def __init__(self, name, fov):
		"""Initialise the application window"""
		environ['SDL_VIDEO_CENTERED'] = '1'
		pygame.init()
		print(self.display)
		pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
		pygame.display.set_caption(f"{name} - FPS: Unknown")

		gluPerspective(fov, WINDOW_RATIO, 0.1, 1000)
		glRotate(45, -90, 0, 0)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
