# 424. Longest Repeating Character Replacement
from collections import defaultdict


class Solution:
    def characterReplacement(self, s, k):
        counts = defaultdict(int)
        start = res = 0
        for end in range(len(s)):
            counts[s[end]] += 1
            win_size = end - start + 1
            if (win_size - max(counts.values())) > k:
                counts[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        return res
