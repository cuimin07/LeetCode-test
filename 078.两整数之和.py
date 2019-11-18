'''
不使用运算符 + 和 -，计算两整数 a 、b 之和。

示例 1:
输入: a = 1, b = 2
输出: 3

示例 2:
输入: a = -2, b = 3
输出: 1
'''

#答：
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0x100000000
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            carry = (a & b) << 1 
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT) 
