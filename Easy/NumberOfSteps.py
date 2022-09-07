# 1342. Number of Steps to Reduce a Number to Zero

def numberOfSteps(self, num: int) -> int:
    steps = 0
    while num != 0:
        steps += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
    return steps


#bit counting :
# class Solution:
#     def numberOfSteps (self, num: int) -> int:
#         steps = num == 0
#         while num > 0:
#             steps += 1 + (num & 1)
#             num >>= 1
#         return steps - 1
