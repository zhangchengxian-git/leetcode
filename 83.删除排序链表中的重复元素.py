#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
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
        index = head
        nextDiffNode = head.next
        while index:
            if not nextDiffNode:
                index.next = nextDiffNode
                index = nextDiffNode
            elif index.val != nextDiffNode.val:
                index.next = nextDiffNode
                index = nextDiffNode
                nextDiffNode = nextDiffNode.next
            else:
                nextDiffNode = nextDiffNode.next
        return head

# @lc code=end

