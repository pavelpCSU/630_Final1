def wrapped_two_sum(nums, target):
def measure_execution_time(nums, target, iterations=10):
if __name__ == "__main__":
    import os
    import sys
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if workspace_root not in sys.path:
        sys.path.insert(0, workspace_root)
    from benchmark_rubric_harness import run_all_problems
    run_all_problems()
        
        # Force fresh memory allocation
        test_data = nums.copy()
        
        start = time.perf_counter_ns()
        result = wrapped_two_sum(test_data, target)
        end = time.perf_counter_ns()
        
        # Convert nanoseconds to microseconds using Decimal
        times.append(Decimal(end - start) / Decimal('1000'))
        
        # Verify result
        if len(result) == 2:
            assert test_data[result[0]] + test_data[result[1]] == target
            assert result[0] != result[1]
    
    return {
        'min': min(times),
        'max': max(times),
        'avg': sum(times) / Decimal(len(times)),
        'med': statistics.median(times),
        'std': Decimal(statistics.stdev(times)) if len(times) > 1 else Decimal('0')
    }

def main():
    test_cases = [
        ('data/p1/generated/input_gen_1.json', 'data/p1/generated/output_gen_1.json'),
        ('data/p1/generated/input_gen_2.json', 'data/p1/generated/output_gen_2.json'),
        ('data/p1/generated/input_gen_3.json', 'data/p1/generated/output_gen_3.json'),
        ('data/p1/generated/input_gen_4.json', 'data/p1/generated/output_gen_4.json')
    ]
    success_count = 0
    fail_count = 0
    print("\nTesting your two_sum implementation:")
    for i, (input_file, output_file) in enumerate(test_cases, 1):
        print(f"\nRunning Test {i}...")
        input_data, expected = load_test_case(input_file, output_file)
        nums, target = input_data['nums'], input_data['target']
        result = solution.two_sum(nums, target)
        valid = (
            isinstance(result, list)
            and len(result) == 2
            and 0 <= result[0] < len(nums)
            and 0 <= result[1] < len(nums)
            and result[0] != result[1]
            and nums[result[0]] + nums[result[1]] == target
        )
        if valid:
            print(f"Test {i}: PASS")
            success_count += 1
        else:
            print(f"Test {i}: FAIL. Got {result}, expected indices summing to {target}")
            fail_count += 1
    print(f"\nSummary: {success_count} passed, {fail_count} failed out of {len(test_cases)} tests.")
    print("\n--- End of two_sum tests ---\n")
    
    print("Detailed Performance Analysis (StringNumber Version)")
    print("-" * 80)
    print("Using wrapped numbers with expensive string operations")
    print("Each number wrapped in a class with string representation")
    
    results = []
    
    for i, (input_file, output_file) in enumerate(test_cases, 1):
        print(f"\nRunning Test {i}...")
        
        input_data, expected = load_test_case(input_file, output_file)
        nums, target = input_data['nums'], input_data['target']
        
        print(f"Input size: {len(nums):,} elements")
        
        timing = measure_execution_time(nums, target)
        results.append({
            'size': len(nums),
            'timing': timing
        })
        
    print(f"Execution times over 10 iterations (wrapped numbers, all in microseconds, μs):")
    print(f"  Min: {timing['min']:.2f} μs")
    print(f"  Max: {timing['max']:.2f} μs")
    print(f"  Avg: {timing['avg']:.2f} μs")
    print(f"  Med: {timing['med']:.2f} μs")
    print(f"  Std: {timing['std']:.2f} μs")
        
    print("\nComplexity Analysis (all times in microseconds, μs):")
    print("Note: 'Expected Ratio' is the ratio of input sizes between consecutive tests (unitless), not a timing value.")
    print(f"{'Size':>12} | {'Med (μs)':>12} | {'Min (μs)':>12} | {'Max (μs)':>12} | {'Avg (μs)':>12} | {'Std (μs)':>12} | {'Time/n (μs)':>14} | {'Actual Ratio':>12} | {'Expected Ratio':>15}")
    print("-" * 120)
    for i in range(len(results)):
        size = results[i]['size']
        timing = results[i]['timing']
        med_time = timing['med']
        min_time = timing['min']
        max_time = timing['max']
        avg_time = timing['avg']
        std_time = timing['std']
        time_per_n = med_time / size
        if i > 0:
            prev_size = results[i-1]['size']
            prev_med = results[i-1]['timing']['med']
            actual_ratio = med_time / prev_med
            expected_ratio = size / prev_size
            ratio_str = f"{actual_ratio:>.2f}"
            expected_str = f"{expected_ratio:>.2f}"
        else:
            ratio_str = "n/a"
            expected_str = "n/a"
        print(f"{size:>12,} | {med_time:>12.2f} | {min_time:>12.2f} | {max_time:>12.2f} | {avg_time:>12.2f} | {std_time:>12.2f} | {time_per_n:>14.6f} | {ratio_str:>12} | {expected_str:>15}")

if __name__ == "__main__":
    main()