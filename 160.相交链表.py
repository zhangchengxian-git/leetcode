#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_index = headA
        b_index = headB
        a_times = 1
        b_times = 1
        while a_index != b_index and a_times != 3 and b_times != 3:
            if a_index == b_index:
                return a_index
            if a_index.next:
                a_index = a_index.next
            elif not a_index.next and a_times == 1:
                a_index = headB
                a_times += 1
            else:
                a_times += 1
            if b_index.next:
                b_index = b_index.next
            elif not b_index.next and b_times == 1:
                b_index = headA
                b_times += 1
            else:
                b_times += 1
        if a_index == b_index:
            return a_index
        else:
            return None
            
# @lc code=end

