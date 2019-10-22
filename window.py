#!/usr/bin/env python
""" Window Management """

from time import time

import pygame
from pygame.locals import DOUBLEBUF, OPENGL, RESIZABLE
from OpenGL.GL import GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_DEPTH_TEST, \
    GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, glTranslatef, glRotatef, \
    glEnable, glBlendFunc, glClearColor, glClear
from OpenGL.GLU import gluPerspective

from const import NAME, FOV, WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR, \
    MAX_SIZE, GRID_PADDING, WATER_ADD_RATE, MARCHING_CUBE_TERRAIN_ISO_LEVEL, \
    MARCHING_CUBE_WATTER_ISO_LEVEL
from color import hex_to_float
from water_modes import water_reset, water_fill
from draw_3d import draw_terrain_3d, draw_water_3d

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

def _quit_control(event):
    """ Quits if the event is a quit event """
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        return (False)
    elif (event.type == pygame.QUIT):
        return (False)
    return (True)

def _water_control(terrain, water_mode_func, event):
    """ Control water if its water control event """
    if (event.type != pygame.KEYDOWN):
        return (water_mode_func)
    if (event.key == pygame.K_SPACE):
        return (water_reset)
    elif (event.key == pygame.K_1):
        return (water_fill)
    return (water_mode_func)

def event_loop_window(terrain):
    """ Catches events """
    running = True
    frames = 0
    fps_start_time = time()
    water_start_time = time()
    water_mode_func = water_reset
    while running:
        for event in pygame.event.get():
            running = _quit_control(event)
            water_mode_func = _water_control(terrain, water_mode_func, event)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_terrain_3d(terrain)
        draw_water_3d(terrain)
        time_passed = (time() - water_start_time)
        water_mode_func(terrain, time_passed)
        water_start_time = time()

        time_passed = (time() - fps_start_time)
        if (time_passed >= 1):
            fps = frames // time_passed
            pygame.display.set_caption("{0} - FPS: {1}".format(NAME, str(fps)))
            fps_start_time = time()
            frames = 0
        pygame.display.flip()
        frames += 1
