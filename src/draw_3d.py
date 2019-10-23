#!/usr/bin/env python
""" 3d Terrain rendering """

from OpenGL.GL import GL_LINES, GL_TRIANGLES, glBegin, glEnd

from . const import MARCHING_CUBE_EDGE_TABLE, MARCHING_CUBE_TRIANGLE_TABLE, \
    MARCHING_CUBE_INDEX_START_TABLE, MARCHING_CUBE_INDEX_END_TABLE, \
    MIN_HEIGHT, MARCHING_CUBE_TERRAIN_ISO_LEVEL, MARCHING_CUBE_WATTER_ISO_LEVEL
from . draw_vertex import draw_vertex_terrain, draw_vertex_water

def _get_corner(point, row, layer):
    """ Gets the cube vertices """
    corners = [
        (point, row, layer),
        (point + 1, row, layer),
        (point + 1, row, layer + 1),
        (point, row, layer + 1),
        (point, row + 1, layer),
        (point + 1, row + 1, layer),
        (point + 1, row + 1, layer + 1),
        (point, row + 1, layer + 1)
    ]
    return (corners)

def _density_from_vertex(grid, vertex):
    """ Gets vertex's density """
    return (grid[vertex[2]][vertex[1]][vertex[0]])

def _get_active_corners(grid, iso_level, corners):
    """ Checks which corner falls in cube """
    active_corners = 0
    if (_density_from_vertex(grid, corners[0]) < iso_level):
        active_corners |= 1
    if (_density_from_vertex(grid, corners[1]) < iso_level):
        active_corners |= 2
    if (_density_from_vertex(grid, corners[2]) < iso_level):
        active_corners |= 4
    if (_density_from_vertex(grid, corners[3]) < iso_level):
        active_corners |= 8
    if (_density_from_vertex(grid, corners[4]) < iso_level):
        active_corners |= 16
    if (_density_from_vertex(grid, corners[5]) < iso_level):
        active_corners |= 32
    if (_density_from_vertex(grid, corners[6]) < iso_level):
        active_corners |= 64
    if (_density_from_vertex(grid, corners[7]) < iso_level):
        active_corners |= 128
    return (active_corners)

def _interpolate(grid, start, end, iso_level):
    """ Interpolate between start and end """
    start_density = _density_from_vertex(grid, start)
    end_density = _density_from_vertex(grid, end)
    t = (iso_level - start_density) / (end_density - start_density)
    return (
        start[0] + (t * (end[0] - start[0])),
        start[1] + (t * (end[1] - start[1])),
        (start[2] + (t * (end[2] - start[2]))) - abs(MIN_HEIGHT)
    )

def _draw_cube(grid, point, row, layer, draw_vertex_func, iso_level):
    """ Draw individual cube """
    corners = _get_corner(point, row, layer)
    active_corners = _get_active_corners(grid, iso_level, corners)

    i = 0
    table_length = len(MARCHING_CUBE_TRIANGLE_TABLE[active_corners])
    while (i < table_length):
        cord = MARCHING_CUBE_TRIANGLE_TABLE[active_corners][i]
        start = MARCHING_CUBE_INDEX_START_TABLE[cord]
        end = MARCHING_CUBE_INDEX_END_TABLE[cord]
        vertex = _interpolate(grid, corners[start], corners[end], iso_level)
        draw_vertex_func(vertex)
        i += 1

def draw_terrain_3d(terrain):
    """ Draw terrain density grid """
    glBegin(GL_TRIANGLES)
    layer = 0
    while (layer < terrain.height_3d - 1):
        row = 0
        while (row < terrain.size - 1):
            point = 0
            while (point < terrain.size - 1):
                _draw_cube(terrain.grid_3d, point, row, layer, draw_vertex_terrain, MARCHING_CUBE_TERRAIN_ISO_LEVEL)
                point += 1
            row += 1
        layer += 1
    glEnd()

def draw_water_3d(terrain):
    """ Draw water density grid """
    glBegin(GL_TRIANGLES)
    terrain.water_3d[terrain.height_3d - 1].fill(0)
    layer = 0
    while (layer < terrain.height_3d - 1):
        row = 0
        while (row < terrain.size - 1):
            point = 0
            while (point < terrain.size - 1):
                _draw_cube(terrain.water_3d, point, row, layer, draw_vertex_water, MARCHING_CUBE_WATTER_ISO_LEVEL)
                point += 1
            row += 1
        layer += 1
    glEnd()
