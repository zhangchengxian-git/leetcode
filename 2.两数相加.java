/*
 * @lc app=leetcode.cn id=2 lang=java
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 public class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
*/ 
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        }if(l2 == null){
            return l1;
        }
        l1.val = l1.val + l2.val;
        if(l1.val > 9){
            l1.next = addTwoNumbers(new ListNode(l1.val/10), l1.next);
            l1.val = l1.val % 10;
        }
        l1.next = addTwoNumbers(l1.next, l2.next);
        return l1;
    }
}
// @lc code=end

