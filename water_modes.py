#!/usr/bin/env python
""" Water simulation modes """

from const import WATER_ADD_VOLUME, WATER_ADD_RATE

def water_reset(terrain, time_passed):
    terrain.water_3d.fill(0)

def water_rise(terrain, time_passed):
    layer = 0
    current_density = terrain.water_3d[layer][0][0]
    while (layer < (terrain.height_3d - 1) and current_density >= 1):
        current_density = terrain.water_3d[layer + 1][0][0]
        layer += 1
    next_density = current_density + (WATER_ADD_VOLUME * (time_passed / WATER_ADD_RATE))
    if (next_density > 1 and layer < (terrain.height_3d - 1)):
        left_over_density = next_density - 1
        next_density -= left_over_density
        terrain.water_3d[layer + 1].fill(left_over_density)
    terrain.water_3d[layer].fill(next_density)
