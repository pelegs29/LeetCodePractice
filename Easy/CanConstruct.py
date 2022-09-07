# 383. Ransom Note

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    mag_dict = {}
    for char in magazine:
        if char in mag_dict:
            mag_dict[char] += 1
        else:
            mag_dict[char] = 1
    for char in ransomNote:
        if char not in mag_dict:
            return False
        else:
            if mag_dict[char] <= 0:
                return False
            else:
                mag_dict[char] -= 1
    return True
