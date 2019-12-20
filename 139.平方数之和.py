'''
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c。

示例1:
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5 

示例2:
输入: 3
输出: False
'''

#答：【二分查找】


#【使用 sqrt 函数】
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j=int(math.sqrt(c))
        i=0
        while i <=j:
            if c==i*i+j*j:
                return True
            elif i*i+j*j>c:
                j=j-1
            else:
                i=i+1

