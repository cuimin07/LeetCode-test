'''
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
'''

#答：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(root, direction=''):
            if root is None:
                return 0
            if not root.left and not root.right:
                if direction == 'l':
                    return root.val
            
            left, right = 0, 0
            if root.left:
                left = helper(root.left, 'l')
            if root.right:
                right = helper(root.right, 'r')
            return left+right
        return helper(root, '')
