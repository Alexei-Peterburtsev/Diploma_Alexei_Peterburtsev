#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

TEST_FILE_01="$SCRIPT_DIR/../tests/test_api_page.py"
TEST_FILE_02="$SCRIPT_DIR/../tests/test_api_search.py"
TEST_FILE_03="$SCRIPT_DIR/../tests/test_api_page_404.py"

REPORT_DIR="$SCRIPT_DIR/../tests/results"

pytest -v -s "$TEST_FILE_01" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_02" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_03" --alluredir="$REPORT_DIR"