'''
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例:
输入：
s = "abcd"
t = "abcde"
输出：
e

解释：
'e' 是那个被添加的字母。
'''

#答：【字典】
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict= dict()
        for x in s:
            if x in s_dict:
                s_dict[x] += 1
            else:
                s_dict[x] = 1
        
        for y in t:
            if y not in s_dict:
                return y
            elif s_dict[y] == 0:
                return y
            else:
                s_dict[y] -= 1
