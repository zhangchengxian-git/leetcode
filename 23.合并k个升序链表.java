/*
 * @lc app=leetcode.cn id=23 lang=java
 *
 * [23] 合并K个升序链表
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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0){
            return null;
        }else{
            return merge(lists, 0, lists.length-1);
        }
    }
    private ListNode merge(ListNode[] lists, int left, int right){
        if(left == right){
            return lists[left];
        }else{
            int mid = left + (right - left)/2;
            return mergeTwoLists(merge(lists, left, mid), merge(lists, mid+1, right));
        }
    }
    private ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode begin = list1;
        if (list1 != null && list2 != null){
            if(list1.val<list2.val){
                list1 = list1.next;
            }else{
                begin = list2;
                list2 = list2.next;
            }
        }else if(list1 != null){
            list1 = list1.next;
        }else if(list2 != null){
            begin = list2;
            list2 = list2.next;
        }else{
            return null;
        }
        ListNode index = begin;
        while(list1 != null && list2 != null){
            if(list1.val<list2.val){
                index.next = list1;
                index = index.next;
                list1 = list1.next;
            }else{
                index.next = list2;
                index = index.next;
                list2 = list2.next;
            }
        }
        if(list1 != null){
            index.next = list1;
        }else if(list2 != null){
            index.next = list2;
        }
        return begin;
    }

}
// @lc code=end

