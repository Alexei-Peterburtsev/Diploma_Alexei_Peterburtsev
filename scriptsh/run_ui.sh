#!/bin/bash

SCRIPT_DIR=$(dirname "$0")

TEST_FILE_ONE="$SCRIPT_DIR/../tests/test_ui_footer.py"
TEST_FILE_TWO="$SCRIPT_DIR/../tests/test_ui_header.py"
TEST_FILE_THREE="$SCRIPT_DIR/../tests/test_ui_mainmenu.py"
TEST_FILE_FOUR="$SCRIPT_DIR/../tests/test_ui_mainmenu_itemcount.py"
TEST_FILE_FIVE="$SCRIPT_DIR/../tests/test_ui_mainpage_info.py"
TEST_FILE_SIX="$SCRIPT_DIR/../tests/test_ui_search.py"

REPORT_DIR="$SCRIPT_DIR/../tests/results"

pytest -v -s "$TEST_FILE_ONE" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_TWO" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_THREE" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_FOUR" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_FIVE" --alluredir="$REPORT_DIR"
pytest -v -s "$TEST_FILE_SIX" --alluredir="$REPORT_DIR"