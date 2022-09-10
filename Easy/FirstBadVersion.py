# 278. First Bad Version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(self, n: int) -> int:
    low = 0
    high = n
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if isBadVersion(mid):
            if not isBadVersion(mid - 1):
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
