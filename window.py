#!/usr/bin/env python
""" Window Management """

from time import time

import pygame
from pygame.locals import DOUBLEBUF, OPENGL, RESIZABLE
from OpenGL.GL import GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_DEPTH_TEST, \
    GL_LEQUAL, GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, glTranslatef, \
    glRotatef, glEnable, glBlendFunc, glDepthFunc, glClearColor, glClear
from OpenGL.GLU import gluPerspective

from const import NAME, FOV, WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR, \
    MAX_SIZE, GRID_PADDING, MARCHING_CUBE_TERRAIN_ISO_LEVEL, \
    MARCHING_CUBE_WATTER_ISO_LEVEL
from color import hex_to_float
from draw_vertex import draw_vertex_terrain, draw_vertex_water
from draw_3d import draw_3d

def init_window(terrain):
    """ Initialise the application window """
    pygame.init()
    resolution = (WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.display.set_mode(resolution, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("{0} - FPS: Unknown".format(NAME))
    gluPerspective(FOV, (resolution[0] / resolution[1]), 0.1, 1000)
    glTranslatef(-(terrain.size / 2), -(terrain.height_3d / 2), -10)
    glRotatef(45, -90, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    color = hex_to_float(BACKGROUND_COLOR)
    glClearColor(color[0], color[1], color[2], 1)

def _check_quit(event):
    """ Check if the event should quit """
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        return (False)
    elif (event.type == pygame.QUIT):
        return (False)
    return (True)

def _get_fps(start_time, cur_time, frames):
    fps = frames // cur_time
    frames = 0
    cur_time = 0
    start_time = 0
    return (fps)

def event_loop_window(terrain):
    """ Catches events """
    running = True
    frames = 0
    start_time = time()
    while running:
        for event in pygame.event.get():
            running = _check_quit(event)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_3d(terrain, terrain.grid_3d, draw_vertex_terrain, MARCHING_CUBE_TERRAIN_ISO_LEVEL)
        draw_3d(terrain, terrain.water_3d, draw_vertex_water, MARCHING_CUBE_WATTER_ISO_LEVEL)

        frames += 1
        cur_time = time() - start_time
        if (cur_time > 1):
            fps = _get_fps(start_time, cur_time, frames)
            pygame.display.set_caption("{0} - FPS: {1}".format(NAME, str(fps)))
        pygame.display.flip()
