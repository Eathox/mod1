#!/usr/bin/env python
""" Window Management """

import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_DEPTH_TEST, \
    GL_LEQUAL, glTranslatef, glRotatef, glEnable, glDepthFunc, glClearColor, \
    glClear
from OpenGL.GLU import gluPerspective

from const import NAME, FOV, WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR, \
    MAX_SIZE, GIRD_PADDING
from color import hex_to_float
from draw_terrain import draw_terrain

def init_window():
    """ Initialise the application window """
    pygame.init()
    resolution = (WINDOW_WIDTH, WINDOW_HEIGHT)
    surface = pygame.display.set_mode(resolution, DOUBLEBUF | OPENGL)
    pygame.display.set_caption(NAME)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    gluPerspective(FOV, (resolution[0] / resolution[1]), 0.1, 1000)
    cam_offset = (MAX_SIZE + GIRD_PADDING) / 2
    glTranslatef(-cam_offset, -cam_offset, -10)
    glRotatef(45, -90, 0, 0)
    return (surface)

def _check_quit(event):
    """ Check if the event should quit """
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        return (False)
    elif (event.type == pygame.QUIT):
        return (False)
    return (True)

def event_loop_window(terrain):
    """ Catches events """
    running = True
    while running:
        for event in pygame.event.get():
            running = _check_quit(event)

        color = hex_to_float(BACKGROUND_COLOR)
        glClearColor(color[0], color[1], color[2], 255)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_terrain(terrain)
        pygame.display.flip()
