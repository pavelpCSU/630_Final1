DEBUG = False  # Set to False to disable debug output globally

import warnings as pywarnings

class EmpiricalBigOResult:
    def __init__(self, best_class, best_score, mse_dict, warning=None):
        self.best_class = best_class
        self.best_score = best_score
        self.mse_dict = mse_dict  # {class: mse}
        self.warning = warning
    def __str__(self):
        msg = f"{self.best_class} (confidence: {self.confidence():.2f})"
        if self.warning:
            msg += f" [Warning: {self.warning}]"
        return msg
    def confidence(self):
        # Lower MSE = higher confidence, but scale for user
        if self.best_score == 0:
            return 1.0
        # Compare best to next best
        sorted_mse = sorted(self.mse_dict.values())
        if len(sorted_mse) > 1 and sorted_mse[1] > 0:
            return max(0.0, min(1.0, 1 - self.best_score / sorted_mse[1]))
        return max(0.0, min(1.0, 1 - self.best_score))
import time
import numpy as np
from typing import Callable, List, Tuple


def time_function(func: Callable, inputs: List) -> float:
    """Times the execution of a function over a list of inputs and returns the average time."""
    times = []
    for inp in inputs:
        start = time.perf_counter()
        func(inp)
        end = time.perf_counter()
        times.append(end - start)
    return np.mean(times)



def empirical_bigo_from_data(sizes: list, times: list) -> str:
    """
    Estimates the empirical Big O of a function by fitting measured times to common complexity classes.
    sizes: list of input sizes
    times: list of measured times (e.g., median times)
    Returns a string representing the closest Big O class.
    """
    import numpy as np
    n = np.array(sizes)
    t = np.array(times)
    if DEBUG:
        print("[DEBUG] Empirical Big O input sizes:", n)
        print("[DEBUG] Empirical Big O measured times:", t)
    if len(n) < 2 or np.any(n <= 0):
        if DEBUG:
            print("[DEBUG] Not enough data or invalid sizes.")
        return EmpiricalBigOResult('n/a', float('inf'), {}, warning="Insufficient data")
    # Build all classes
    classes = [
        ('O(1)', np.ones_like(n)),
        ('O(log n)', np.log2(n + 1)),
        ('O(n)', n),
        ('O(n log n)', n * np.log2(n + 1)),
        ('O(n^2)', n ** 2),
        ('O(n^3)', n ** 3),
    ]
    if np.all(n < 30):
        classes.append(('O(2^n)', 2 ** n))
    best_class = None
    best_score = float('inf')
    mse_dict = {}
    warning = None
    for name, f in classes:
        if DEBUG:
            print(f"[DEBUG] Trying class {name} with f:", f)
        if np.any(np.isnan(f)):
            if DEBUG:
                print(f"[DEBUG] Skipping class {name} due to NaN.")
            continue
        try:
            # Normalize f to avoid numerical issues
            f_norm = (f - f.min()) / (f.max() - f.min()) if f.max() != f.min() else f
            t_norm = (t - t.min()) / (t.max() - t.min()) if t.max() != t.min() else t
            with pywarnings.catch_warnings(record=True) as wlist:
                pywarnings.simplefilter('always')
                a, b = np.polyfit(f_norm, t_norm, 1)
                pred = a * f_norm + b
                mse = np.mean((t_norm - pred) ** 2)
                mse_dict[name] = mse
                if DEBUG:
                    print(f"[DEBUG] Class {name}: mse={mse}, a={a}, b={b}")
                if mse < best_score:
                    best_score = mse
                    best_class = name
                # Check for RankWarning
                for warn in wlist:
                    if issubclass(warn.category, pywarnings.Warning):
                        warning = str(warn.message)
        except Exception as e:
            if DEBUG:
                print(f"[DEBUG] Exception for class {name}: {e}")
            continue
    if DEBUG:
        print(f"[DEBUG] Best class: {best_class} with score {best_score}")
    return EmpiricalBigOResult(best_class if best_class else 'n/a', best_score, mse_dict, warning=warning)

# Example usage (to be replaced with actual function and input generator):
# def example_func(arr):
#     return sum(arr)
# def input_gen(size):
#     return [list(range(size)) for _ in range(10)]
# print(empirical_bigo(example_func, input_gen, [10, 100, 1000, 10000]))
