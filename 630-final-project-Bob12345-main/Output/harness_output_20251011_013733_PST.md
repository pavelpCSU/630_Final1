# Benchmark Harness Output

*Exported: 2025-10-11T09:40:57.896541*

```
=== Problem 1: Two Sum ===

--- Problem1-copilot-GPT-4.1-python (Python) ---

Test 1: Input size = 1,000
  Result: PASS
  Min: 226327.20 ns
  Max: 242525.40 ns
  Avg: 234220.88 ns
  Med: 234122.30 ns
  Std: 5591.60 ns
  (Each timing sample is averaged over 25 repetitions)

Test 2: Input size = 10,000
  Result: PASS
  Min: 2047399.88 ns
  Max: 3042721.92 ns
  Avg: 2434837.48 ns
  Med: 2300816.68 ns
  Std: 396191.86 ns
  (Each timing sample is averaged over 25 repetitions)

Test 3: Input size = 100,000
  Result: PASS
  Min: 20030954.64 ns
  Max: 36224879.40 ns
  Avg: 22577894.07 ns
  Med: 20416644.24 ns
  Std: 4980958.77 ns
  (Each timing sample is averaged over 25 repetitions)

Test 4: Input size = 1,000,000
  Result: PASS
  Min: 207186550.88 ns
  Max: 271322902.40 ns
  Avg: 222143626.52 ns
  Med: 211646595.36 ns
  Std: 20459526.92 ns
  (Each timing sample is averaged over 25 repetitions)

Complexity Analysis Table (all times in nanoseconds, ns):
Note: 'Expected Ratio' is the ratio of input sizes between consecutive tests (unitless)
Each timing sample is averaged over {results[0]['timing']['repeat']} repetitions per test run.
Big O Analysis (Expected): O(n)
  Input Size |     Med (ns) |     Min (ns) |     Max (ns) |     Avg (ns) |     Std (ns) |    Time/n (ns) | Actual Ratio |  Expected Ratio |      Big O |     Real. Big O
-----------------------------------------------------------------------------------------------------------------------------------------------------------
       1,000 |    234122.30 |    226327.20 |    242525.40 |    234220.88 |      5591.60 |     234.122300 |          n/a |             n/a |       O(n) |            O(n)
      10,000 |   2300816.68 |   2047399.88 |   3042721.92 |   2434837.48 |    396191.86 |     230.081668 |         9.83 |           10.00 |       O(n) |            O(n)
     100,000 |  20416644.24 |  20030954.64 |  36224879.40 |  22577894.07 |   4980958.77 |     204.166442 |         8.87 |           10.00 |       O(n) |            O(n)
   1,000,000 | 211646595.36 | 207186550.88 | 271322902.40 | 222143626.52 |  20459526.92 |     211.646595 |        10.37 |           10.00 |       O(n) |            O(n)
[Empirical Big O Confidence] 0.87

Python version: 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0]
Platform: linux

--- Problem1-copilot-Claude-Sonnet-3.5-python (Python) ---

Test 1: Input size = 1,000
  Result: PASS
  Min: 224294.52 ns
  Max: 434165.12 ns
  Avg: 264821.25 ns
  Med: 235174.10 ns
  Std: 67499.04 ns
  (Each timing sample is averaged over 25 repetitions)

Test 2: Input size = 10,000
  Result: PASS
  Min: 2019704.12 ns
  Max: 4538403.92 ns
  Avg: 2313808.49 ns
  Med: 2057849.92 ns
  Std: 783018.04 ns
  (Each timing sample is averaged over 25 repetitions)

Test 3: Input size = 100,000
  Result: PASS
  Min: 19890397.24 ns
  Max: 21974155.04 ns
  Avg: 21109359.90 ns
  Med: 21188234.40 ns
  Std: 753309.74 ns
  (Each timing sample is averaged over 25 repetitions)

Test 4: Input size = 1,000,000
  Result: PASS
  Min: 206472354.40 ns
  Max: 215174307.68 ns
  Avg: 210307883.51 ns
  Med: 209926921.02 ns
  Std: 3187023.27 ns
  (Each timing sample is averaged over 25 repetitions)

Complexity Analysis Table (all times in nanoseconds, ns):
Note: 'Expected Ratio' is the ratio of input sizes between consecutive tests (unitless)
Each timing sample is averaged over {results[0]['timing']['repeat']} repetitions per test run.
Big O Analysis (Expected): O(n)
  Input Size |     Med (ns) |     Min (ns) |     Max (ns) |     Avg (ns) |     Std (ns) |    Time/n (ns) | Actual Ratio |  Expected Ratio |      Big O |     Real. Big O
-----------------------------------------------------------------------------------------------------------------------------------------------------------
       1,000 |    235174.10 |    224294.52 |    434165.12 |    264821.25 |     67499.04 |     235.174100 |          n/a |             n/a |       O(n) |            O(n)
      10,000 |   2057849.92 |   2019704.12 |   4538403.92 |   2313808.49 |    783018.04 |     205.784992 |         8.75 |           10.00 |       O(n) |            O(n)
     100,000 |  21188234.40 |  19890397.24 |  21974155.04 |  21109359.90 |    753309.74 |     211.882344 |        10.30 |           10.00 |       O(n) |            O(n)
   1,000,000 | 209926921.02 | 206472354.40 | 215174307.68 | 210307883.51 |   3187023.27 |     209.926921 |         9.91 |           10.00 |       O(n) |            O(n)
[Empirical Big O Confidence] 1.00

Python version: 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0]
Platform: linux

=== Problem 2: Group Anagrams ===

--- Problem2-copilot-GPT-4.1-python (Python) ---

Test 1: Input size = 30
  Result: PASS
  Min: 36627.64 ns
  Max: 99215.96 ns
  Avg: 48271.52 ns
  Med: 38013.96 ns
  Std: 19742.68 ns
  (Each timing sample is averaged over 25 repetitions)

Test 2: Input size = 300
  Result: PASS
  Min: 240340.04 ns
  Max: 270699.20 ns
  Avg: 247706.82 ns
  Med: 242760.20 ns
  Std: 10302.66 ns
  (Each timing sample is averaged over 25 repetitions)

Test 3: Input size = 3,000
  Result: PASS
  Min: 2261432.04 ns
  Max: 2895472.04 ns
  Avg: 2388698.22 ns
  Med: 2269322.28 ns
  Std: 229319.97 ns
  (Each timing sample is averaged over 25 repetitions)

Complexity Analysis Table (all times in nanoseconds, ns):
Note: 'Expected Ratio' is the ratio of input sizes between consecutive tests (unitless)
Each timing sample is averaged over {results[0]['timing']['repeat']} repetitions per test run.
Big O Analysis (Expected): O(nk)
  Input Size |     Med (ns) |     Min (ns) |     Max (ns) |     Avg (ns) |     Std (ns) |    Time/n (ns) | Actual Ratio |  Expected Ratio |      Big O |     Real. Big O
-----------------------------------------------------------------------------------------------------------------------------------------------------------
          30 |     38013.96 |     36627.64 |     99215.96 |     48271.52 |     19742.68 |    1267.132000 |          n/a |             n/a |      O(nk) |            O(n)
         300 |    242760.20 |    240340.04 |    270699.20 |    247706.82 |     10302.66 |     809.200667 |         6.39 |           10.00 |      O(nk) |            O(n)
       3,000 |   2269322.28 |   2261432.04 |   2895472.04 |   2388698.22 |    229319.97 |     756.440760 |         9.35 |           10.00 |      O(nk) |            O(n)

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(nk), but empirical result is O(n).
Possible reasons: Input sizes may be too small to reveal true asymptotic behavior.

[Empirical Big O Confidence] 1.00

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(nk), but empirical result is O(n).
Possible reasons: Input sizes may be too small to reveal true asymptotic behavior.


Python version: 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0]
Platform: linux

--- Problem2-copilot-Claude-Sonnet-3.5-python (Python) ---

Test 1: Input size = 30
  Result: PASS
  Min: 34404.96 ns
  Max: 42337.52 ns
  Avg: 36363.83 ns
  Med: 35559.82 ns
  Std: 2284.34 ns
  (Each timing sample is averaged over 25 repetitions)

Test 2: Input size = 300
  Result: PASS
  Min: 237681.12 ns
  Max: 439000.72 ns
  Avg: 329962.97 ns
  Med: 326859.98 ns
  Std: 94526.70 ns
  (Each timing sample is averaged over 25 repetitions)

Test 3: Input size = 3,000
  Result: PASS
  Min: 2248173.68 ns
  Max: 2915025.64 ns
  Avg: 2334037.98 ns
  Med: 2262563.28 ns
  Std: 205316.53 ns
  (Each timing sample is averaged over 25 repetitions)

Complexity Analysis Table (all times in nanoseconds, ns):
Note: 'Expected Ratio' is the ratio of input sizes between consecutive tests (unitless)
Each timing sample is averaged over {results[0]['timing']['repeat']} repetitions per test run.
Big O Analysis (Expected): O(nk)
  Input Size |     Med (ns) |     Min (ns) |     Max (ns) |     Avg (ns) |     Std (ns) |    Time/n (ns) | Actual Ratio |  Expected Ratio |      Big O |     Real. Big O
-----------------------------------------------------------------------------------------------------------------------------------------------------------
          30 |     35559.82 |     34404.96 |     42337.52 |     36363.83 |      2284.34 |    1185.327333 |          n/a |             n/a |      O(nk) |            O(n)
         300 |    326859.98 |    237681.12 |    439000.72 |    329962.97 |     94526.70 |    1089.533267 |         9.19 |           10.00 |      O(nk) |            O(n)
       3,000 |   2262563.28 |   2248173.68 |   2915025.64 |   2334037.98 |    205316.53 |     754.187760 |         6.92 |           10.00 |      O(nk) |            O(n)

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(nk), but empirical result is O(n).
Possible reasons: Input sizes may be too small to reveal true asymptotic behavior.

[Empirical Big O Confidence] 0.60

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(nk), but empirical result is O(n).
Possible reasons: Input sizes may be too small to reveal true asymptotic behavior.


Python version: 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0]
Platform: linux

=== Problem 3: Median of Two Sorted Arrays ===

--- Problem3-copilot-GPT-4.1-python (Python) ---

Test 1: Input size = 50
  Result: PASS
  Min: 29755.88 ns
  Max: 51276.96 ns
  Avg: 33105.31 ns
  Med: 30640.34 ns
  Std: 6583.16 ns
  (Each timing sample is averaged over 25 repetitions)

Test 2: Input size = 500
  Result: PASS
  Min: 209705.32 ns
  Max: 238453.00 ns
  Avg: 221042.55 ns
  Med: 218625.04 ns
  Std: 9140.64 ns
  (Each timing sample is averaged over 25 repetitions)

Test 3: Input size = 5,000
  Result: PASS
  Min: 1993234.44 ns
  Max: 3259140.28 ns
  Avg: 2158274.03 ns
  Med: 2032427.66 ns
  Std: 388841.91 ns
  (Each timing sample is averaged over 25 repetitions)

Complexity Analysis Table (all times in nanoseconds, ns):
Note: 'Expected Ratio' is the ratio of input sizes between consecutive tests (unitless)
Each timing sample is averaged over {results[0]['timing']['repeat']} repetitions per test run.
Big O Analysis (Expected): O(log(min(n, m)))
  Input Size |     Med (ns) |     Min (ns) |     Max (ns) |     Avg (ns) |     Std (ns) |    Time/n (ns) | Actual Ratio |  Expected Ratio |      Big O |     Real. Big O
-----------------------------------------------------------------------------------------------------------------------------------------------------------
          50 |     30640.34 |     29755.88 |     51276.96 |     33105.31 |      6583.16 |     612.806800 |          n/a |             n/a | O(log(min(n, m))) |            O(n)
         500 |    218625.04 |    209705.32 |    238453.00 |    221042.55 |      9140.64 |     437.250080 |         7.14 |           10.00 | O(log(min(n, m))) |            O(n)
       5,000 |   2032427.66 |   1993234.44 |   3259140.28 |   2158274.03 |    388841.91 |     406.485532 |         9.30 |           10.00 | O(log(min(n, m))) |            O(n)

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(log(min(n, m))), but empirical result is O(n).
Possible reasons: Input sizes may be too small to reveal true asymptotic behavior.

[Empirical Big O Confidence] 0.99

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(log(min(n, m))), but empirical result is O(n).
Possible reasons: Input sizes may be too small to reveal true asymptotic behavior.


Python version: 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0]
Platform: linux

--- Problem3-copilot-Claude-Sonnet-3.5-python (Python) ---

Test 1: Input size = 50
  Result: PASS
  Min: 29903.44 ns
  Max: 36008.68 ns
  Avg: 31928.54 ns
  Med: 31201.32 ns
  Std: 1826.83 ns
  (Each timing sample is averaged over 25 repetitions)

Test 2: Input size = 500
  Result: PASS
  Min: 212128.44 ns
  Max: 349767.68 ns
  Avg: 244865.54 ns
  Med: 222337.26 ns
  Std: 50504.92 ns
  (Each timing sample is averaged over 25 repetitions)

Test 3: Input size = 5,000
  Result: PASS
  Min: 1990890.96 ns
  Max: 2682441.88 ns
  Avg: 2219155.07 ns
  Med: 2143551.38 ns
  Std: 249163.66 ns
  (Each timing sample is averaged over 25 repetitions)

Complexity Analysis Table (all times in nanoseconds, ns):
Note: 'Expected Ratio' is the ratio of input sizes between consecutive tests (unitless)
Each timing sample is averaged over {results[0]['timing']['repeat']} repetitions per test run.
Big O Analysis (Expected): O(log(min(n, m)))
  Input Size |     Med (ns) |     Min (ns) |     Max (ns) |     Avg (ns) |     Std (ns) |    Time/n (ns) | Actual Ratio |  Expected Ratio |      Big O |     Real. Big O
-----------------------------------------------------------------------------------------------------------------------------------------------------------
          50 |     31201.32 |     29903.44 |     36008.68 |     31928.54 |      1826.83 |     624.026401 |          n/a |             n/a | O(log(min(n, m))) |            O(n)
         500 |    222337.26 |    212128.44 |    349767.68 |    244865.54 |     50504.92 |     444.674520 |         7.13 |           10.00 | O(log(min(n, m))) |            O(n)
       5,000 |   2143551.38 |   1990890.96 |   2682441.88 |   2219155.07 |    249163.66 |     428.710276 |         9.64 |           10.00 | O(log(min(n, m))) |            O(n)

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(log(min(n, m))), but empirical result is O(n).
Possible reasons: Input sizes may be too small to reveal true asymptotic behavior.

[Empirical Big O Confidence] 1.00

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(log(min(n, m))), but empirical result is O(n).
Possible reasons: Input sizes may be too small to reveal true asymptotic behavior.


Python version: 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0]
Platform: linux

--- Problem3-copilot-GPT-4.1-C++ (C++) ---
Running C++ tests for Problem3-copilot-GPT-4.1-C++...

Complexity Analysis Table (all times in nanoseconds, ns):
Note: 'Expected Ratio' is the ratio of input sizes between consecutive tests (unitless)
Big O Analysis (Expected): O(log(min(n, m)))
  Input Size |     Med (ns) |     Min (ns) |     Max (ns) |     Avg (ns) |     Std (ns) |    Time/n (ns) | Actual Ratio |  Expected Ratio |      Big O |     Real. Big O
-----------------------------------------------------------------------------------------------------------------------------------------------------------
         100 |        71.25 |        70.55 |        75.35 |        71.71 |         1.35 |       0.712500 |          n/a |             n/a | O(log(min(n, m))) |        O(log n)
       1,000 |        96.78 |        95.05 |       116.28 |       100.62 |         7.93 |       0.096780 |         1.36 |           10.00 | O(log(min(n, m))) |        O(log n)
      10,000 |       124.18 |       123.90 |       157.15 |       128.31 |         9.88 |       0.012418 |         1.28 |           10.00 | O(log(min(n, m))) |        O(log n)
     100,000 |       134.66 |       133.89 |       217.70 |       145.74 |        24.93 |       0.001347 |         1.08 |           10.00 | O(log(min(n, m))) |        O(log n)
     200,000 |       149.00 |       142.65 |       180.39 |       153.65 |        12.68 |       0.000745 |         1.11 |            2.00 | O(log(min(n, m))) |        O(log n)
     400,000 |       168.93 |       168.25 |       202.08 |       175.19 |        12.25 |       0.000422 |         1.13 |            2.00 | O(log(min(n, m))) |        O(log n)
     800,000 |       163.21 |       156.70 |       186.58 |       166.45 |        10.19 |       0.000204 |         0.97 |            2.00 | O(log(min(n, m))) |        O(log n)
   1,600,000 |       175.13 |       174.35 |       271.74 |       187.36 |        29.05 |       0.000109 |         1.07 |            2.00 | O(log(min(n, m))) |        O(log n)

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(log(min(n, m))), but empirical result is O(log n).
Possible reasons: Possible causes include small input sizes, constant factors, implementation optimizations, or measurement noise.

[Empirical Big O Confidence] 0.95

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(log(min(n, m))), but empirical result is O(log n).
Possible reasons: Possible causes include small input sizes, constant factors, implementation optimizations, or measurement noise.

Test 1: PASS
Test 2: PASS
Test 3: PASS
Test 4: PASS
Test 5: PASS
Test 6: PASS
Test 7: PASS
Test 8: PASS

--- Problem3-copilot-Claude-Sonnet-3.5-C++ (C++) ---
Running C++ tests for Problem3-copilot-Claude-Sonnet-3.5-C++...

Complexity Analysis Table (all times in nanoseconds, ns):
Note: 'Expected Ratio' is the ratio of input sizes between consecutive tests (unitless)
Big O Analysis (Expected): O(log(min(n, m)))
  Input Size |     Med (ns) |     Min (ns) |     Max (ns) |     Avg (ns) |     Std (ns) |    Time/n (ns) | Actual Ratio |  Expected Ratio |      Big O |     Real. Big O
-----------------------------------------------------------------------------------------------------------------------------------------------------------
         100 |        76.34 |        75.88 |        86.06 |        78.60 |         3.66 |       0.763400 |          n/a |             n/a | O(log(min(n, m))) |        O(log n)
       1,000 |       127.98 |       119.83 |       153.59 |       132.15 |        10.48 |       0.127980 |         1.68 |           10.00 | O(log(min(n, m))) |        O(log n)
      10,000 |       139.80 |       137.57 |       167.89 |       144.04 |         9.20 |       0.013980 |         1.09 |           10.00 | O(log(min(n, m))) |        O(log n)
     100,000 |       194.33 |       185.25 |       217.79 |       195.77 |         8.40 |       0.001943 |         1.39 |           10.00 | O(log(min(n, m))) |        O(log n)
     200,000 |       210.45 |       199.26 |       240.01 |       213.65 |        13.83 |       0.001052 |         1.08 |            2.00 | O(log(min(n, m))) |        O(log n)
     400,000 |       215.96 |       207.93 |       291.01 |       225.90 |        23.38 |       0.000540 |         1.03 |            2.00 | O(log(min(n, m))) |        O(log n)
     800,000 |       223.53 |       209.76 |       240.73 |       223.79 |        10.52 |       0.000279 |         1.04 |            2.00 | O(log(min(n, m))) |        O(log n)
   1,600,000 |       214.38 |       206.09 |       255.14 |       222.97 |        16.39 |       0.000134 |         0.96 |            2.00 | O(log(min(n, m))) |        O(log n)

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(log(min(n, m))), but empirical result is O(log n).
Possible reasons: Possible causes include small input sizes, constant factors, implementation optimizations, or measurement noise.

[Empirical Big O Confidence] 0.94

[Big O Discrepancy Analysis]
Discrepancy detected: Theoretical Big O is O(log(min(n, m))), but empirical result is O(log n).
Possible reasons: Possible causes include small input sizes, constant factors, implementation optimizations, or measurement noise.

Test 1: PASS
Test 2: PASS
Test 3: PASS
Test 4: PASS
Test 5: PASS
Test 6: PASS
Test 7: PASS
Test 8: PASS

```