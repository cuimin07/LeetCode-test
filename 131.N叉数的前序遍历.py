'''
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :
返回其前序遍历: [1,3,5,6,2,4]。

说明: 递归法很简单，你可以使用迭代法完成此题吗?
'''

#答：【递归】
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        root_list = [root.val]
        for node in root.children:
            root_list += self.preorder(node)
        return root_list
#【迭代】
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, root_list = [root, ], []
        while stack:
            root = stack.pop()
            root_list.append(root.val)
            stack.extend(root.children[::-1])
        return root_list
