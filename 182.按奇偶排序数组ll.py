'''
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。

示例：
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

提示：
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''

#答：【两次遍历】
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        N = len(A)
        ans = [None] * N
        t=0
        for i, x in enumerate(A):
            if x%2 == 0:
                ans[t] = x
                t+=2
        t=1
        for i, x in enumerate(A):
            if x % 2 == 1:
                ans[t] = x
                t+=2
        
        return ans
        
#【不使用额外空间】
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[j], A[i] = A[i], A[j]
        return A
