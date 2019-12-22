'''
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:
输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
输出: True

案例 2:
输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
输出: False
'''

#答：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        s = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            s.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        for num in s:
            if k - num in s and 2 * (k - num) != k:
                return True
        return False
        
        
#【中序遍历+双指针】
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left)+[root.val]+inorder(root.right)
        numbers = sorted(inorder(root))
        n = len(numbers)
           
        i = 0
        j = n-1
        while i < j:
             if numbers[i] + numbers[j] > k:
                j -= 1
             elif numbers[i] + numbers[j] < k:
                i +=1
             else:
                return True
        return False
