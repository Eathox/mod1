#!/usr/bin/env python3
"""Definition of setup manager"""

from sys import platform

from . pip import run_pip
from . library import Library

class Manager:
	"""Manage all library dependencies"""

	def __init__(self, args, *libraries, pip="pip3"):
		"""Add args and collect all installed libraries"""
		self.platform = platform.lower()
		self.args = list(map(str.lower, args))
		self.pip = pip
		self.libraries = []
		for name in libraries:
			self.libraries.append(Library(name, pip))

	def __str__(self):
		"""Return args and libraries in string form"""
		name = self.__class__.__name__
		library_names = list(map(str, self))
		return f"<{name}: {self.args}, {library_names}>"

	def __iter__(self):
		"""Define iterator"""
		return self.libraries.__iter__()

	def pip_installed(self):
		"""Checks if pip3 is installed"""
		arguments = ["-V"]
		return run_pip(self.pip, arguments, True)

	def install_libraries(self):
		"""Installs all libraries"""
		installed = []
		for library in self:
			if library.library_installed() == True:
				continue
			success = library.install_library()
			if success == False or library.library_installed() == False:
				return False, installed
			installed.append(library)
		return True, installed

	def uninstall_libraries(self):
		"""Uninstalls all libraries"""
		uninstalled = []
		for library in self:
			if library.library_installed() == False:
				continue
			success, removed = library.uninstall_library()
			if success == False:
				return False, uninstalled
			elif removed:
				uninstalled.append(library)
		return True, uninstalled
