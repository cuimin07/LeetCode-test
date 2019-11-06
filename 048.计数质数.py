'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

#答：【数论中知识：一个数不是质数，则可以分解成一系列小于它的质数】
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        nums = [None] * n
        nums[0] = False
        nums[1] = False
        
        for i in range(n):
            if nums[i] == None:
                nums[i] = True
                for j in range(i+i,n,i):
                    nums[j] = False
        return sum(nums)
