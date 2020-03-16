#!/usr/bin/env python3
"""Definition of setup manager"""

import sys

from . pip import *
from . library import *

class Manager:
	"""Manage all library dependencies"""

	def __init__(self, args, *libraries, pip="pip3"):
		"""Add args and collect all installed libraries"""
		self.platform = sys.platform.lower()
		self.args = list(map(str.lower, args))
		self.pip = pip
		self.libraries = []
		for name in libraries:
			self.libraries.append(Library(name, pip))

	def __str__(self) -> str:
		"""Return args and libraries in string form"""
		name = self.__class__.__name__
		library_names = list(map(str, self))
		return f"<{name}: {self.args}, {library_names}>"

	def __iter__(self) -> iter:
		"""Define iterator"""
		return self.libraries.__iter__()

	def pip_installed(self) -> bool:
		"""Checks if pip3 is installed"""
		arguments = ["-v"]
		return run_pip(self.pip, arguments, True)

	def installed_libraries(self) -> list:
		"""Return all allready installed libaraires"""
		libraries = []
		for library in self:
			if library.installed():
				libraries.append(library)
		return libraries

	def install_libraries(self) -> (bool, list):
		"""Installs all libraries"""
		installed = []
		for library in self:
			if library.installed() == True:
				continue
			success = library.install()
			if success == False or library.installed() == False:
				return False, installed
			installed.append(library)
		return True, installed

	def uninstall_libraries(self) -> (bool, list):
		"""Uninstalls all libraries"""
		uninstalled = []
		for library in self:
			if library.installed() == False:
				continue
			success, removed = library.uninstall()
			if success == False:
				return False, uninstalled
			elif removed:
				uninstalled.append(library)
		return True, uninstalled
