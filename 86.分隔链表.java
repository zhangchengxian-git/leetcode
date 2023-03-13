/*
 * @lc app=leetcode.cn id=86 lang=java
 *
 * [86] 分隔链表
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
    public ListNode partition(ListNode head, int x) {
        ListNode small = new ListNode(-101);
        ListNode small_index = small;
        ListNode big = new ListNode(-101);
        ListNode big_index = big;
        while(head!=null){
            if(head.val<x){
                small_index.next = head;
                small_index = head;
                head = head.next;
                small_index.next = null;
            }else{
                big_index.next = head;
                big_index = head;
                head = head.next;
                big_index.next = null;
            }
        }
        small_index.next = big.next;
        return small.next;
    }
}
// @lc code=end

