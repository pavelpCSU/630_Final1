from calculate_bigo import DEBUG
import subprocess
import json
import time
import statistics
import os
import sys
from decimal import Decimal, getcontext
import importlib.util
import glob


# Import optimizer reduction utilities
from optimizer_reduction import reduce_optimizations

# --- Optimizer Reduction Control Flags ---
# Set these to control optimizer reduction behavior globally
USE_OPTIMIZER_REDUCTION = True
OPTIMIZER_REDUCTION_LEVEL = 'medium'  # Options: 'off', 'low', 'medium', 'high', 'max'

# Map levels to parameters
OPTIMIZER_REDUCTION_PARAMS = {
    'off':    dict(warmup=0,  repeat=1,   randomize_args=False, restart_between_runs=False),
    'low':    dict(warmup=3,  repeat=10,  randomize_args=False, restart_between_runs=False),
    'medium': dict(warmup=7,  repeat=25,  randomize_args=True,  restart_between_runs=False),
    'high':   dict(warmup=15, repeat=50,  randomize_args=True,  restart_between_runs=False),
    'max':    dict(warmup=30, repeat=100, randomize_args=True,  restart_between_runs=True),
}

getcontext().prec = 28

def load_test_case(input_file, output_file):
    with open(input_file, 'r') as f:
        input_data = json.load(f)
    with open(output_file, 'r') as f:
        expected = json.load(f)
    return input_data, expected

def measure_execution_time(func, *args, iterations=10):
    import copy
    # Select optimizer reduction parameters
    level = OPTIMIZER_REDUCTION_LEVEL if USE_OPTIMIZER_REDUCTION else 'off'
    params = OPTIMIZER_REDUCTION_PARAMS.get(level, OPTIMIZER_REDUCTION_PARAMS['off'])
    warmup_runs = params['warmup']
    repeat_per_sample = params['repeat']
    randomize_args = params['randomize_args']
    restart_between_runs = params['restart_between_runs']
    times = []
    if USE_OPTIMIZER_REDUCTION and level != 'off':
        # Use the optimizer_reduction utility for timing
        def wrapped_func(*wrapped_args):
            test_args = [copy.deepcopy(arg) for arg in wrapped_args]
            func(*test_args)
        for _ in range(iterations):
            avg_time = reduce_optimizations(
                wrapped_func,
                args=args,
                repeat=repeat_per_sample,
                warmup=warmup_runs,
                randomize_args=randomize_args,
                restart_between_runs=restart_between_runs
            )
            # Convert seconds to nanoseconds for compatibility
            times.append(Decimal(avg_time) * Decimal(1e9))
    else:
        # Original timing logic
        # Warm-up phase
        for _ in range(warmup_runs):
            test_args = [copy.deepcopy(arg) for arg in args]
            func(*test_args)
        # Timing phase
        for _ in range(iterations):
            test_args = [copy.deepcopy(arg) for arg in args]
            start = time.perf_counter_ns()
            for _ in range(repeat_per_sample):
                func(*test_args)
            end = time.perf_counter_ns()
            times.append(Decimal(end - start) / Decimal(repeat_per_sample))
    return {
        'min': min(times),
        'max': max(times),
        'avg': sum(times) / Decimal(len(times)),
        'med': statistics.median(times),
        'std': Decimal(statistics.stdev(times)) if len(times) > 1 else Decimal('0'),
        'repeat': repeat_per_sample
    }

def print_stats_table(results, big_o=None):
    print("\nComplexity Analysis Table (all times in nanoseconds, ns):")
    print("Note: 'Expected Ratio' is the ratio of input sizes between consecutive tests (unitless)")
    if results and 'repeat' in results[0]['timing']:
        print(f"Each timing sample is averaged over {{results[0]['timing']['repeat']}} repetitions per test run.")
    if big_o:
        print(f"Big O Analysis (Expected): {big_o}")
    print(f"{'Input Size':>12} | {'Med (ns)':>12} | {'Min (ns)':>12} | {'Max (ns)':>12} | {'Avg (ns)':>12} | {'Std (ns)':>12} | {'Time/n (ns)':>14} | {'Actual Ratio':>12} | {'Expected Ratio':>15} | {'Big O':>10} | {'Real. Big O':>15}")
    print("-" * 155)
    # Empirical Big O calculation using actual test run data
    try:
        from calculate_bigo import empirical_bigo_from_data, EmpiricalBigOResult
        from analyze_bigo import analyze_bigo_discrepancy
        sizes = [r['size'] for r in results]
        times = [float(r['timing']['med']) for r in results]
        empirical_result = empirical_bigo_from_data(sizes, times)
        if isinstance(empirical_result, EmpiricalBigOResult):
            real_bigo = empirical_result.best_class
            confidence = empirical_result.confidence()
            warning = empirical_result.warning
        else:
            real_bigo = empirical_result
            confidence = None
            warning = None
        if DEBUG:
            print(f"[DEBUG] Theoretical Big O: {big_o}, Empirical Big O: {real_bigo}, Confidence: {confidence}, Warning: {warning}")
    except Exception as e:
        real_bigo = 'n/a'
        confidence = None
        warning = str(e)
    for i in range(len(results)):
        size = results[i]['size']
        timing = results[i]['timing']
        med_time = timing['med']
        min_time = timing['min']
        max_time = timing['max']
        avg_time = timing['avg']
        std_time = timing['std']
        time_per_n = med_time / size if size else Decimal(0)
        if i > 0:
            prev_size = results[i-1]['size']
            prev_med = results[i-1]['timing']['med']
            if prev_med == 0:
                actual_ratio = "n/a"
            else:
                actual_ratio = f"{med_time / prev_med:>.2f}"
            expected_ratio = f"{size / prev_size:>.2f}"
        else:
            actual_ratio = "n/a"
            expected_ratio = "n/a"
        print(f"{size:>12,} | {med_time:>12.2f} | {min_time:>12.2f} | {max_time:>12.2f} | {avg_time:>12.2f} | {std_time:>12.2f} | {time_per_n:>14.6f} | {actual_ratio:>12} | {expected_ratio:>15} | {big_o if big_o else '':>10} | {real_bigo:>15}")
    # After table, explain discrepancy if any
    try:
        if big_o and real_bigo and big_o != real_bigo:
            context = {'sizes': sizes, 'times': times}
            explanation = analyze_bigo_discrepancy(big_o, real_bigo, context)
            print("\n[Big O Discrepancy Analysis]\n" + explanation + "\n")
        if warning:
            print(f"[Empirical Big O Warning] {warning}")
        if confidence is not None:
            print(f"[Empirical Big O Confidence] {confidence:.2f}")
    except Exception as e:
        print(f"[Big O Discrepancy Analysis] Could not analyze discrepancy: {e}")
    # After table, explain discrepancy if any
    try:
        if big_o and real_bigo and big_o != real_bigo:
            context = {'sizes': sizes, 'times': times}
            explanation = analyze_bigo_discrepancy(big_o, real_bigo, context)
            print("\n[Big O Discrepancy Analysis]\n" + explanation + "\n")
    except Exception as e:
        print(f"[Big O Discrepancy Analysis] Could not analyze discrepancy: {e}")

def import_solution(folder_name):
    import importlib.util
    import os
    solution_path = os.path.join(os.path.dirname(__file__), folder_name, "solution.py")
    spec = importlib.util.spec_from_file_location("solution", solution_path)
    solution = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution)
    return solution

def handler_two_sum(input_data, expected):
    # If expected is a dict with 'indices', extract the list
    if isinstance(expected, dict) and 'indices' in expected:
        expected_val = expected['indices']
    else:
        expected_val = expected
    return (input_data['nums'], input_data['target']), expected_val

def handler_group_anagrams(input_data, expected):
    # If expected is a dict with 'groups', extract the list
    if isinstance(expected, dict) and 'groups' in expected:
        expected_val = expected['groups']
    else:
        expected_val = expected
    return (input_data['strs'],), expected_val

def handler_median(input_data, expected):
    return (input_data['nums1'], input_data['nums2']), expected['median'] if isinstance(expected, dict) and 'median' in expected else expected

def handler_three_sum(input_data, expected):
    nums = input_data['nums']
    # expected can be a dict or a list
    if isinstance(expected, dict) and 'triplets' in expected:
        expected_val = expected['triplets']
    else:
        expected_val = expected
    return (nums,), expected_val

def main(solution_func, test_cases, iterations=10, input_handler=None, validator=None):
    results = []
    for i, (input_file, output_file) in enumerate(test_cases, 1):
        input_data, expected = load_test_case(input_file, output_file)
        if input_handler:
            args, expected_result = input_handler(input_data, expected)
        else:
            args = (input_data['nums'], input_data['target'])
            expected_result = expected
        print(f"\nTest {i}: Input size = {len(args[0]):,}")
        try:
            timing = measure_execution_time(lambda *a: solution_func(*a), *args, iterations=iterations)
            result = solution_func(*args)
            # Use validator if provided, else default to True
            if validator:
                valid = validator(result, expected_result, args)
            else:
                valid = True
            if valid:
                print("  Result: PASS")
            else:
                print(f"  Result: FAIL")
        except Exception as e:
            import traceback
            print(f"  Result: FAIL (Exception: {e})")
            traceback.print_exc()
            timing = {'min': Decimal(0), 'max': Decimal(0), 'avg': Decimal(0), 'med': Decimal(0), 'std': Decimal(0), 'repeat': 1}
        print(f"  Min: {timing['min']:.2f} ns")
        print(f"  Max: {timing['max']:.2f} ns")
        print(f"  Avg: {timing['avg']:.2f} ns")
        print(f"  Med: {timing['med']:.2f} ns")
        print(f"  Std: {timing['std']:.2f} ns")
        print(f"  (Each timing sample is averaged over {timing['repeat']} repetitions)")
        results.append({'size': len(args[0]), 'timing': timing})
    # Pass the big_o value if available
    big_o = None
    if hasattr(main, 'big_o'):
        big_o = main.big_o
    print_stats_table(results, big_o=big_o)
    print(f"\nPython version: {sys.version}")
    print(f"Platform: {sys.platform}")

def validator_two_sum(result, expected, args):
    nums, target = args
    return (
        isinstance(result, list)
        and len(result) == 2
        and 0 <= result[0] < len(nums)
        and 0 <= result[1] < len(nums)
        and result[0] != result[1]
        and nums[result[0]] + nums[result[1]] == target
    )

def validator_group_anagrams(result, expected, args):
    # Compare groups as sets of frozensets for order-insensitive match
    result_groups = [set(group) for group in result]
    expected_groups = [set(group) for group in expected]
    return sorted([frozenset(g) for g in result_groups]) == sorted([frozenset(g) for g in expected_groups])

def validator_median(result, expected, args):
    return abs(result - expected) < 1e-6

def validator_three_sum(result, expected, args):
    # Compare as sets of sorted tuples for order-insensitive match
    result_set = {tuple(sorted(triplet)) for triplet in result}
    expected_set = {tuple(sorted(triplet)) for triplet in expected}
    return result_set == expected_set

def get_test_cases(pattern_in, pattern_out):
    inputs = sorted(glob.glob(pattern_in))
    outputs = sorted(glob.glob(pattern_out))
    pairs = []
    for inp in inputs:
        base = inp.rsplit('.', 1)[0].rsplit('_', 1)[-1]
        out = None
        for o in outputs:
            if o.rsplit('.', 1)[0].endswith(base):
                out = o
                break
        if out:
            pairs.append((inp, out))
    return pairs
import glob
import sys

# Set data_folder before using it in problems list
data_folder = 'data'
if len(sys.argv) > 1 and sys.argv[1] == 'data2':
    data_folder = 'data2'

def get_test_cases(pattern_in, pattern_out):
    inputs = sorted(glob.glob(pattern_in))
    outputs = sorted(glob.glob(pattern_out))
    pairs = []
    for inp in inputs:
        base = inp.rsplit('.', 1)[0].rsplit('_', 1)[-1]
        out = None
        for o in outputs:
            if o.rsplit('.', 1)[0].endswith(base):
                out = o
                break
        if out:
            pairs.append((inp, out))
    return pairs

problems = [
    {
        'name': 'Problem 1: Two Sum',
        'python_folders': [
            'Problem1-copilot-GPT-4.1-python',
            'Problem1-copilot-Claude-Sonnet-3.5-python',
        ],
        'cpp_folders': [],
        'function': 'two_sum',
        'test_cases': get_test_cases(f"{data_folder}/p1/generated/input_gen_*.json", f"{data_folder}/p1/generated/output_gen_*.json"),
        'input_handler': handler_two_sum,
        'validator': validator_two_sum,
        'big_o': 'O(n)',
    },
    {
        'name': 'Problem 2: Group Anagrams',
        'python_folders': [
            'Problem2-copilot-GPT-4.1-python',
            'Problem2-copilot-Claude-Sonnet-3.5-python',
        ],
        'cpp_folders': [],
        'function': 'group_anagrams',
        'test_cases': get_test_cases(f"{data_folder}/p2/input_*.json", f"{data_folder}/p2/output_*.json"),
        'input_handler': handler_group_anagrams,
        'validator': validator_group_anagrams,
        'big_o': 'O(nk)',
    },
    {
        'name': 'Problem 3: Median of Two Sorted Arrays',
        'python_folders': [
            'Problem3-copilot-GPT-4.1-python',
            'Problem3-copilot-Claude-Sonnet-3.5-python',
        ],
        'cpp_folders': [
            'Problem3-copilot-GPT-4.1-C++',
            'Problem3-copilot-Claude-Sonnet-3.5-C++',
        ],
        'function': 'find_median_sorted_arrays',
        'test_cases': get_test_cases(f"{data_folder}/p3/input_*.json", f"{data_folder}/p3/output_*.json"),
        'input_handler': handler_median,
        'validator': validator_median,
        'big_o': 'O(log(min(n, m)))',
    },
    {
        'name': 'Problem 4: 3-Sum (Zero-Sum Triplets)',
        'python_folders': [
            'Problem4-copilot-GPT-4.1-python',
            'Problem4-copilot-Claude-Sonnet-3.5-python',
        ],
        'cpp_folders': [
            'Problem4-copilot-GPT-4.1-C++',
            'Problem4-copilot-Claude-Sonnet-3.5-C++',
        ],
        'function': 'three_sum',
        'test_cases': get_test_cases(f"{data_folder}/p4/input_*.json", f"{data_folder}/p4/output_*.json"),
        'input_handler': handler_three_sum,
        'validator': validator_three_sum,
        'big_o': 'O(n^2)',
    },
]
for problem in problems:
    print(f"\n=== {problem['name']} ===")
    # Python solutions
    for folder in problem.get('python_folders', []):
        print(f"\n--- {folder} (Python) ---")
        solution = import_solution(folder)
        func = None
        func_name = problem['function']
        alt_func_name = None
        if func_name == 'find_median_sorted_arrays':
            alt_func_name = 'findMedianSortedArrays'
        try:
            func = getattr(solution, func_name)
        except AttributeError:
            if alt_func_name and hasattr(solution, alt_func_name):
                func = getattr(solution, alt_func_name)
            else:
                raise
        main.big_o = problem.get('big_o', None)
        main(func, problem['test_cases'], iterations=10, input_handler=problem.get('input_handler'), validator=problem.get('validator'))
    # C++ solutions
    for cpp_folder in problem.get('cpp_folders', []):
        print(f"\n--- {cpp_folder} (C++) ---")
        build_sh = 'build.sh'  # Use relative path for subprocess with cwd
        run_tests_bin = os.path.join(cpp_folder, 'build', 'run_tests')



        def try_build():
            print(f"Building {cpp_folder}...")
            result = subprocess.run(['bash', './build.sh'], capture_output=True, text=True, cwd=cpp_folder)
            print(result.stdout)
            print(result.stderr)
            if result.returncode != 0:
                print(f"\n[ERROR] Build failed for {cpp_folder}.")
                print(f"\n[HINT] Please check your build script and environment. Try running:\n  cd {cpp_folder}\n  bash build.sh\n")
                return False
            return True

        def is_stale(binary, sources):
            if not os.path.exists(binary):
                return True
            bin_mtime = os.path.getmtime(binary)
            for src in sources:
                if os.path.exists(src) and os.path.getmtime(src) > bin_mtime:
                    return True
            return False

        # Check if binary is missing or stale (older than source/build.sh)
        sources = [os.path.join(cpp_folder, 'run_tests.cpp'), os.path.join(cpp_folder, 'build.sh')]
        if is_stale(run_tests_bin, sources):
            print(f"[INFO] Binary is missing or stale. Rebuilding...")
            if not try_build():
                continue
            if is_stale(run_tests_bin, sources):
                print(f"[ERROR] Test binary still missing or stale after build. Aborting.")
                continue

        # Run the test binary and capture output
        print(f"Running C++ tests for {cpp_folder}...")
        result = subprocess.run([run_tests_bin], capture_output=True, text=True)
        output = result.stdout
        if result.returncode != 0:
            print(f"C++ tests for {cpp_folder} failed with return code {result.returncode}")
            print(output)
            continue
        # Parse C++ output for test results
        import re
        test_results = []
        lines = output.splitlines()
        size_re = re.compile(r"Input sizes: (\d+) and (\d+)")
        min_re = re.compile(r"Min: ([0-9.eE+-]+) ns")
        max_re = re.compile(r"Max: ([0-9.eE+-]+) ns")
        avg_re = re.compile(r"Avg: ([0-9.eE+-]+) ns")
        med_re = re.compile(r"Med: ([0-9.eE+-]+) ns")
        std_re = re.compile(r"Std: ([0-9.eE+-]+) ns")
        pass_re = re.compile(r"PASS|PASSED|✅")
        fail_re = re.compile(r"FAIL|❌")
        i = 0
        while i < len(lines):
            if lines[i].startswith("Running Test"):
                # Find input size
                size = None
                m = size_re.search(lines[i+1]) if i+1 < len(lines) else None
                if m:
                    size = int(m.group(1)) + int(m.group(2))
                # Find timing lines
                min_ns = max_ns = avg_ns = med_ns = std_ns = None
                for j in range(i+2, min(i+10, len(lines))):
                    if min_ns is None:
                        m = min_re.search(lines[j])
                        if m: min_ns = float(m.group(1))
                    if max_ns is None:
                        m = max_re.search(lines[j])
                        if m: max_ns = float(m.group(1))
                    if avg_ns is None:
                        m = avg_re.search(lines[j])
                        if m: avg_ns = float(m.group(1))
                    if med_ns is None:
                        m = med_re.search(lines[j])
                        if m: med_ns = float(m.group(1))
                    if std_ns is None:
                        m = std_re.search(lines[j])
                        if m: std_ns = float(m.group(1))
                # Find PASS/FAIL
                status = None
                for j in range(i+2, min(i+10, len(lines))):
                    if pass_re.search(lines[j]):
                        status = 'PASS'
                    if fail_re.search(lines[j]):
                        status = 'FAIL'
                if size and med_ns is not None:
                    test_results.append({
                        'size': size,
                        'timing': {
                            'min': min_ns or 0,
                            'max': max_ns or 0,
                            'avg': avg_ns or 0,
                            'med': med_ns or 0,
                            'std': std_ns or 0,
                        },
                        'status': status or 'UNKNOWN',
                    })
            i += 1
        # Print summary table in Python style
        print_stats_table(test_results, big_o=problem.get('big_o'))
        # Print PASS/FAIL for each test
        for idx, res in enumerate(test_results, 1):
            print(f"Test {idx}: {res['status']}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--problem', type=int, help='Run only the specified problem number (1-based)')
    args = parser.parse_args()
    run_all_problems(selected_problem=args.problem if args.problem else None)