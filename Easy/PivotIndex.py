# 724. Find Pivot Index

def pivotIndex(nums: list[int]) -> int:
    arr_sum = 0
    for x in nums:
        arr_sum += x

    left_sum = 0
    index = 0
    for val in nums:
        if left_sum == arr_sum - left_sum - val:
            return index
        left_sum += val
        index += 1
    return -1
