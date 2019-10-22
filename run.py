#!/usr/bin/env python
""" Runs the mod1 program """

from sys import argv

import pygame

from map_file import read_map_file
from const import USAGE, Terrain
from window import init_window, event_loop_window

if __name__ == "__main__":
    """ Read terrain and run simulation """
    if (len(argv) != 2):
        print ("Usage: python3", argv[0], USAGE)
        exit(0)

    terrain = Terrain(argv[1])
    terrain.error = read_map_file(terrain)
    if (terrain.error != ""):
        print ("Error: " + terrain.error)
        exit(0)

    init_window(terrain)
    event_loop_window(terrain)
    pygame.quit()
    quit()
