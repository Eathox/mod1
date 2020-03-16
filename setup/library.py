#!/usr/bin/env python3
"""Defintion of library"""

from . pip import *

class Library:
	"""A single library dependency"""

	def __init__(self, name, pip="pip3"):
		"""Define library with given pip"""
		self.name = name
		self.pip = pip

	def __str__(self) -> str:
		"""Return library name"""
		name = self.__class__.__name__
		return f"<{name}: {self.name}>"

	def installed(self) -> bool:
		"""Checks if the library is installed using shell"""
		arguments = ["show", self.name]
		return run_pip(self.pip, arguments, True)

	def install(self) -> bool:
		"""Installs library"""
		print(f"Installing {self.name}")
		arguments = ["install", self.name]
		success = run_pip(self.pip, arguments)
		if success == False:
			print(f"Failed to install {self.name}")
			return False
		return success

	def uninstall(self) -> (bool, bool):
		"""Uninstalls library"""
		arguments = ["uninstall", self.name]
		success = run_pip(self.pip, arguments)
		removed = (self.installed() == False)
		return success, removed
