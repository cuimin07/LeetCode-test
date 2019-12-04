'''
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。
前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
(注：分数越高的选手，排名越靠前。)

示例 1:
输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。

提示:
N 是一个正整数并且不会超过 10000。
所有运动员的成绩都不相同。
'''

#答：
#思路
#1、先编出名次的列表
#2、在编出字典
#3、根据字典得出结果
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        k=4
        medel=["Gold Medal", "Silver Medal", "Bronze Medal"]
        while k<=len(nums):
            medel.append(str(k))
            k+=1
        n=sorted(nums)
        n.reverse()
        medel_to_score={}
        for i in range(len(n)):
            medel_to_score[n[i]]=medel[i]
        res=[]
        for j in nums:
            res.append(medel_to_score[j])
        return res
