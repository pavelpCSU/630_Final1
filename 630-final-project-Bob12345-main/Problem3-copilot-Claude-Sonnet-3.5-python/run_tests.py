def load_test_case(input_file, output_file):
def run_test(nums1, nums2, test_num=1, test_type=""):
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
    
    # Calculate timing statistics
    timing = {
        'min': min(times),
        'max': max(times),
        'avg': statistics.mean(times),
        'med': statistics.median(times),
        'std': statistics.stdev(times) if len(times) > 1 else 0.0
    }
    
    print(f"Execution times over {iterations} iterations:")
    print(f"  Min: {timing['min']:.6f}s")
    print(f"  Max: {timing['max']:.6f}s")
    print(f"  Avg: {timing['avg']:.6f}s")
    print(f"  Med: {timing['med']:.6f}s")
    print(f"  Std: {timing['std']:.6f}s")
    
    return result, timing, total_size

def generate_test_case(size1, size2, case_type="random"):
    """Generate a test case with specific characteristics"""
    if case_type == "random":
        nums1 = sorted(random.randint(-1000000, 1000000) for _ in range(size1))
        nums2 = sorted(random.randint(-1000000, 1000000) for _ in range(size2))
    elif case_type == "interleaved":
        combined = list(range(0, (size1 + size2) * 2, 2))
        nums1 = sorted(combined[:size1])
        nums2 = sorted(combined[size1:size1+size2])
    elif case_type == "disjoint":
        nums1 = sorted(random.randint(-1000000, 0) for _ in range(size1))
        nums2 = sorted(random.randint(1, 1000000) for _ in range(size2))
    else:  # identical
        nums = sorted(random.sample(range(-1000000, 1000000), size1))
        nums1 = nums.copy()
        nums2 = nums[:size2]
    
    # Calculate true median
    merged = sorted(nums1 + nums2)
    total_len = len(merged)
    if total_len % 2 == 0:
        median = (merged[total_len//2 - 1] + merged[total_len//2]) / 2
    else:
        median = float(merged[total_len//2])
    
    return nums1, nums2, {"median": median}

def main():
    print("Detailed Performance Analysis (Median of Two Sorted Arrays)")
    print("-" * 80)

    results = []
    pass_count = 0
    fail_count = 0

    # File-based tests
    print("\nFile-Based Tests:")
    print("-" * 80)
    
    test_cases = [
        ('data/p3/input_1.json', 'data/p3/output_1.json'),
        ('data/p3/input_2.json', 'data/p3/output_2.json'),
        ('data/p3/input_3.json', 'data/p3/output_3.json')
    ]
    
    for i, (input_file, output_file) in enumerate(test_cases, 1):
        input_data, expected = load_test_case(input_file, output_file)
        nums1, nums2 = input_data['nums1'], input_data['nums2']
        expected_median = expected['median']
        
        result, timing, total_size = run_test(nums1, nums2, i, "file")
        passed = abs(result - expected_median) < 1e-6
        
        if passed:
            print(f"Test {i}: PASS")
            pass_count += 1
        else:
            print(f"Test {i}: FAIL")
            print(f"Got {result}, expected {expected_median}")
            fail_count += 1
            
        results.append({
            'size': total_size,
            'timing': timing,
            'passed': passed
        })
    
    print("\nGenerated Tests:")
    print("-" * 80)
    
    generated_cases = [
        # Powers of 10 progression for complexity analysis
        (50000, 50000, "random"),    # 100K total
        (100000, 100000, "random"),  # 200K total
        (200000, 200000, "random"),  # 400K total
        (400000, 400000, "random"),  # 800K total
        (800000, 800000, "random")   # 1.6M total
    ]
    
    test_num = len(test_cases) + 1
    
    for size1, size2, case_type in generated_cases:
        nums1, nums2, expected = generate_test_case(size1, size2, case_type)
        result, timing, total_size = run_test(nums1, nums2, test_num, case_type)
        passed = abs(result - expected['median']) < 1e-6
        
        if passed:
            print(f"Test {test_num}: PASS")
            pass_count += 1
        else:
            print(f"Test {test_num}: FAIL")
            print(f"Got {result}, expected {expected['median']}")
            fail_count += 1
            
        results.append({
            'size': total_size,
            'timing': timing,
            'passed': passed
        })
        test_num += 1

    # Print complexity analysis
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
            expected_ratio = size / prev_size  # For O(log(m+n)), use log2 ratio
            ratio_str = f"{actual_ratio:>.2f}"
            expected_str = f"{expected_ratio:>.2f}"
        else:
            ratio_str = "n/a"
            expected_str = "n/a"
        
        print(f"{size:>12,} | {med_time:>10.6f} | {time_per_n:>10.8f} | {ratio_str:>10} | {expected_str:>10}")

    # Print summary
    print(f"\nSummary: {pass_count} passed, {fail_count} failed out of {len(results)} tests.")
    
    return pass_count == len(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
