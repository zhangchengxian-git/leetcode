/*
 * @lc app=leetcode.cn id=61 lang=java
 *
 * [61] 旋转链表
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
    public ListNode rotateRight(ListNode head, int k) {
        ListNode begin = new ListNode(-1, head);
        ListNode last = begin;
        int length = 0;
        while(last.next != null){
            length += 1;
            last = last.next;
        }
        if(length<2){
            return head;
        }
        k = k % length;
        if(k==0){
            return head;
        }
        ListNode index = begin;
        for(int i=0; i<length-k; i++){
            index = index.next;
        }
        last.next = begin.next;
        begin.next = index.next;
        index.next = null;
        return begin.next;
    }
}
// @lc code=end

