'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2

示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
'''

#答：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current:
            runner = current.next
            while runner and current.val == runner.val:
                runner = runner.next
            current.next = runner
            current = runner
        return head
