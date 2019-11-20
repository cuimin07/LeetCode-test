'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:
s = "leetcode"
返回 0.
s = "loveleetcode",
返回 2.

注意事项：您可以假定该字符串只包含小写字母。
'''

#答：【字典】
class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup =dict()
        for i in s:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        
        for i,c in enumerate(s):
            if lookup[c] == 1:
                return i
        
        return -1
