/*
 * @lc app=leetcode.cn id=19 lang=java
 *
 * [19] 删除链表的倒数第 N 个结点
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
 }*/

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode res = head;
        ListNode delete = head;
        int step = 0;
        while(head.next != null){
            head = head.next;
            step += 1;
            if(step>=n+1){
                delete = delete.next;
            }
        }
        if(step == 0){
            return null;
        }else{
            if(step+1 == n){
                res = res.next;
            }else{
                delete.next = delete.next.next;
            }
        }
        return res;
    }
}
// @lc code=end

