'''
二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
每个 LED 代表一个 0 或 1，最低位在右侧。


例如，上面的二进制手表读取 “3:25”。
给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

案例:
输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

注意事项:
输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
'''

#答：【回溯算法-递归】
class Solution(object):
    def __init__(self):
        self.result_all = None
        self.nums = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        self.visited = None
    
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.result_all = []
        self.visited = [0 for _ in range(len(self.nums))]
        self.dfs(num, 0, 0)
        return self.result_all
    
    def dfs(self, num, step, start):
        if step == num:
            self.result_all.append(self.handle_date(self.visited))
            return
        for i in range(start, len(self.nums)):
            self.visited[i] = 1
            if not self.calc_sum(self.visited):
                self.visited[i] = 0
                continue
            self.dfs(num, step + 1, i + 1)
            self.visited[i] = 0
        return
            
    def calc_sum(self, visited):
        sum_h = 0
        sum_m = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        return 0 <= sum_h <= 11 and 0 <= sum_m <= 59
    
    def handle_date(self, visited):
        sum_h = 0
        sum_m = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                continue
            if i < 4:
                sum_h += self.nums[i]
            else:
                sum_m += self.nums[i]
        result = "" + str(sum_h) + ":"
        if sum_m < 10:
            result += "0" + str(sum_m)
        else:
            result += str(sum_m)
        return result
