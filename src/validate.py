#!/usr/bin/env python3
"""Validate map file"""

from re import search, sub

MIN_HEIGHT = -5
MAX_HEIGHT = 5
MAX_SIZE = 7

def _line_size(line):
	"""Counts the amount of fields in line"""
	line = sub("[ \t]+", " ", line) # Compress multipale spacers to single space
	return len(line.split())

def _validate_line(line, row, size):
	"""Validates a single lines format"""
	line = sub("[ \t]+", " ", line) # Compress multipale spacers to single space
	line_length = len(line)
	if line_length < 1:
		return

	match = search(r"^ ?([-]?\d[ ]?)+\n?", line) # match digits with space in between
	line = match.group()
	if len(line) != line_length:
		raise Exception(f"Line {row} contains none digits")

	line = line.strip("\n")
	if line.endswith(" "):
		raise Exception(f"Line {row} has trailing whitespace")

	count = 1
	points = line.split()
	for point in points:
		point = int(point)
		if count > MAX_SIZE:
			raise Exception(f"Line {row} exceeds max size ({MAX_SIZE})")
		elif point < MIN_HEIGHT:
			raise Exception(f"Line {row} '{point}' is smaller then min size ({MIN_HEIGHT})")
		elif point > MAX_HEIGHT:
			raise Exception(f"Line {row} '{point}' is bigger then max size ({MAX_HEIGHT})")
		count += 1
	count -= 1
	if count != size:
		raise Exception(f"Line {row} doesn't contain {size} entries ({count})")

def validate_map_file(map_file):
	try:
		if map_file.suffix != ".mod1":
			raise Exception("Invalid file extension expected '.mod1'")
		elif map_file.exists() == False:
			raise Exception(f"No such file '{map_file}'")

		row = 1
		content = map_file.read_text()
		content = content.strip()
		content = content.splitlines()
		if len(content) == 0:
			raise Exception(f"File '{map_file}' is empty")

		size = _line_size(content[0])
		for line in content:
			_validate_line(line, row, size)
			if row > MAX_SIZE:
				raise Exception(f"Lines in file exceeds max size ({MAX_SIZE})")
			if len(line) > 0:
				row += 1
	except Exception as error:
		print("Error:", error)
		exit(0)
