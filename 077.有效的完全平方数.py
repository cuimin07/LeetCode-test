'''
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
说明：不要使用任何内置的库函数，如  sqrt。

示例 1：
输入：16
输出：True

示例 2：
输入：14
输出：False
'''

#答：
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            if  mid > num / mid:
                right = mid - 1
            elif mid == num / mid:
                return True
            else:
                left = mid + 1
        return left == num//left and num % left == 0 
