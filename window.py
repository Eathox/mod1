#!/usr/bin/env python
""" Window Management """

import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import glTranslatef, glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT
from OpenGL.GLU import gluPerspective

from const import WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT

def init_window():
    """ Initialise the application window """
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption(WINDOW_TITLE)
    glTranslatef(0, 0, -5)
    gluPerspective(60, (WINDOW_WIDTH / WINDOW_HEIGHT), 0.1, 1000)
    return (surface)

def _check_quit(event):
    """ Check if the event should quit """
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        return (False)
    elif (event.type == pygame.QUIT):
        return (False)
    return (True)

def event_loop_window(surface):
    """ Ctaches events """
    running = True
    while running:
        for event in pygame.event.get():
            running = _check_quit(event)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        pygame.display.flip()

