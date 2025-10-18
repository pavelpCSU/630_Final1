#!/bin/bash
# Script to check for common Problem 4 harness issues

echo "Checking Problem 4 harness setup..."

# 1. Check Python solution files and function signature
for folder in Problem4-copilot-GPT-4.1-python Problem4-copilot-Claude-Sonnet-3.5-python; do
    if [ ! -f "$folder/solution.py" ]; then
        echo "❌ Missing $folder/solution.py"
    else
        if ! grep -q "def three_sum" "$folder/solution.py"; then
            echo "❌ $folder/solution.py does not define 'three_sum(nums)'"
        else
            echo "✅ $folder/solution.py found and has 'three_sum'"
        fi
    fi
done

# 2. Check C++ solution files
for folder in Problem4-copilot-GPT-4.1-C++ Problem4-copilot-Claude-Sonnet-3.5-C++; do
    if [ ! -f "$folder/solution.cpp" ]; then
        echo "❌ Missing $folder/solution.cpp"
    else
        echo "✅ $folder/solution.cpp found"
    fi
    if [ ! -f "$folder/build.sh" ]; then
        echo "❌ Missing $folder/build.sh"
    else
        echo "✅ $folder/build.sh found"
    fi
done

# 3. Check test case files
if [ ! -d "data/p4" ]; then
    echo "❌ Missing data/p4 directory"
else
    inputs=$(ls data/p4/input_*.json 2>/dev/null | wc -l)
    outputs=$(ls data/p4/output_*.json 2>/dev/null | wc -l)
    if [ "$inputs" -eq 0 ]; then
        echo "❌ No input_*.json files in data/p4"
    else
        echo "✅ Found $inputs input_*.json files in data/p4"
    fi
    if [ "$outputs" -eq 0 ]; then
        echo "❌ No output_*.json files in data/p4"
    else
        echo "✅ Found $outputs output_*.json files in data/p4"
    fi
fi

# 4. Check handler and validator functions in harness
if ! grep -q "def handler_three_sum" benchmark_rubric_harness.py; then
    echo "❌ Missing handler_three_sum in benchmark_rubric_harness.py"
else
    echo "✅ handler_three_sum found in benchmark_rubric_harness.py"
fi
if ! grep -q "def validator_three_sum" benchmark_rubric_harness.py; then
    echo "❌ Missing validator_three_sum in benchmark_rubric_harness.py"
else
    echo "✅ validator_three_sum found in benchmark_rubric_harness.py"
fi

echo "Check complete."