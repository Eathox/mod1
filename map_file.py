#!/usr/bin/env python
""" Validation and reading of map files """

from re import search, sub

from numpy import zeros

from const import GRID_PADDING, MIN_HEIGHT, MAX_HEIGHT, MAX_SIZE

def _validate_line(line, row, terrain):
    """ Validates a single lines format """
    line = sub("[ \t]+", " ", line) # Compress multipale spacers to single space
    if (len(line) < 1):
        return ("Line {0} is empty".format(row))

    match = search(r"^([-]?\d[ ]?)+\n?", line) # match digits with space in between
    match = match.group()
    if (len(match) != len(line)):
        return ("Line {0} contains none digits".format(row))

    match = match.strip("\n")
    if (match.endswith(" ")):
        return ("Line {0} has trailing whitespace".format(row))

    count = 1
    points = match.split()
    terrain.points += [points]
    for point in points:
        point = int(point)
        if (count > MAX_SIZE):
            return ("Line {0} exceeds max size ({1})".format(row, MAX_SIZE))
        elif (point < MIN_HEIGHT):
            return ("Line {0} '{1}' is smaller then min size ({2})".format(row, point, MIN_HEIGHT))
        elif (point > MAX_HEIGHT):
            return ("Line {0} '{1}' is bigger then max size ({2})".format(row, point, MAX_HEIGHT))
        count += 1
    return ("")

def _validate_map_file(terrain):
    """ Validates file format """
    if (terrain.loc.endswith(".mod1") == False):
        return ("Invalid file extension expected '.mod1'")
    elif (terrain.file.exists() == False):
        return ("No such file")

    row = 1
    content = terrain.file.read_text()
    content = content.strip()
    content = content.splitlines()
    for line in content:
        terrain.error = _validate_line(line, row, terrain)
        if (row > MAX_SIZE):
            return ("Lines in file exceeds max size ({0})".format(MAX_SIZE))
        elif (terrain.error != ""):
            return (terrain.error)
        row += 1
    if (len(terrain.points) == 0):
        return ("File is empty")
    return (terrain.error)

def _grid_to_3d(terrain):
    layer = 0
    min_height = abs(MIN_HEIGHT)
    while (layer < terrain.height_3d):
        row = 0
        while (row < terrain.size):
            point = 0
            while (point < terrain.size):
                if (terrain.grid[row][point] >= (layer - min_height)):
                    terrain.grid_3d[layer][row][point] = 1
                else:
                    terrain.grid_3d[layer][row][point] = 0
                point += 1
            row += 1
        layer += 1

def read_map_file(terrain):
    """ Reads file into terrain format """
    terrain.error = _validate_map_file(terrain)
    if (terrain.error != ""):
        return (terrain.error)

    row = GRID_PADDING
    for line in terrain.points:
        i = GRID_PADDING
        for point in line:
            terrain.grid[row][i] = point
            i += 1
        row += 1
    terrain.grid = terrain.grid[::-1]
    _grid_to_3d(terrain)
    return ("")
