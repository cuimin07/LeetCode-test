'''
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:
输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
注意：
节点值的范围在32位有符号整数范围内。
'''

#答：【层次遍历】
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        lists=[]
        lists.append(root)
        result=[]
        while lists:
            length=len(lists)
            nums=0
            for n in range(length):
                node=lists.pop(0)
                nums+=node.val
                if node.left:
                    lists.append(node.left)
                if node.right:
                    lists.append(node.right)
            result.append(nums/length)
        return result
