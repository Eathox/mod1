#!/usr/bin/env python
"""Runs the mod1 program"""

from sys import argv

import pygame

from const import USAGE
from window import init_window, event_loop_window

if __name__ == "__main__":
    if (len(argv) != 2):
        print ("python", argv[0], USAGE)
        exit(0)

    surface = init_window()
    event_loop_window(surface)
    pygame.quit()
