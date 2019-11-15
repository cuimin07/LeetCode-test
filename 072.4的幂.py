'''
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:
输入: 16
输出: true

示例 2:
输入: 5
输出: false

进阶：
你能不使用循环或者递归来完成本题吗？
'''

#答：
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        elif num <= 3:
            return False
        
        while num > 4:
            if num % 4 == 0:
                num /= 4
            else:
                return False
        
        if num == 4:
            return True
        else:
            return False
