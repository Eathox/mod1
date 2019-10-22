#!/usr/bin/env python
""" Install all library dependencies constants """

from os import system
from sys import argv, platform

g_libraries = [
    "numpy",
    "pygame",
    "pyopengl"
]

def _check_pip3():
    """ Checks if pip3 is installed """
    command = "pip3 -V 1>/dev/null 2>/dev/null"
    installed = system(command)
    return (installed == 0)

def _check_library_installed(libray):
    """ Checks if the library is installed """
    command = "pip3 show " + libray + " 1>/dev/null 2>/dev/null"
    installed = system(command)
    return (installed == 0)

def _install_library(libray):
    """ Installs library """
    command = "pip3 install " + libray
    installed = system(command)
    return (installed == 0)

def _uninstall_library(libray):
    """ Uninstalls library """
    command = "pip3 uninstall " + libray
    installed = system(command)
    return (installed == 0)

def _install_libaries():
    """ Installs all libaries """
    installed = []
    for libray in g_libraries:
        if (_check_library_installed(libray) == False):
            print ("Installing " + libray)
            installed.append(libray)
            success = _install_library(libray)
            if (success == False):
                print ("Failed to install " + libray)
                exit()
    if (installed == []):
        print("All dependencies allready installed")
    else:
        print ("\nSuccessfully installed:")
        for libray in installed:
            print ("  " + libray)

def _uninstall_libaries():
    """ Uninstalls all libaries """
    uninstalled = []
    for libray in g_libraries:
        if (_check_library_installed(libray) == True):
            uninstalled.append(libray)
            success = _uninstall_library(libray)
    if (uninstalled == []):
        print("All dependencies allready uninstalled")
    else:
        print ("\nSuccessfully uninstalled:")
        for libray in uninstalled:
            print ("  " + libray)

if __name__ == "__main__":
    """ Setup dependencies """
    if (_check_pip3() == False):
        kernel = platform
        if (kernel.lower() == "linux"):
            print ("pip3 is not installed.\nConsider runing: 'sudo apt install python3-pip' to install")
        elif (kernel.lower() == "darwin"):
            print ("pip3 is not installed.\nConsider runing: 'brew install python3' to install")
        elif (kernel.lower() == "win32"):
            print ("pip3 is not installed.\nConsider runing: 'python3 get-pip.py' to install")
        else:
            print ("Unrecognized kernel, unable to provide install suggestion")
        exit()

    args = list(map(str.lower, argv[1:])) # case insensitive argv
    if (("--uninstall" in args) or ("--remove" in args)):
        _uninstall_libaries()
    else:
        _install_libaries()
