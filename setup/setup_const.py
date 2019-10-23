#!/usr/bin/env python
""" Common setup constants """

from subprocess import run, PIPE
from sys import platform

class Setup:
    """ General setup information """
    pip = "pip3"
    libraries = [
        "numpy",
        "pygame",
        "pyopengl",
    ]

    def __init__(self, args):
        self.platform = platform.lower()
        self.args = list(map(str.lower, args))
        self._set_installed()

    def _library_installed_shell(self, library):
        """ Checks if the library is installed using shell """
        arguments = ["show", library]
        return (self._run_pip(arguments, True))

    def _set_installed(self):
        """ Set internal installed array """
        self.installed = []
        for library in self.libraries:
            if (self._library_installed_shell(library) == True):
                self.installed.append(library)

    def _run_pip(self, arguments, silent=False):
        """ Runs pip with arguments and returns success """
        if (silent == True):
            success = run([self.pip] + arguments, stdout=PIPE, stderr=PIPE).returncode
        else:
            success = run([self.pip] + arguments).returncode
        return (success == 0)

    def pip_installed(self):
        """ Checks if pip3 is installed """
        arguments = ["-V"]
        return (self._run_pip(arguments, True))

    def library_installed(self, library):
        """ Checks if the library is installed from the internal installed array """
        return (library in self.installed)

    def install_library(self, library):
        """ Installs library """
        print ("Installing {0}".format(library))
        arguments = ["install", library]
        success = self._run_pip(arguments)
        if (success == False):
            print ("Failed to install {0}".format(library))
            return (False)
        elif (library not in self.installed):
            self.installed.append(library)
        return (success)

    def uninstall_library(self, library):
        """ Uninstalls library """
        arguments = ["uninstall", library]
        success = self._run_pip(arguments)
        removed = self._library_installed_shell(library) == False
        if (success == False):
            return (False, removed)
        if (removed == True):
            self.installed.remove(library)
        return (success, removed)

    def install_libaries(self):
        """ Installs all libaries """
        installed = []
        for library in self.libraries:
            if (self.library_installed(library) == True):
                continue
            success = self.install_library(library)
            if (success == False or (self.library_installed(library) == False)):
                return (False, installed)
            installed.append(library)
        return (True, installed)

    def uninstall_libaries(self):
        """ Uninstalls all libaries """
        uninstalled = []
        for library in self.libraries:
            if (self.library_installed(library) == False):
                continue
            success, removed = self.uninstall_library(library)
            if (success == False):
                return (False, uninstalled)
            elif (removed):
                uninstalled.append(library)
        return (True, uninstalled)
