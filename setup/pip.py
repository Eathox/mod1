#!/usr/bin/env python3
"""Pip util functions"""

import subprocess

def run_pip(pip, arguments, silent=False) -> bool:
	"""Runs pip with arguments and returns success"""
	if silent == True:
		result = subprocess.run([pip, *arguments], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	else:
		result = subprocess.run([pip, *arguments])
	return (result.returncode == 0)
