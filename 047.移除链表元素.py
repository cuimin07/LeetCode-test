'''
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''

#答：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(float('-inf'))
        dummy.next = head
        previous, current = dummy, dummy.next
        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        return dummy.next 
