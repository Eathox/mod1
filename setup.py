#!/usr/bin/env python
""" Install all library dependencies constants """

from sys import argv

from setup import setup_const

def _print_action_result(success, libraries, action_string):
    """ print install or uninstall action results """
    if (success == False):
        print ("Failed to {0} all dependencies".format(action_string))
    if (libraries == [] and success == True):
        print("All dependencies allready {0}.".format(action_string))
    elif (libraries != []):
        print ("\nSuccessfully {0} the following:".format(action_string))
        for library in libraries:
            print (" - {0}".format(library))

if __name__ == "__main__":
    """ Setup dependencies """
    setup = setup_const.Setup(argv[1:])
    if (setup.pip_installed() == False):
        suggestion = "Unrecognized kernel, unable to provide install suggestion."
        if (setup.platform == "linux"):
            suggestion = "Consider runing: 'sudo apt install python3-pip' to install."
        elif (setup.platform == "darwin"):
            suggestion = "Consider runing: 'brew install python3' to install."
        elif (setup.platform == "win32"):
            suggestion = "Consider runing: 'python3 get-pip.py' to install."
        print ("{0} is not installed.\n{1}".format(setup.pip, suggestion))
        exit()

    if (("--uninstall" in setup.args) or ("--remove" in setup.args)):
        success, libraries = setup.uninstall_libaries()
        action_string = "uninstalled"
    else:
        success, libraries = setup.install_libaries()
        action_string = "installed"
    _print_action_result(success, libraries, action_string)
