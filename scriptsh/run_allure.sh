#!/bin/bash

DIR=$(dirname "$0")

RESULTS="$DIR/../tests/results"

allure serve "$RESULTS"