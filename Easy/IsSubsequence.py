# 392. Is Subsequence

def isSubsequence(s: str, t: str) -> bool:
    if len(t) < len(s):
        return False
    if len(s) == 0:
        return True
    index = 0
    for x in t:
        if s[index] == x:
            if index == len(s) - 1:
                return True
            index += 1
    return False

