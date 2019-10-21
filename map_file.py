#!/usr/bin/env python
""" Validation and reading of map files """

from re import search, sub

from const import GIRD_PADDING, MIN_HEIGHT, MAX_HEIGHT, MAX_SIZE

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

def read_map_file(terrain):
    """ Reads file into terrain format """
    terrain.error = _validate_map_file(terrain)
    if (terrain.error != ""):
        return (terrain.error)

    total_size = MAX_SIZE + (GIRD_PADDING * 2)
    for line in terrain.points:
        row = [0] * GIRD_PADDING # fill front with zero padding
        i = len(line)
        for point in line:
            row.append(int(point))
        while (i < total_size - GIRD_PADDING): # fill remaining points with zero padding
            row.append(0)
            i += 1
        terrain.grid.append(row)

    i = len(terrain.points)
    while (i < total_size - GIRD_PADDING): # fill remaining with zero padding
        terrain.grid.append([0] * total_size)
        i += 1
    while (i < total_size): # fill front with zero padding
        terrain.grid.insert(0, [0] * total_size)
        i += 1
    terrain.grid.reverse()
    return ("")
