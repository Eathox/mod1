#!/usr/bin/env python
"""Install all library dependencies constants"""

from sys import argv

from setup import libraries

g_dependencies = [
	"numpy",
	"pygame",
	"pyopengl",
]

g_suggestions = {
	"linux": "Consider runing: 'sudo apt install python3-pip' to install.",
	"darwin": "Consider runing: 'brew install python3' to install.",
	"win32": "Consider runing: 'python3 get-pip.py' to install.",
}

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
	setup = libraries.Setup(argv[1:], *g_dependencies)
	if setup.pip_installed() == False:
		if setup.platform in g_suggestions:
			suggestion = g_suggestions[setup.platform]
		else:
			suggestion = "Unrecognized kernel, unable to provide install suggestion."
		print(f"{setup.pip} is not installed.\n{suggestion}")
		print(f"For more info visit: https://pip.pypa.io/en/stable/installing/")
		exit()

	if "--uninstall" in setup.args or "--remove" in setup.args:
		success, libraries = setup.uninstall_libraries()
		action_str = "uninstalled"
	else:
		success, libraries = setup.install_libraries()
		action_str = "installed"
	_print_action_result(success, libraries, action_str)
