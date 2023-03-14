/*
 * @lc app=leetcode.cn id=92 lang=java
 *
 * [92] 反转链表 II
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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(left == right){
            return head;
        }
        ListNode begin = new ListNode(-501, head);
        ListNode index, last, end, re_end;
        index = last = end = re_end = begin;

        for(int i=0; i<=right; i++){
            if(i==left-1){
                last = index;
                index = index.next;
            }else if(i<left){
                index = index.next;
            }else if(i==left){
                end = re_end = index;
                index = index.next;                
            }else{
                last.next = index;
                ListNode next_index = index.next;
                index.next = end;
                end = index;
                index = next_index;
            }
            if(i==right){
                re_end.next = index;
            }
        }
        return begin.next;
    }
}
// @lc code=end

