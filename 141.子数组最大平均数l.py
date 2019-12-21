'''
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:
输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
 
注意:
1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
'''

#答：【双指针】
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right, cur_sum = 0, k, sum(nums[:k])          # 初始化左右指针和当前滑窗中的元素和
        max_sum = cur_sum                                   # 定义当前最大值
        while right < len(nums):                            # 遍历滑窗
            cur_sum = cur_sum + nums[right] - nums[left]    # 获得当前滑窗中的元素和
            max_sum = max(max_sum, cur_sum)                 # 更新当前最大和
            left, right = left + 1, right + 1               # 左右指针右移
        return max_sum / k 
