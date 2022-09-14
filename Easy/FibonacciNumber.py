# 509. Fibonacci Number

mem = {}


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n - 1 not in mem:
                mem[n - 1] = self.fib(n - 1)
            if n - 2 not in mem:
                mem[n - 2] = self.fib(n - 2)
            return mem[n - 1] + mem[n - 2]

# recursive
# def fib(self, n: int) -> int:
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return self.fib(n - 1) + self.fib(n - 2)
