#!/bin/bash
# Script to execute all Problem 4 solutions (Python and C++)

echo "Running Problem 4 Python solutions..."
for folder in Problem4-copilot-GPT-4.1-python Problem4-copilot-Claude-Sonnet-3.5-python; do
    if [ -f "$folder/solution.py" ]; then
        echo "Executing $folder/solution.py"
        python3 "$folder/solution.py"
    else
        echo "❌ $folder/solution.py not found."
    fi
done

echo ""
echo "Building and running Problem 4 C++ solutions..."
for folder in Problem4-copilot-GPT-4.1-C++ Problem4-copilot-Claude-Sonnet-3.5-C++; do
    if [ -f "$folder/build.sh" ]; then
        echo "Building $folder..."
        bash "$folder/build.sh"
        if [ -f "$folder/build/run_tests" ]; then
            echo "Executing $folder/build/run_tests"
            "$folder/build/run_tests"
        else
            echo "❌ $folder/build/run_tests not found after build."
        fi
    else
        echo "❌ $folder/build.sh not found."
    fi
done