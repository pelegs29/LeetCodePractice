# 205. Isomorphic Strings

def isIsomorphic(self, s: str, t: str) -> bool:
    return isomorphiocHelper(self, s, t) and isomorphiocHelper(self, t, s)


def isomorphiocHelper(self, s: str, t: str) -> bool:
    hash = {}
    for i in range(0, len(s)):
        x = s[i]
        if x in hash:
            if hash.get(x) == t[i]:
                continue
            else:
                return False
        else:
            hash[x] = t[i]
    return True
