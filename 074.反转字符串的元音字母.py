'''
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:
输入: "hello"
输出: "holle"

示例 2:
输入: "leetcode"
输出: "leotcede"

说明:
元音字母不包含字母"y"。
'''

#答：
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        string = list(s)
        i, j = 0, len(s) - 1
        while i<j:
            if string[i].lower() not in vowels:
                i += 1
            elif string[j].lower() not in vowels:
                j -= 1
            else:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
        return ''.join(string)
