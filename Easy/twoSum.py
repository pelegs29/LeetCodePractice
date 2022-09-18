# 1. Two Sum
from collections import defaultdict


def twoSum(nums: list[int], target: int) -> list[int]:
    h_map = defaultdict(int)
    for x in nums:
        h_map[x] += 1
    for num in nums:
        if num == target - num:
            if h_map[num] == 2:
                first = nums.index(num)
                nums[first] = target - 1
                return [first, nums.index(num)]
            else:
                continue
        if (target - num) in h_map:
            return [nums.index(num), nums.index(target - num)]


twoSum([-1,-2,-3,-4,-5], -8)
