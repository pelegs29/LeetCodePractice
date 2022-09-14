# 70. Climbing Stairs

mem = {}


class Solution:
    def climbStairs(self, n: int) -> int:
        mem[1] = 1
        mem[2] = 2
        if n not in mem:
            mem[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return mem[n]

# recursive (long time)
# def climbStairs(self, n: int) -> int:
#     if n <= 1:
#         return 1
#     else:
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
