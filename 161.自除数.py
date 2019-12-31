'''
自除数 是指可以被它包含的每一位数除尽的数。
例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
还有，自除数不允许包含 0 。
给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：
输入： 
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

注意：
每个输入参数的边界满足 1 <= left <= right <= 10000。
'''

#答：【int转str】
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True
        
        res = []
        for n in range(left, right+1):
            if self_dividing(n):
                res.append(n)
        return res
        
        
#【取余】
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def self_dividing(n):
            x = n
            while x>0:
                x, d = divmod(x, 10)
                if d == 0 or n % d > 0:
                    return False
            return True
        
        res = []
        for n in range(left, right+1):
            if self_dividing(n):
                res.append(n)
        return res
