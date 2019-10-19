#!/usr/bin/env python
""" Runs the mod1 program """

from sys import argv

import pygame

from map_file import read_map_file
from const import USAGE, Terrain
from window import init_window, event_loop_window

if __name__ == "__main__":
    if (len(argv) != 2):
        print ("python", argv[0], USAGE)
        exit_application()

    terrain = Terrain(argv[1])
    terrain.error = read_map_file(terrain)
    if (terrain.error != ""):
        print ("Error: " + terrain.error)
        exit(0)

    surface = init_window()
    event_loop_window(surface)
    pygame.quit()
    quit()
