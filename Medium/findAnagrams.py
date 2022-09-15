# 438. Find All Anagrams in a String
from collections import defaultdict


def findAnagrams(s: str, p: str) -> list[int]:
    h_map = defaultdict(int)
    output = []
    size_p = len(p)
    size_s = len(s)
    if size_p > size_s:
        return output
    for c in p:
        h_map[c] += 1
    for i in range(size_p):
        if s[i] in h_map:
            h_map[s[i]] -= 1
    for i in range(size_s - size_p + 1):
        if all(val == 0 for val in h_map.values()):
            output.append(i)
        if s[i] in h_map:
            h_map[s[i]] += 1
        if i + size_p < size_s and s[i + size_p] in h_map:
            h_map[s[i + size_p]] -= 1
    return output


findAnagrams("cbaebabacd", "abc")
