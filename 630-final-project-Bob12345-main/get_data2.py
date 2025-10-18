import json
import os

def gen_two_sum(path):
    nums = list(range(1, 10001))  # 10,000 sequential integers
    target = nums[-1] + nums[-2]  # sum of two largest
    data = {"nums": nums, "target": target}
    with open(os.path.join(path, "input_4.json"), "w") as f:
        json.dump(data, f)
    print(f"Generated {path}/input_4.json (len(nums)={len(nums)})")

def gen_group_anagrams(path):
    base = ["abcde", "edcba", "bcdea", "cdeab", "eabcd"]
    # Amplify: 2000 groups, each with 5 anagrams, k=5
    strs = []
    for i in range(2000):
        for s in base:
            strs.append(f"{s}{i}")
    data = {"strs": strs}
    with open(os.path.join(path, "input_4.json"), "w") as f:
        json.dump(data, f)
    print(f"Generated {path}/input_4.json (len(strs)={len(strs)})")

def gen_median_sorted_arrays(path):
    nums1 = list(range(0, 5000))
    nums2 = list(range(5000, 15000))
    data = {"nums1": nums1, "nums2": nums2}
    with open(os.path.join(path, "input_4.json"), "w") as f:
        json.dump(data, f)
    print(f"Generated {path}/input_4.json (len(nums1)={len(nums1)}, len(nums2)={len(nums2)})")

def main():
    base = "data2"
    gen_two_sum(os.path.join(base, "p1"))
    gen_group_anagrams(os.path.join(base, "p2"))
    gen_median_sorted_arrays(os.path.join(base, "p3"))

if __name__ == "__main__":
    main()
