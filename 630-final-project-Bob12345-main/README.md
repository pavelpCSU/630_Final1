## Benchmarking Workflow

**To run all benchmarks and see results, execute:**

```bash
python3 benchmark_rubric_harness.py
```

This script will automatically build and run all C++ and Python solutions, collect timing and correctness data, and print unified summary tables.

**Do not run the C++ run_tests binaries directly.** All output and reporting is handled by the Python harness for consistency.

---

## Harness Options

The benchmark harness supports several options and configuration flags:

### 1. Data Folder Selection

- By default, the harness uses the `data/` folder for test cases.
- To use the larger `data2/` folder, pass `data2` as a command-line argument:

```bash
python3 benchmark_rubric_harness.py data2
```

### 2. Optimizer Reduction Control

The harness uses optimizer reduction to improve timing accuracy. You can control this behavior by editing the following variables at the top of `benchmark_rubric_harness.py`:

- `USE_OPTIMIZER_REDUCTION`: Set to `True` (default) to enable, or `False` to disable optimizer reduction.
- `OPTIMIZER_REDUCTION_LEVEL`: Controls the aggressiveness of reduction. Options:
	- `'off'`: No reduction (fastest, least accurate)
	- `'low'`: Light reduction
	- `'medium'`: (default) Balanced
	- `'high'`: Strong reduction
	- `'max'`: Maximum reduction (slowest, most accurate)

Example (edit in `benchmark_rubric_harness.py`):

```python
USE_OPTIMIZER_REDUCTION = True
OPTIMIZER_REDUCTION_LEVEL = 'medium'  # Options: 'off', 'low', 'medium', 'high', 'max'
```

### 3. Customizing Iterations

You can change the number of timing iterations by editing the `iterations` parameter in the `main()` function call (default is 10).

---

## Summary of Usage

| Option/Flag                | How to Use                                                      |
|----------------------------|-----------------------------------------------------------------|
| Use default data           | `python3 benchmark_rubric_harness.py`                           |
| Use large data set         | `python3 benchmark_rubric_harness.py data2`                     |
| Change optimizer reduction | Edit `USE_OPTIMIZER_REDUCTION` and `OPTIMIZER_REDUCTION_LEVEL`  |
| Change timing iterations   | Edit `iterations` in `main()` in `benchmark_rubric_harness.py`  |

---

For more details, see comments in `benchmark_rubric_harness.py`.
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/TXqbkY7N)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20761573)
