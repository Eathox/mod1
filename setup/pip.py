#!/usr/bin/env python3
"""Pip util functions"""

from subprocess import run, PIPE

def run_pip(pip, arguments, silent=False):
	"""Runs pip with arguments and returns success"""
	if silent == True:
		result = run([pip] + arguments, stdout=PIPE, stderr=PIPE)
	else:
		result = run([pip] + arguments)
	success = result.returncode
	return success == 0
