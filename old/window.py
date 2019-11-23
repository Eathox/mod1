#!/usr/bin/env python
"""Window Management"""

from os import environ

import pygame
from pygame.locals import DOUBLEBUF, OPENGL, RESIZABLE
from OpenGL.GL import GL_DEPTH_TEST, GL_BLEND, GL_SRC_ALPHA, \
    GL_ONE_MINUS_SRC_ALPHA, glTranslate, glRotate, glEnable, glBlendFunc, \
    glClearColor
from OpenGL.GLU import gluPerspective

from . const import NAME, FOV, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_RATIO, \
    BACKGROUND_COLOR
from . color import HexColor

# class Window:


def init_window(terrain):
    """Initialise the application window"""
    environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption(f"{NAME} - FPS: Unknown")
    gluPerspective(FOV, WINDOW_RATIO, 0.1, 1000)
    glTranslate(-(terrain.size / 2), -(terrain.height_3d / 2), -10)
    glRotate(45, -90, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    color = HexColor(BACKGROUND_COLOR)
    glClearColor(color.r, color.g, color.b, 1)
