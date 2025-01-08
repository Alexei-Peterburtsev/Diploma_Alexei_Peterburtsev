#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

TEST_FILE_01="$SCRIPT_DIR/../tests/test_ui_footer.py"
TEST_FILE_02="$SCRIPT_DIR/../tests/test_ui_header.py"
TEST_FILE_03="$SCRIPT_DIR/../tests/test_ui_mainmenu.py"
TEST_FILE_04="$SCRIPT_DIR/../tests/test_ui_mainpage_info.py"
TEST_FILE_05="$SCRIPT_DIR/../tests/test_ui_search.py"
TEST_FILE_06="$SCRIPT_DIR/../tests/test_ui_management.py"

REPORT_DIR="$SCRIPT_DIR/../tests/results"

pytest -v -s "$TEST_FILE_01" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_02" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_03" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_04" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_05" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_06" --alluredir="$REPORT_DIR"