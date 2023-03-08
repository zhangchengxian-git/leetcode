/*
 * @lc app=leetcode.cn id=24 lang=java
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        ListNode begin = new ListNode(-1, head);
        ListNode last = begin;
        ListNode first = head;
        ListNode second = head.next;
        while(first != null && second != null){
            last.next = second;
            first.next = second.next;
            second.next = first;
            last = first;
            first = first.next;
            if(first == null){
                break;
            }
            second = first.next;
        }
        return begin.next;
    }
}
// @lc code=end

