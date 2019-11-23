#!/usr/bin/env python
"""Common setup constants"""

from sys import platform
from subprocess import run, PIPE

def _run_pip(pip, arguments, silent=False):
	"""Runs pip with arguments and returns success"""
	if silent == True:
		success = run([pip] + arguments, stdout=PIPE, stderr=PIPE).returncode
	else:
		success = run([pip] + arguments).returncode
	return success == 0

class Library:
	"""A single library dependency"""

	def __init__(self, name, pip="pip3"):
		"""Define library with given pip"""
		self.platform = platform.lower()
		self.name = name
		self.pip = pip

	def __str__(self):
		"""Return library name"""
		name = self.__class__.__name__
		return f"<{name}: {self.name}>"

	def library_installed(self):
		"""Checks if the library is installed using shell"""
		arguments = ["show", self.name]
		return _run_pip(self.pip, arguments, True)

	def install_library(self):
		"""Installs library"""
		print(f"Installing {self.name}")
		arguments = ["install", self.name]
		success = _run_pip(self.pip, arguments)
		if success == False:
			print(f"Failed to install {self.name}")
			return False
		return success

	def uninstall_library(self):
		"""Uninstalls library"""
		arguments = ["uninstall", self.name]
		success = _run_pip(self.pip, arguments)
		removed = self.library_installed() == False
		if success == False:
			return False, removed
		return success, removed

class Setup:
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
		return _run_pip(self.pip, arguments, True)

	def install_libraries(self):
		"""Installs all libraries"""
		installed = []
		for library in self:
			if library.library_installed() == True:
				continue
			success = library.install_library()
			if success == False or library.library_installed() == False:
				return False, installed
		return True, installed

	def uninstall_libraries(self):
		"""Uninstalls all libraries"""
		uninstalled = []
		for library in self:
			if library.library_installed() == False:
				continue
			success = library.uninstall_library()
			if success == False:
				return False, uninstalled
		return True, uninstalled
