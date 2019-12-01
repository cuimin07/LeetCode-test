'''
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。

说明:
给出的房屋和供暖器的数目是非负数且不会超过 25000。
给出的房屋和供暖器的位置均是非负数且不会超过10^9。
只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
所有供暖器都遵循你的半径标准，加热的半径也一样。

示例 1:
输入: [1,2,3],[2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。

示例 2:
输入: [1,2,3,4],[1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
'''

#答：
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 存放每个房屋与加热器的最短距离
        res = []
        # 排序
        houses.sort()
        heaters.sort()
        for c in houses:
            # 二分查找，在heaters中寻找与房屋 c 最近的加热器
            left = 0
            right = len(heaters) - 1
            while left < right:
                mid = (left + right) >> 1
                if heaters[mid] < c:
                    left = mid + 1
                else:
                    right = mid
            # 若找到的值等于 c ，则说明 c 房屋处放有一个加热器，c 房屋到加热器的最短距离为 0
            if heaters[left] == c:
                res.append(0)
            # 若该加热器的坐标值小于 c ，说明该加热器的坐标与 c 之间没有别的加热器
            elif heaters[left] < c:
                res.append(c - heaters[left])
            # 若该加热器的坐标值大于 c 并且left不等于 0 ，说明 c 介于left和left-1之间，
            # 房屋到加热器的最短距离就是left和left - 1处加热器与 c 差值的最小值
            elif left:
                res.append(min(heaters[left] - c, c - heaters[left - 1]))
            else:
                res.append(heaters[left] - c)
        return max(res)
