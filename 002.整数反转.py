#给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

class Solution:
    def reverse(self, x: int) -> int:
        y,res = abs(x), 0
        of = (1<<31)-1 if x>0 else 1<<31
        while y!=0:
            res = res*10 +y%10
            if res>of:return 0
            y//=10
        return res if x>0 else -res
        

#---------//     取整除，返回商的整数部分（向下取整）
#---------//==   取整除赋值运算符
#---------<<     左移动运算符，运算数的各二进位全部左移若干位，由 "<<" 右边的数指定移动的位数，高位丢弃，低位补 。
