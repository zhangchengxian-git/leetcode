#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        return self.merge(lists, 0, len(lists)-1)
    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        else:
            mid = left + (right-left)//2
            return self.mergeTwoLists(self.merge(lists, left, mid), self.merge(lists, mid+1, right))
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val < list2.val:
                begin = list1
                list1 = list1.next
            else:
                begin = list2
                list2 = list2.next
        elif list1:
            return list1
        elif list2:
            return list2
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
'''
if __name__ == "__main__":
    lists = [[],[ListNode(-1, ListNode(5, ListNode(11)))], [], [ListNode(6, ListNode(10))]]
    So = Solution()
    So.mergeKLists(lists)
'''
# @lc code=end

