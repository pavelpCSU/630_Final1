import json
import os

def gen_two_sum(path):
    nums = list(range(1, 1000001))  # 1,000,000 sequential integers
    target = nums[-1] + nums[-2]  # sum of two largest
    data = {"nums": nums, "target": target}
    with open(os.path.join(path, "input_4.json"), "w") as f:
        json.dump(data, f)
    print(f"Generated {path}/input_4.json (len(nums)={len(nums)})")
    # Placeholder output
    with open(os.path.join(path, "output_4.json"), "w") as f:
        json.dump(None, f)

def gen_group_anagrams(path):
    base = ["abcde", "edcba", "bcdea", "cdeab", "eabcd"]
    # Amplify: 200,000 groups, each with 5 anagrams, k=5
    strs = []
    for i in range(200000):
        for s in base:
            strs.append(f"{s}{i}")
    data = {"strs": strs}
    with open(os.path.join(path, "input_4.json"), "w") as f:
        json.dump(data, f)
    print(f"Generated {path}/input_4.json (len(strs)={len(strs)})")
    # Placeholder output
    with open(os.path.join(path, "output_4.json"), "w") as f:
        json.dump(None, f)

def gen_median_sorted_arrays(path):
    nums1 = list(range(0, 500000))
    nums2 = list(range(500000, 1500000))
    data = {"nums1": nums1, "nums2": nums2}
    with open(os.path.join(path, "input_4.json"), "w") as f:
        json.dump(data, f)
    print(f"Generated {path}/input_4.json (len(nums1)={len(nums1)}, len(nums2)={len(nums2)})")
    # Placeholder output
    with open(os.path.join(path, "output_4.json"), "w") as f:
        json.dump(None, f)

def main():
    base = "data2"
    gen_two_sum(os.path.join(base, "p1"))
    gen_group_anagrams(os.path.join(base, "p2"))
    gen_median_sorted_arrays(os.path.join(base, "p3"))

if __name__ == "__main__":
    main()
