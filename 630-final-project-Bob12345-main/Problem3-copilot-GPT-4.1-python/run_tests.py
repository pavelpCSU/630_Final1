def load_test_case(input_file, output_file):
import os
import sys

if __name__ == "__main__":
    import os
    import sys
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if workspace_root not in sys.path:
        sys.path.insert(0, workspace_root)
    from benchmark_rubric_harness import run_all_problems
    run_all_problems()
        self.str_val = f"num_{num:012d}"
    
    def __eq__(self, other):
        # Make comparison more expensive
        return self.str_val == other.str_val
    
    def __hash__(self):
        # Make hashing more expensive
        return hash(self.str_val)

def create_memory_pressure():
    """Create memory pressure to force cache misses"""
    garbage = []
    for _ in range(10):
        # Create string objects to consume memory
        chunk = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=20)) 
                for _ in range(100_000)]
        garbage.append(chunk)
        # Touch random locations
        for _ in range(1000):
            idx = random.randint(0, len(chunk)-1)
            _ = chunk[idx]
    garbage.clear()

def wrapped_two_sum(nums, target):
    """Two sum implementation using StringNumber objects"""
    # Convert numbers to StringNumber objects
    wrapped_nums = [StringNumber(x) for x in nums]
    target_wrapped = StringNumber(target)
    
    seen = {}
    for i, num in enumerate(wrapped_nums):
        complement_val = target - num.num  # Have to use raw numbers for arithmetic
        complement = StringNumber(complement_val)
        
        if complement.str_val in seen:
            return [seen[complement.str_val], i]
            
        seen[num.str_val] = i
    
    return []

def measure_execution_time(nums, target, iterations=10):
    times = []
    
    for _ in range(iterations):
        gc.collect()
        create_memory_pressure()
        
        # Force fresh memory allocation
        test_data = nums.copy()
        
        start = time.perf_counter_ns()
        result = wrapped_two_sum(test_data, target)
        end = time.perf_counter_ns()
        
        times.append((end - start) / 1e9)
        
        # Verify result
        if len(result) == 2:
            assert test_data[result[0]] + test_data[result[1]] == target
            assert result[0] != result[1]
    
    return {
        'min': min(times),
        'max': max(times),
        'avg': statistics.mean(times),
        'med': statistics.median(times),
        'std': statistics.stdev(times)
    }

def main():
    test_cases = [
        ('data/p3/input_1.json', 'data/p3/output_1.json'),
        ('data/p3/input_2.json', 'data/p3/output_2.json'),
        ('data/p3/input_3.json', 'data/p3/output_3.json')
    ]

    print("Detailed Performance Analysis (Median of Two Sorted Arrays)")
    print("-" * 80)
    results = []
    pass_count = 0
    fail_count = 0
    for i, (input_file, output_file) in enumerate(test_cases, 1):
        print(f"\nRunning Test {i}...")
        input_data, expected = load_test_case(input_file, output_file)
        nums1, nums2 = input_data['nums1'], input_data['nums2']
        expected_median = expected['median']
        print(f"Input sizes: {len(nums1):,} and {len(nums2):,} elements")
        times = []
        for _ in range(10):
            gc.collect()
            test1, test2 = nums1.copy(), nums2.copy()
            start = time.perf_counter_ns()
            result = solution.find_median_sorted_arrays(test1, test2)
            end = time.perf_counter_ns()
            times.append((end - start) / 1e9)
        passed = abs(result - expected_median) < 1e-6
        if passed:
            print(f"Test {i}: PASS")
            pass_count += 1
        else:
            print(f"Test {i}: FAIL. Got {result}, expected {expected_median}")
            fail_count += 1
        timing = {
            'min': min(times),
            'max': max(times),
            'avg': statistics.mean(times),
            'med': statistics.median(times),
            'std': statistics.stdev(times) if len(times) > 1 else 0.0
        }
        print(f"Execution times over 10 iterations:")
        print(f"  Min: {timing['min']:.6f}s")
        print(f"  Max: {timing['max']:.6f}s")
        print(f"  Avg: {timing['avg']:.6f}s")
        print(f"  Med: {timing['med']:.6f}s")
        print(f"  Std: {timing['std']:.6f}s")
        results.append({'size': len(nums1) + len(nums2), 'timing': timing})

    print(f"\nSummary: {pass_count} passed, {fail_count} failed out of {len(test_cases)} tests.")
    print("\nComplexity Analysis:")
    print(f"{'Size':>12} | {'Med Time':>10} | {'Time/n':>10} | {'Ratio':>10} | {'Expected':>10}")
    print("-" * 60)
    for i in range(len(results)):
        size = results[i]['size']
        med_time = results[i]['timing']['med']
        time_per_n = med_time / size
        if i > 0:
            prev_size = results[i-1]['size']
            prev_time = results[i-1]['timing']['med']
            actual_ratio = med_time / prev_time
            expected_ratio = size / prev_size
            ratio_str = f"{actual_ratio:>.2f}"
            expected_str = f"{expected_ratio:>.2f}"
        else:
            ratio_str = "n/a"
            expected_str = "n/a"
        print(f"{size:>12,} | {med_time:>10.6f} | {time_per_n:>10.8f} | {ratio_str:>10} | {expected_str:>10}")
if __name__ == "__main__":
    main()