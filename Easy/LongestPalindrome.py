# 409. Longest Palindrome

def longestPalindrome(self, s: str) -> int:
    hash_map = {}
    max_pali = 0
    flag = 0
    for char in s:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
    for key in hash_map:
        if hash_map[key] == 1:
            flag = 1
        elif hash_map[key] % 2 == 0:
            max_pali += hash_map[key]
        else:
            max_pali += hash_map[key] - 1
            flag = 1
    return max_pali + flag
