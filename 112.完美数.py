'''
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
给定一个 整数 n， 如果他是完美数，返回 True，否则返回 False

示例：
输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14

提示：
输入的数字 n 不会超过 100,000,000. (1e8)
'''

#答：【枚举】
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:	
            return False	
        	
        i, sum1 = 1, 0	
        while i*i <= num:
            if num % i == 0:	
                sum1 += i	
                if i*i != num:	
                    sum1 += num / i	
            i += 1	
            	
        return sum1 - num == num
