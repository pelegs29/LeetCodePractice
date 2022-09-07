# 1337. The K Weakest Rows in a Matrix

def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
    rankList = []
    for l in mat:
        value = 0
        for x in l:
            if x == 0:
                break
            value += 1
        rankList.append(value)
    output = []
    for i in range(0, k):
        min_index = rankList.index(min(rankList))
        output.append(min_index)
        # max size of m is 100
        rankList[min_index] = 101
    return output
