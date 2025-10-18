#!/bin/bash
mkdir -p build
g++ -O2 run_tests.cpp solution.cpp -o build/run_tests
