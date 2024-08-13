#!/bin/bash

# Path to your cash.py script
SCRIPT_PATH="/tmp/.cash/cash.py"

# Kill any existing instance of cash.py
pkill -f "$SCRIPT_PATH"

# Run the script
/usr/local/bin/python3.9 "$SCRIPT_PATH" &