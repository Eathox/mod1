#!/usr/bin/bash

function check_installed {
	return $(python3 -c "import $1" &>/dev/null)
}

echo $(check_installed numpy)
