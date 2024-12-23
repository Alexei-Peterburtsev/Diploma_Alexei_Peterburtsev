#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

TEST_FILE="$SCRIPT_DIR/../tests/test_search_input.py"

REPORT_DIR="$SCRIPT_DIR/../reports"

pytest -v -s "$TEST_FILE" --alluredir="$REPORT_DIR"