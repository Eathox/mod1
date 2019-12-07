#!/usr/bin/env python3
"""Validate map file"""

from re import sub
from pathlib import Path

def	_open_map_file(file_name):
	map_file = Path(file_name)
	if len(map_file.suffix) == 0:
		map_file = Path(file_name + ".mod1")
	return map_file

def get_map_content(file_name):
	try:
		with _open_map_file(file_name) as map_file:
			if map_file.suffix != ".mod1":
				raise Exception("Invalid file extension expected '.mod1'")
			elif map_file.exists() == False:
				raise Exception(f"No such file '{map_file}'")

			content = map_file.read_text()
			content = content.strip()
			content = sub(r"[ \t]+", " ", content) # Compress multipale spacers to a single space
			content = sub(r"\n+", "\n", content) # Compress multipale newlines to a single newline
			if len(content) == 0:
				raise Exception(f"File '{map_file}' is empty")
			return content
	except Exception as error:
		print("Error:", error)
		exit(0)
