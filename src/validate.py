#!/usr/bin/env python3
"""Validate map file"""

from re import search

from . terrain import MAX_SIZE, MAX_HEIGHT, MIN_HEIGHT

def _line_size(line):
	"""Counts the amount of fields in line"""
	return len(line.split())

def _validate_line(line, row, size):
	"""Validates a single lines format"""
	full_len = len(line)
	match = search(r"^ ?([-]?\d[ ]?)+\n?", line) # match digits with space in between
	line = match.group()
	if len(line) != full_len:
		raise Exception(f"Line {row} contains none digits")

	line = line.strip("\n")
	if line.endswith(" "):
		raise Exception(f"Line {row} has trailing whitespace")

	count = 0
	points = line.split()
	for point in points:
		point = int(point)
		if (count + 1) > MAX_SIZE:
			raise Exception(f"Line {row} exceeds max size ({MAX_SIZE})")
		elif point < MIN_HEIGHT:
			raise Exception(f"Line {row} '{point}' is smaller then min size ({MIN_HEIGHT})")
		elif point > MAX_HEIGHT:
			raise Exception(f"Line {row} '{point}' is bigger then max size ({MAX_HEIGHT})")
		count += 1

	if count != size:
		raise Exception(f"Line {row} contains {count} entries, expected {size}")

def validate_map_file(map_content):
	""""""
	try:
		row = 1
		lines = map_content.splitlines()
		size = _line_size(lines[0])
		for line in lines:
			_validate_line(line, row, size)
			if row > MAX_SIZE:
				raise Exception(f"Lines in file exceeds max size ({MAX_SIZE})")
			if len(line) > 0:
				row += 1
	except Exception as error:
		print("Error:", error)
		exit(0)
