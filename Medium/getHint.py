# 299. Bulls and Cows

from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        cows = sum(min(secret.count(x), guess.count(x)) for x in set(guess)) - bulls
        return str(bulls) + "A" + str(cows) + "B"

