#!/usr/bin/env python
"""3d Terrain rendering"""

from OpenGL.GL import GL_LINES, GL_TRIANGLES, glBegin, glEnd

from . const import MARCHING_CUBE_EDGE_TABLE, MARCHING_CUBE_TRIANGLE_TABLE, \
    MARCHING_CUBE_INDEX_START_TABLE, MARCHING_CUBE_INDEX_END_TABLE, \
    MIN_HEIGHT, MARCHING_CUBE_TERRAIN_ISO_LEVEL, MARCHING_CUBE_WATTER_ISO_LEVEL
from . draw_vertex import draw_vertex_terrain, draw_vertex_water

def _get_corner(point, row, layer):
    """Gets the cube vertices"""
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
    return corners

def _density_from_vertex(grid, vertex):
    """Gets vertex's density"""
    return grid[vertex[2]][vertex[1]][vertex[0]]

def _get_active_corners(grid, iso_level, corners):
    """Checks which corner falls in cube"""
    active_corners = 0
    for i in range(len(corners)):
        if _density_from_vertex(grid, corners[i]) < iso_level:
            active_corners |= (1 << i)
    return active_corners

def _interpolate(grid, start, end, iso_level):
    """Interpolate between start and end"""
    start_density = _density_from_vertex(grid, start)
    end_density = _density_from_vertex(grid, end)
    interpolate = (iso_level - start_density) / (end_density - start_density)
    return (
        start[0] + (interpolate * (end[0] - start[0])),
        start[1] + (interpolate * (end[1] - start[1])),
        (start[2] + (interpolate * (end[2] - start[2]))) - abs(MIN_HEIGHT)
    )

def _draw_cube(grid, point, row, layer, draw_vertex_func, iso_level):
    """Draw individual cube"""
    corners = _get_corner(point, row, layer)
    active_corners = _get_active_corners(grid, iso_level, corners)

    table_length = len(MARCHING_CUBE_TRIANGLE_TABLE[active_corners])
    for i in range(table_length):
        cord = MARCHING_CUBE_TRIANGLE_TABLE[active_corners][i]
        start = MARCHING_CUBE_INDEX_START_TABLE[cord]
        end = MARCHING_CUBE_INDEX_END_TABLE[cord]
        vertex = _interpolate(grid, corners[start], corners[end], iso_level)
        draw_vertex_func(vertex)

def draw_terrain_3d(terrain):
    """Draw terrain density grid"""
    glBegin(GL_TRIANGLES)
    for layer in range(terrain.height_3d - 1):
        for row in range(terrain.size - 1):
            for point in range(terrain.size - 1):
                _draw_cube(terrain.grid_3d, point, row, layer, draw_vertex_terrain, MARCHING_CUBE_TERRAIN_ISO_LEVEL)
    glEnd()

def draw_water_3d(terrain):
    """Draw water density grid"""
    glBegin(GL_TRIANGLES)
    terrain.water_3d[terrain.height_3d - 1].fill(0)
    for layer in range(terrain.height_3d - 1):
        for row in range(terrain.size - 1):
            for point in range(terrain.size - 1):
                _draw_cube(terrain.water_3d, point, row, layer, draw_vertex_water, MARCHING_CUBE_WATTER_ISO_LEVEL)
    glEnd()
