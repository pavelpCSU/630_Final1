def group_anagrams(strs):
	from collections import defaultdict
	groups = defaultdict(list)
	for s in strs:
		key = tuple(sorted(s))
		groups[key].append(s)
	# Sort each group and then sort the list of groups for canonical output
	result = [sorted(group) for group in groups.values()]
	result.sort()
	return result