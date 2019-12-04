'''
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:
输入: 100
输出: "202"

示例 2:
输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。
'''

#答：【根据二进制短除法的转换方法，类比到七进制的实现】
class Solution:
    def convertToBase7(self, num: int) -> str:
        base7 = []
        if num < 0:
            flag =1
            num = -num
        else:
            flag = 0
        while num >= 7:
            fig = str(num % 7)
            base7.append(fig)
            num = num // 7
        base7.append(str(num))
        if flag:
            base7.append('-')
        base7.reverse()
        return ''.join(base7)
