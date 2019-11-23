#!/usr/bin/env python
"""Install all library dependencies constants"""

from sys import argv

from setup import libraries

dependencies = [
	"numpy",
	"pygame",
	"pyopengl",
]

def _print_action_result(success, libraries, action_str):
	"""print install or uninstall action results"""
	if success == False:
		print(f"Failed to {action_str} all dependencies")
	if libraries == [] and success == True:
		print(f"All dependencies allready {action_str}.")
	elif libraries != []:
		print(f"\nSuccessfully {action_str} the following:")
		for library in libraries:
			print(f" - {library}")

if __name__ == "__main__":
	"""Setup dependencies"""
	setup = libraries.Setup(argv[1:], *dependencies)
	if setup.pip_installed() == False:
		suggestion = "Unrecognized kernel, unable to provide install suggestion."
		if setup.platform == "linux":
			suggestion = "Consider runing: 'sudo apt install python3-pip' to install."
		elif setup.platform == "darwin":
			suggestion = "Consider runing: 'brew install python3' to install."
		elif setup.platform == "win32":
			suggestion = "Consider runing: 'python3 get-pip.py' to install."
		print(f"{setup.pip} is not installed.\n{suggestion}")
		exit()

	if "--uninstall" in setup.args or "--remove" in setup.args:
		success, libraries = setup.uninstall_libraries()
		action_str = "uninstalled"
	else:
		success, libraries = setup.install_libraries()
		action_str = "installed"
	_print_action_result(success, libraries, action_str)
