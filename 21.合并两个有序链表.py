#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val < list2.val:
                begin = list1
                list1 = list1.next
            else:
                begin = list2
                list2 = list2.next
        elif list1:
            begin = list1
            list1 = list1.next
        elif list2:
            begin = list2
            list2 = list2.next
        else:
            return None
        index = begin
        while list1 and list2:
            if list1.val < list2.val:
                index.next = list1
                index = index.next
                list1 = list1.next
            else:
                index.next = list2
                index = index.next
                list2 = list2.next
        if list1:
            index.next = list1
        elif list2:
            index.next =  list2
        return begin
# @lc code=end

