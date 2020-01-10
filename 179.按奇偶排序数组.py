'''
给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
你可以返回满足此条件的任何数组作为答案。

示例：
输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
 
提示：
1 <= A.length <= 5000
0 <= A[i] <= 5000
'''

#答：【排序】
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x : x%2)
        return A

#【两边扫描】
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])
                
                
#【原地处理】
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A
