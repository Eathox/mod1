#!/usr/bin/env python3
"""Install all library dependencies constants"""

from sys import argv

from setup import Manager

g_dependencies = [
	"numpy",
	"pyglet",
	"pyopengl",
]

g_suggestions = {
	"linux": "Consider runing: 'sudo apt install python3-pip' to install.",
	"darwin": "Consider runing: 'brew install python3' to install.",
	"win32": "Consider runing: 'python3 get-pip.py' to install.",
}

def _print_pip_not_installed(manager):
	if manager.platform in g_suggestions:
		suggestion = g_suggestions[manager.platform]
	else:
		suggestion = "Unrecognized kernel, unable to provide install suggestion."
	print(f"{manager.pip} is not installed.\n{suggestion}")
	print(f"For more info visit: https://pip.pypa.io/en/stable/installing/")
	exit()

def _print_action_result(success, libraries, action_str):
	"""print install or uninstall action results"""
	if success == False:
		print(f"Failed to {action_str} all dependencies")
	if libraries == [] and success == True:
		print(f"All dependencies allready {action_str}.")
	elif libraries != []:
		print(f"\nSuccessfully {action_str} the following:")
		for library in libraries:
			print(f" - {library.name}")

if __name__ == "__main__":
	"""Setup dependencies"""
	manager = Manager(argv[1:], *g_dependencies)
	if manager.pip_installed() == False:
		_print_pip_not_installed(manager)

	if "--uninstall" in manager.args or "--remove" in manager.args:
		success, libraries = manager.uninstall_libraries()
		action_str = "uninstalled"
	else:
		success, libraries = manager.install_libraries()
		action_str = "installed"
	_print_action_result(success, libraries, action_str)
