"""
optimizer_reduction.py

This module provides utilities to reduce the impact of hardware and interpreter optimizations during benchmarking in Python.

Usage:
    from optimizer_reduction import reduce_optimizations
    reduce_optimizations(func, args, repeat=10, warmup=3)
"""
import gc
import time
import random
import os
import sys

def reduce_optimizations(func, args=(), repeat=10, warmup=3, randomize_args=False, restart_between_runs=False):
    """
    Run the function with strategies to reduce optimization effects:
    - Warm up runs
    - Multiple repeats with averaging
    - Optionally randomize arguments
    - Optionally restart interpreter between runs (expensive)
    - Garbage collection before each run
    Returns average execution time (seconds).
    """
    # Warm up
    for _ in range(warmup):
        _ = func(*args)
    times = []
    for i in range(repeat):
        call_args = args
        if randomize_args:
            # Only randomize if a single argument and it's a list/tuple
            if len(args) == 1 and isinstance(args[0], (list, tuple)):
                randomized = list(args[0])
                random.shuffle(randomized)
                call_args = (randomized,)
            # Otherwise, do not randomize
        gc.collect()
        start = time.perf_counter()
        if restart_between_runs:
            # Relaunch the script for each run (very slow)
            import subprocess
            result = subprocess.run([sys.executable, __file__, 'single_run'], capture_output=True)
            elapsed = float(result.stdout.decode().strip())
        else:
            _ = func(*call_args)
            elapsed = time.perf_counter() - start
        times.append(elapsed)
    avg_time = sum(times) / len(times)
    return avg_time

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == 'single_run':
    # For restart_between_runs mode
    import pickle
    # Dummy function for subprocess mode
    def dummy():
        sum(range(1000))
    start = time.perf_counter()
    dummy()
    elapsed = time.perf_counter() - start
    print(elapsed)
