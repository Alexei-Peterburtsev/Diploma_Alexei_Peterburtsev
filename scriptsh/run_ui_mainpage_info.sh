#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

TEST_FILE="$SCRIPT_DIR/../tests/test_ui_mainpage_info.py"

REPORT_DIR="$SCRIPT_DIR/../tests/results"

pytest -v -s "$TEST_FILE" --alluredir="$REPORT_DIR"