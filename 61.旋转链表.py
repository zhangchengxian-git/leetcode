#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        begin = ListNode(-1, head)
        last = begin
        length = 0
        while last.next:
            length += 1
            last = last.next
        if length < 2:
            return head
        k = k % length
        if k == 0:
            return head
        index = begin
        for i in range(length-k):
            index = index.next
        last.next = begin.next
        begin.next = index.next
        index.next = None
        return begin.next


# @lc code=end

