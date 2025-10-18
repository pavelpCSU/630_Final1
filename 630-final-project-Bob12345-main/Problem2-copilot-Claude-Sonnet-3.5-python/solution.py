from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group anagrams together.
    
    Args:
        strs: List of strings
    
    Returns:
        List of lists where each inner list contains a group of anagrams
        
    Time Complexity: O(n * k * log k) where:
        n = number of strings
        k = maximum length of a string
    Space Complexity: O(n * k) for storing all strings
    """
    # Use defaultdict to automatically create empty lists for new keys
    anagram_groups = defaultdict(list)
    
    # Group strings by their sorted characters
    for s in strs:
        # Sort characters to get canonical form for anagrams
        sorted_chars = tuple(sorted(s))
        # Add string to its group
        anagram_groups[sorted_chars].append(s)
    
    # Convert to list format and sort as required:
    # 1. Sort strings within each group
    # 2. Sort groups by their first string
    result = []
    for group in anagram_groups.values():
        result.append(sorted(group))  # Sort strings within group
    result.sort(key=lambda x: x[0])  # Sort groups by first string
    
    return result