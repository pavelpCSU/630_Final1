#!/bin/bash

# Create build directory if it doesn't exist
mkdir -p build

# Move to build directory and run cmake and make
cd build && \
cmake .. && \
make

# Check if build was successful
if [ $? -eq 0 ]; then
    echo -e "\nBuild successful! You can run the tests with:\n./build/run_tests"
else
    echo -e "\nBuild failed!"
    exit 1
fi