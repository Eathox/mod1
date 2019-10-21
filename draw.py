#!/usr/bin/env python
""" General draw functions """

from OpenGL.GL import GL_LINES, GL_TRIANGLES, glBegin, glEnd, glVertex3f, \
    glColor3fv
from const import MIN_HEIGHT, MAX_HEIGHT, DRAW_HEIGHT_WEIGHT, \
    TERRAIN_COLOR_HIGH, TERRAIN_COLOR_MID, TERRAIN_COLOR_LOW, \
    DRAW_COLOR_INTENSITY_WEIGHT
from color import hex_to_float

def draw_color(v):
    """ Draws point with height color """
    z = v[2]
    if (z < 0 and z <= (MIN_HEIGHT / 2)):
        color = TERRAIN_COLOR_LOW
    elif (z > 0 and z >= (MAX_HEIGHT / 2)):
        color = TERRAIN_COLOR_HIGH
    else:
        color = TERRAIN_COLOR_MID

    color = hex_to_float(color)
    if (z < 0):
        # intensity = MIN_HEIGHT / (MIN_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT)
        # intensity += z / (MIN_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT)
        intensity = 1 - (z / (MIN_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT))
    else:
        # intensity = MAX_HEIGHT / (MAX_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT)
        # intensity += z / (MAX_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT)
        intensity = 1 - (z / (MAX_HEIGHT * DRAW_COLOR_INTENSITY_WEIGHT))
    color[0] = color[0] * intensity
    color[1] = color[1] * intensity
    color[2] = color[2] * intensity

    glColor3fv(color)
    glVertex3f(v[0], v[1], z * DRAW_HEIGHT_WEIGHT)
