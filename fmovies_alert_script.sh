#!/bin/bash

# Path to the py venv
VENV_PATH="" # Put the absolute path of the py venv here 

# Activate venv
source "$VENV_PATH/bin/activate"

# Path to requirements.txt
REQUIREMENTS_FILE=""  # Put the absolute path of the requirements.txt here

# Install py package from requirements.txt
pip install -r "$REQUIREMENTS_FILE"

# Path to py script
PYTHON_SCRIPT="" # Put the absolute path of the py script here

# Run py script
python3 "$PYTHON_SCRIPT"

# Deactivate venv
deactivate
