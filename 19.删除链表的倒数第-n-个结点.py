#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = head
        delete = head
        step = 0
        while head.next:
            head = head.next
            step = step + 1
            if step >= n+1:
                delete = delete.next
        if step == 0:
            return None
        if step+1 == n:
            res = res.next
        else:
            delete.next = delete.next.next
        return res
'''
if __name__ == "__main__":
    So = Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    print(So.removeNthFromEnd(head, 2))
'''
# @lc code=end

