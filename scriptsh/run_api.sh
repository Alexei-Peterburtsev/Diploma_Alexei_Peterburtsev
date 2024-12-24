#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

TEST_FILE_ONE="$SCRIPT_DIR/../tests/test_api_page.py"
TEST_FILE_TWO="$SCRIPT_DIR/../tests/test_api_search.py"

REPORT_DIR="$SCRIPT_DIR/../tests/results"

pytest -v -s "$TEST_FILE_ONE" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_TWO" --alluredir="$REPORT_DIR"