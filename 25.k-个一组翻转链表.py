#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        begin = ListNode(-1, head)
        left = begin
        while True:
            last = self.hasKNodes(left.next, k)
            if not last:
                break
            right = last.next
            first = left.next
            fro = left.next
            to = fro.next
            for i in range(k-1):
               res = to.next
               to.next = fro
               if i == 0:
                   fro.next = right
               fro = to
               to = res
            left.next = fro
            left = first
        return begin.next
    
    def hasKNodes(self, begin: Optional[ListNode], k: int) -> Optional[ListNode]:
        for i in range(k-1):
            if not begin:
                return None
            begin = begin.next
        return begin
# @lc code=end

