'''
给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。

举个例子，A = "abcd"，B = "cdabcdab"。
答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。

注意:
A 与 B 字符串的长度在1和10000区间范围内。
'''

#答：
#遍历时重点需要注意：构造出的字符串的最大长度不能超过2*len(A)+len(B)。为什么要选择这个数字？
#考虑以下情况：
#如果字符串A比字符串B长：
#（1）字符串A本来就包含字符串B，这时A仅复制一遍就找到了，最大长度为len(A)；
#（2）字符串A复制一遍包含字符B，这时A的重复次数为2，遍历控制范围是len(A)2；
#（3）字符串A复制一遍不包含字符B，那么无论复制多少遍也不包含字符B，控制长度在len(A)2即可。
#如果字符串A比字符串B短，我们将字符串A复制到刚好大于字符串B的长度，长度控制为不小于len(B)时跳出循环。
#以上两种情况取最大值，求和即可：len(A)*2+len(B)。

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        A_repeat, r = A, 1
        while len(A_repeat) < 2 * len(A) + len(B):
            if B in A_repeat:
                return r
            A_repeat, r = A_repeat + A, r+1
        return -1
