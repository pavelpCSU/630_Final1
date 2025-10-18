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
        # Make hashing more expensive
        return hash(self.str_val + self.str_val)

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

def wrapped_group_anagrams(strs):
    """Group anagrams implementation using StringWrapper objects"""
    # Count string occurrences first
    str_counts = {}
    for s in strs:
        str_counts[s] = str_counts.get(s, 0) + 1
    
    # Convert unique strings to wrapped objects
    unique_strs = list(str_counts.keys())
    wrapped_strs = [StringWrapper(s) for s in unique_strs]
    
    # Use sorted characters as key for anagram groups
    groups = {}
    
    # Group strings by their sorted characters
    for wrapped in wrapped_strs:
        key = wrapped.get_sorted()
        if key not in groups:
            groups[key] = []
        # Add each string as many times as it appears in input
        groups[key].extend([wrapped.str_val] * str_counts[wrapped.str_val])
    
    # Convert to list format and sort
    result = []
    for key in sorted(groups.keys()):
        # Sort strings within each group
        group = sorted(groups[key])
        result.append(group)
    
    # Sort groups by their first string
    result.sort(key=lambda x: x[0])
    
    return result

def measure_execution_time(strs, iterations=10):
    times = []
    
    for _ in range(iterations):
        gc.collect()
        create_memory_pressure()
        
        # Force fresh memory allocation
        test_data = strs.copy()
        
        start = time.perf_counter_ns()
        result = wrapped_group_anagrams(test_data)
        end = time.perf_counter_ns()
        
        times.append((end - start) / 1e9)
        
        # Validate result maintains string counts
        flat_result = [item for group in result for item in group]
        input_counts = {}
        result_counts = {}
        for s in strs:
            input_counts[s] = input_counts.get(s, 0) + 1
        for s in flat_result:
            result_counts[s] = result_counts.get(s, 0) + 1
        assert input_counts == result_counts, "String counts don't match"
    
    return {
        'min': min(times),
        'max': max(times),
        'avg': statistics.mean(times),
        'med': statistics.median(times),
        'std': statistics.stdev(times)
    }

def main():
    test_cases = [
        ('data/p2/input_1.json', 'data/p2/output_1.json'),
        ('data/p2/input_2.json', 'data/p2/output_2.json'),
        ('data/p2/input_3.json', 'data/p2/output_3.json')
    ]
    
    print("Detailed Performance Analysis (StringWrapper Version)")
    print("-" * 80)
    print("Using wrapped strings with expensive string operations")
    print("Each string wrapped in a class with lazy sorting")
    
    results = []
    
    for i, (input_file, output_file) in enumerate(test_cases, 1):
        print(f"\nRunning Test {i}...")
        
        input_data, expected = load_test_case(input_file, output_file)
        strs = input_data['strs']
        
        print(f"Input size: {len(strs):,} strings")
        
        timing = measure_execution_time(strs)
        result = wrapped_group_anagrams(strs)
        is_correct = result == expected['groups']
        
        results.append({
            'size': len(strs),
            'timing': timing,
            'passed': is_correct
        })
        
        print(f"Execution times over 10 iterations (wrapped strings):")
        print(f"  Min: {timing['min']:.6f}s")
        print(f"  Max: {timing['max']:.6f}s")
        print(f"  Avg: {timing['avg']:.6f}s")
        print(f"  Med: {timing['med']:.6f}s")
        print(f"  Std: {timing['std']:.6f}s")
        print(f"{'✅' if is_correct else '❌'} Test {i} {'PASSED' if is_correct else 'FAILED'}")
        
        if not is_correct:
            print("\nFirst difference in output:")
            # Find first differing group
            for g1, g2 in zip(result, expected['groups']):
                if g1 != g2:
                    print(f"Got:      {g1}")
                    print(f"Expected: {g2}")
                    break
    
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