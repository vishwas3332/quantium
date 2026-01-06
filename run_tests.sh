#!/bin/bash

VENV_DIR="C:/VIRTUAL_ENV/universal_venv/Scripts/activate"

if [ -f "$VENV_DIR" ]; then
    source "$VENV_DIR"
    echo "Virtual environment activated."
else
    echo "Error: Virtual environment not found at $VENV_PATH"
fi

python -m pytest test.py

PYTEST_EXITCODE=$?

if [ $PYTEST_EXITCODE -eq 0 ]; then
    echo "Tests passed successfully."
    exit 0
else
    echo "Tests failed with exit code $TEST_EXIT_CODE."
    exit 1
fi
