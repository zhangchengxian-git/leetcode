import java.util.List;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=95 lang=java
 *
 * [95] 不同的二叉搜索树 II
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<TreeNode> generateTrees(int n) {
        return buildTree(1, n);
    }

    private List<TreeNode> buildTree(int begin, int end){
        List<TreeNode> allTrees = new LinkedList<TreeNode>();
        if(begin>end){
            allTrees.add(null);
            return allTrees;
        }
        for(int i=begin; i<=end; i++){
            List<TreeNode> leftTrees = buildTree(begin, i-1);
            List<TreeNode> rightTrees = buildTree(i+1, end);
            for(TreeNode left: leftTrees){
                for(TreeNode right: rightTrees){
                    allTrees.add(new TreeNode(i, left, right));
                }
            }
        }
        return allTrees;
    }
}
// @lc code=end

