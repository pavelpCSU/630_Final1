#!/bin/bash
# Consolidated Problem 4 fix script for Ubuntu dev container

echo "=== Problem 4 Harness Fix Script ==="

# 1. Add build.sh to C++ solution folders if missing
for folder in Problem4-copilot-GPT-4.1-C++ Problem4-copilot-Claude-Sonnet-3.5-C++; do
    build_sh="$folder/build.sh"
    if [ ! -f "$build_sh" ]; then
        echo "Creating $build_sh..."
        cat > "$build_sh" <<EOF
#!/bin/bash
mkdir -p build
g++ -O2 run_tests.cpp solution.cpp -o build/run_tests
EOF
        chmod +x "$build_sh"
        echo "✅ $build_sh created and made executable."
    else
        echo "✅ $build_sh already exists."
    fi
done

# 2. Add sample test case files to data/p4 if missing
mkdir -p data/p4

if [ ! -f data/p4/input_01.json ]; then
    echo '{"nums": [-1, 0, 1, 2, -1, -4]}' > data/p4/input_01.json
    echo "[[-1, -1, 2], [-1, 0, 1]]" > data/p4/output_01.json
    echo "✅ Added data/p4/input_01.json and output_01.json"
else
    echo "✅ data/p4/input_01.json already exists."
fi

if [ ! -f data/p4/input_02.json ]; then
    echo '{"nums": [0, 0, 0]}' > data/p4/input_02.json
    echo "[[0, 0, 0]]" > data/p4/output_02.json
    echo "✅ Added data/p4/input_02.json and output_02.json"
else
    echo "✅ data/p4/input_02.json already exists."
fi

# 3. Check handler and validator functions in harness
for func in handler_three_sum validator_three_sum; do
    if grep -q "def $func" benchmark_rubric_harness.py; then
        echo "✅ $func found in benchmark_rubric_harness.py"
    else
        echo "❌ $func missing in benchmark_rubric_harness.py"
    fi
done

echo "=== Problem 4 Fixes Complete ==="