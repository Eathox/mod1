#!/usr/bin/env python
""" General draw functions """

from OpenGL.GL import GL_LINES, GL_TRIANGLES, glBegin, glEnd, glVertex3f, \
    glColor3fv, glColor4fv

from . const import MIN_HEIGHT, MAX_HEIGHT, DRAW_HEIGHT_WEIGHT, WATER_COLOR, \
    TERRAIN_COLOR_HIGH, TERRAIN_COLOR_MID, TERRAIN_COLOR_LOW, \
    DRAW_COLOR_INTENSITY_WEIGHT
from . color import hex_to_float

def draw_vertex_terrain(vertex):
    """ Draws point with terrain height color """
    z = vertex[2]
    if (z < 0 and z <= (MIN_HEIGHT / 2)):
        color = TERRAIN_COLOR_LOW
    elif (z > 0 and z >= (MAX_HEIGHT / 2)):
        color = TERRAIN_COLOR_HIGH
    else:
        color = TERRAIN_COLOR_MID

    color = hex_to_float(color)
    if (z < 0):
        minium_intensity = MIN_HEIGHT / (MIN_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT)
        intensity = (z / (MIN_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT))
        # intensity = 1 - (z / (MIN_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT))
    else:
        minium_intensity = MAX_HEIGHT / (MAX_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT)
        intensity = (z / (MAX_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT))
        # intensity = 1 - (z / (MAX_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT))
    intensity += minium_intensity
    color[0] = color[0] * intensity
    color[1] = color[1] * intensity
    color[2] = color[2] * intensity

    glColor3fv(color)
    glVertex3f(vertex[0], vertex[1], z * DRAW_HEIGHT_WEIGHT)

def draw_vertex_water(vertex):
    """ Draws point with water color """
    z = vertex[2]
    color = hex_to_float(WATER_COLOR, True)
    glColor4fv(color)
    glVertex3f(vertex[0], vertex[1], z * DRAW_HEIGHT_WEIGHT)
