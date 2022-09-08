# 215. Kth Largest Element in an Array

import heapq

def findKthLargest(self, nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[k - 1]


# selection sort
# def findKthLargest(self, nums, k):
#     if not nums: return
#     pivot = random.choice(nums)
#     left = [x for x in nums if x > pivot]
#     mid = [x for x in nums if x == pivot]
#     right = [x for x in nums if x < pivot]
#
#     L, M = len(left), len(mid)
#
#     if k <= L:
#         return self.findKthLargest(left, k)
#     elif k > L + M:
#         return self.findKthLargest(right, k - L - M)
#     else:
#         return mid[0]

findKthLargest(None, [3, 2, 1, 5, 6, 4], 2)
