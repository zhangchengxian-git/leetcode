#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = [[root.val]]
        pre_node = [root]
        while pre_node != []:
            res = []
            node = []
            for no in pre_node:
                if no.left:
                    node.append(no.left)
                    res.append(no.left.val)
                if no.right:
                    node.append(no.right)
                    res.append(no.right.val)
            if res != []:
                result.append(res)
            pre_node = node
        return result
            
# @lc code=end

