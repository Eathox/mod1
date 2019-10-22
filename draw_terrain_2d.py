#!/usr/bin/env python
""" 2d Terrain rendering (Legacy code) """

from OpenGL.GL import GL_LINES, GL_TRIANGLES, glBegin, glEnd

from draw import draw_color

def _draw_edge(terrain, row, rowCount):
    """ Draws edge wire frame """
    glBegin(GL_LINES)
    point = 0
    rowLength = len(terrain.grid[row])
    while (point < rowLength):
        if (point + 1 < rowLength):
            top_left = (point, row, terrain.grid[row][point])
            top_right = (point + 1, row, terrain.grid[row][point + 1])
            draw_color(top_left)
            draw_color(top_right)

        if (row + 1 < rowCount):
            top_left = (point, row, terrain.grid[row][point])
            bottom_left = (point, row + 1, terrain.grid[row + 1][point])
            draw_color(top_left)
            draw_color(bottom_left)

        if (point + 1 < rowLength and row + 1 < rowCount):
            bottom_right = (point + 1, row + 1, terrain.grid[row + 1][point + 1])

            middle_height = (top_left[2] + top_right[2] + bottom_left[2] + bottom_right[2]) / 4
            middle = (point + 0.5, row + 0.5, middle_height)
            draw_color(top_left)
            draw_color(middle)

            draw_color(top_right)
            draw_color(middle)

            draw_color(bottom_left)
            draw_color(middle)

            draw_color(bottom_right)
            draw_color(middle)
        point += 1
    glEnd()

def _draw_surface(terrain, row, rowCount):
    """ Fills in the wire frame """
    if (row + 1 == rowCount):
        return
    glBegin(GL_TRIANGLES)

    point = 0
    rowLength = len(terrain.grid[row])
    while (point < rowLength - 1):
        top_left = (point, row, terrain.grid[row][point])
        top_right = (point + 1, row, terrain.grid[row][point + 1])
        bottom_left = (point, row + 1, terrain.grid[row + 1][point])
        bottom_right = (point + 1, row + 1, terrain.grid[row + 1][point + 1])

        middle_height = (top_left[2] + top_right[2] + bottom_left[2] + bottom_right[2]) / 4
        middle = (point + 0.5, row + 0.5, middle_height)
        draw_color(top_left)
        draw_color(top_right)
        draw_color(middle)

        draw_color(top_right)
        draw_color(bottom_right)
        draw_color(middle)

        draw_color(bottom_right)
        draw_color(bottom_left)
        draw_color(middle)

        draw_color(bottom_left)
        draw_color(top_left)
        draw_color(middle)
        point += 1
    glEnd()

def draw_terrain_2d(terrain):
    """ Render 2d terrain """
    row = 0
    rowCount = len(terrain.grid)
    while (row < rowCount):
        _draw_edge(terrain, row, rowCount)
        # _draw_surface(terrain, row, rowCount)
        row += 1
