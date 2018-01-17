#!/bin/bash
# Install script for Secure Delete
# Run as root, UID = 0
if [ "$UID" -ne 0 ]; then
	printf "Error: Run as UID 0, use \"sudo $0\" to do this.\n";
	exit 13
fi
if [ ! -f "../code/secdel.py" ]; then
	printf "Secure Delete not found, did you move this script?\n";
	exit 1
fi
printf "DUDEX64 - Secure Delete\n";
printf "Copyright (C) 2017 Michael Miranda, all rights reserved.\n";
printf "\n"
printf "This program is licensed under the terms of the GNU General Public License V3,\n"
printf " or at your option, any later version.\n";

