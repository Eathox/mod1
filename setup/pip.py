#!/usr/bin/env python
"""Pip util functions"""

from subprocess import run, PIPE

def run_pip(pip, arguments, silent=False):
	"""Runs pip with arguments and returns success"""
	if silent == True:
		success = run([pip] + arguments, stdout=PIPE, stderr=PIPE).returncode
	else:
		success = run([pip] + arguments).returncode
	return success == 0
