'''
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

'''

#答：【以右-根-左顺序遍历树，并进行值的累加】
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lSum = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.convertBST(root.right)
        self.lSum += root.val
        root.val = self.lSum
        self.convertBST(root.left)
        return root
