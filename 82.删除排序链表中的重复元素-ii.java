/*
 * @lc app=leetcode.cn id=82 lang=java
 *
 * [82] 删除排序链表中的重复元素 II
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
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null){
            return head;
        }
        ListNode begin = new ListNode(-101, head);
        ListNode pre = begin;
        ListNode index = head;
        while(index!=null && index.next!=null){
            if(index.next.val != index.val){
                pre = index;
                index = index.next;
            }else{
                while(index.next!=null &&index.next.val==index.val){
                    index = index.next;
                }
                index = index.next;
                pre.next = index;
            }
        } 
        return begin.next;
    }
}
// @lc code=end

