#!/usr/bin/env python
"""Runs the mod1 program"""

from sys import argv

from tkinter import Tk

from const import USAGE, WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT

def _exit(_=None):
    exit(0)

def init_window():
    """Initialise the application window"""
    window = Tk()
    window.title(WINDOW_TITLE)
    window.resizable(False, False)
    window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
    window.bind("<Escape>", _exit)
    return (window)

if __name__ == "__main__":
    if (len(argv) != 2):
        print ("python", argv[0], USAGE)
        _exit()
    window = init_window()
    window.mainloop()
