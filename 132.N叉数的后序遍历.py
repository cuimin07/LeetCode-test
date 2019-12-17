'''
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :
返回其后序遍历: [5,6,3,2,4,1].

说明: 递归法很简单，你可以使用迭代法完成此题吗?
'''

#答：【迭代】
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, root_list = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                root_list.append(root.val)
            for c in root.children:
                stack.append(c)
        return root_list[::-1]
        
#【递归】
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        res = []
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res
