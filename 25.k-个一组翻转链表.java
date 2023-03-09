/*
 * @lc app=leetcode.cn id=25 lang=java
 *
 * [25] K 个一组翻转链表
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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode begin = new ListNode(-1, head);
        ListNode left = begin;
        while(true){
            ListNode last = hasK(left, k);
            if(last == null){
                break;
            }
            ListNode right = last.next;
            ListNode first = left.next;
            ListNode from = left.next;
            ListNode to = from.next;
            for(int i=1; i<=k-1; i++){
                ListNode res = to.next;
                to.next = from;
                from = to;
                to = res;
            }
            left.next = from;
            first.next = right;
            left = first;
        }
        return begin.next;
    }
    private ListNode hasK(ListNode head, int k){
        for(int i=1; i<=k; i++){
            head = head.next;
            if(head == null){
                return null;
            }
        }
        return head;
    }
}
// @lc code=end

