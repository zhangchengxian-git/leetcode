#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        begin = ListNode(-101, head)
        pre = begin
        index = head
        while index and index.next:
            if index.next.val != index.val:
                pre = index
                index = index.next
            else:
                while index.next and index.next.val == index.val:
                    index = index.next
                index = index.next
                pre.next = index
        return begin.next
            
# @lc code=end

