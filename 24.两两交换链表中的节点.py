#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        begin = ListNode(-1, head)
        last = begin
        first = head
        second = head.next
        while first and second:
            last.next = second
            first.next = second.next
            second.next = first
            last = first
            first = first.next
            if not first:
                break
            second = first.next
        return begin.next
# @lc code=end

