import difflib

def analyze_bigo_discrepancy(theoretical: str, empirical: str, context: dict = None) -> str:
    """
    Analyze and explain the discrepancy between theoretical and empirical Big O results.
    Optionally use context (e.g., timing data, input sizes, code snippets) for a more detailed explanation.
    """
    if theoretical == empirical:
        return f"The empirical Big O matches the theoretical expectation: {theoretical}. This suggests the implementation behaves as expected for the tested input sizes."

    explanation = f"Discrepancy detected: Theoretical Big O is {theoretical}, but empirical result is {empirical}.\n"
    reasons = []
    if context:
        # Check for small input sizes
        sizes = context.get('sizes')
        if sizes and max(sizes) < 10000:
            reasons.append("Input sizes may be too small to reveal true asymptotic behavior.")
        # Check for implementation details
        code = context.get('code')
        if code and 'sort' in code:
            reasons.append("The use of built-in sort functions may affect empirical complexity.")
        # Check for constant factors
        times = context.get('times')
        if times and min(times) < 1e-6:
            reasons.append("Constant-time operations may dominate for small inputs.")
    # General reasons
    if theoretical.startswith('O(n)') and empirical == 'O(log n)':
        reasons.append("The implementation may have optimizations or early exits that reduce average-case complexity.")
    if theoretical == 'O(log n)' and empirical == 'O(n)':
        reasons.append("The implementation may not fully exploit logarithmic algorithms, or input data may not trigger best-case behavior.")
    if not reasons:
        reasons.append("Possible causes include small input sizes, constant factors, implementation optimizations, or measurement noise.")
    explanation += "Possible reasons: " + "; ".join(reasons)
    return explanation

# Example usage:
# print(analyze_bigo_discrepancy('O(n)', 'O(log n)', {'sizes': [1000, 10000, 100000], 'times': [0.01, 0.02, 0.03]}))
