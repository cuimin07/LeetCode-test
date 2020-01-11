'''
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：
输入："ab-cd"
输出："dc-ba"

示例 2：
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

示例 3：
输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!" 

提示：
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S 中不包含 \ or "
'''

#答：【字母栈】
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return ''.join(ans)
        
#【双指针】        
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j-=1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)
        return ''.join(ans)
