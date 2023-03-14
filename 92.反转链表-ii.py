#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        begin = ListNode(-501, head)
        index = begin
        i = 0
        while i <= right: 
            if i == left-1:
                last = index
                index = index.next
            elif i < left:
                index = index.next
            elif i == left:
                end = index
                re_end = index
                index = index.next
            else:
                last.next = index
                next_index = index.next
                index.next = end
                end = index
                index = next_index
            if i == right:
                re_end.next = index
            i+=1
        return begin.next


# @lc code=end

