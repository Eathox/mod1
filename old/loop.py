#!/usr/bin/env python
"""Window event loop"""

from time import time

import pygame
from OpenGL.GL import GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, glClear

from . const import NAME
from . water_modes import water_reset, water_hold, water_rise
from . draw_3d import draw_terrain_3d, draw_water_3d

def event_loop_window(terrain):
    """Catches events"""
    frames = 0
    running = True
    fps_start_time = time()
    water_start_time = fps_start_time
    water_mode_func = water_hold
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
        if time_passed >= 1:
            fps = frames // time_passed
            pygame.display.set_caption(f"{NAME} - FPS: {fps}")
            fps_start_time = time()
            frames = 0
        pygame.display.flip()
        frames += 1

def _quit_control(event):
    """Quits if the event is a quit event"""
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return False
    elif event.type == pygame.QUIT:
        return False
    return True

def _water_control(terrain, water_mode_func, event):
    """Control water if its water control event"""
    if event.type != pygame.KEYDOWN:
        return water_mode_func
    elif event.key == pygame.K_SPACE:
        return water_hold
    elif event.key == pygame.K_r:
        return water_reset
    elif event.key == pygame.K_1:
        return water_rise
    return water_mode_func
