#!/usr/bin/env python3
"""Validation and reading of map files"""

from re import search, sub

from numpy import zeros

GRID_PADDING = 2 # Grid border badding
MIN_HEIGHT = -5
MAX_HEIGHT = 5
MAX_SIZE = 7

class Terrain:
    """Holds general information about map"""
    size = MAX_SIZE + (GRID_PADDING * 2)
    height_3d = (abs(MIN_HEIGHT) + abs(MAX_HEIGHT)) + 2 # To account for overflow on top and bottom
    error = ""
    points = []
    grid = zeros((size, size))
    grid_3d = zeros((height_3d, size, size))
    water_3d = zeros((height_3d, size, size))

    def __init__(self, file_path):
        self.loc = file_path
        self.file = Path(file_path)

def _validate_line(line, row, terrain):
    """Validates a single lines format"""
    line = sub("[ \t]+", " ", line) # Compress multipale spacers to single space
    if len(line) < 1:
        return f"Line {row} is empty"

    match = search(r"^([-]?\d[ ]?)+\n?", line) # match digits with space in between
    match = match.group()
    if len(match) != len(line):
        return f"Line {row} contains none digits"

    match = match.strip("\n")
    if match.endswith(" "):
        return f"Line {row} has trailing whitespace"

    count = 1
    points = match.split()
    terrain.points += [points]
    for point in points:
        point = int(point)
        if count > MAX_SIZE:
            return f"Line {row} exceeds max size ({MAX_SIZE})"
        elif point < MIN_HEIGHT:
            return f"Line {row} '{point}' is smaller then min size ({MIN_HEIGHT})"
        elif point > MAX_HEIGHT:
            return f"Line {row} '{point}' is bigger then max size ({MAX_HEIGHT})"
        count += 1
    return ""

def _validate_map_file(terrain):
    """Validates file format"""
    if terrain.loc.endswith(".mod1") == False:
        return "Invalid file extension expected '.mod1'"
    elif terrain.file.exists() == False:
        return "No such file"

    row = 1
    content = terrain.file.read_text()
    content = content.strip()
    content = content.splitlines()
    for line in content:
        terrain.error = _validate_line(line, row, terrain)
        if row > MAX_SIZE:
            return f"Lines in file exceeds max size ({MAX_SIZE})"
        elif terrain.error != "":
            return terrain.error
        row += 1
    if len(terrain.points) == 0:
        return "File is empty"
    return terrain.error

def _grid_to_3d(terrain):
    min_height = abs(MIN_HEIGHT)
    for layer in range(terrain.height_3d):
        for row in range(terrain.size):
            for point in range(terrain.size):
                if terrain.grid[row][point] >= (layer - min_height):
                    terrain.grid_3d[layer][row][point] = 1
                else:
                    terrain.grid_3d[layer][row][point] = 0

def read_map_file(terrain):
    """Reads file into terrain format"""
    terrain.error = _validate_map_file(terrain)
    if terrain.error != "":
        return terrain.error

    row = GRID_PADDING
    for line in terrain.points:
        i = GRID_PADDING
        for point in line:
            terrain.grid[row][i] = point
            i += 1
        row += 1
    terrain.grid = terrain.grid[::-1]
    _grid_to_3d(terrain)
    return ""
