'''
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

示例：
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]

注意：
你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。
'''

#答：
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = ['q','w','e','r','t','y','u','i','o','p']
        middle = ['a','s','d','f','g','h','j','k','l']
        bottom = ['z','x','c','v','b','n','m']
        rows = [top, middle, bottom]
        result = []
        for word in words:
            for row in rows:
                if word[0].lower() in row:
                    result_row = row
                    break
            for char in word:
                j = 0
                if char.lower() not in result_row:
                    j = -1
                    break
            if j != -1:
                result.append(word)
        return result
