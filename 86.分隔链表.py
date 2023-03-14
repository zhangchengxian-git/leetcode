#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(-101)
        small_index = small
        big = ListNode(-101)
        big_index = big
        while head:
            if head.val < x:
                small_index.next = head
                small_index = small_index.next
                head = head.next
                small_index.next = None
            else:
                big_index.next = head
                big_index = big_index.next
                head = head.next
                big_index.next = None
        small_index.next = big.next
        return small.next
        
            
# @lc code=end

