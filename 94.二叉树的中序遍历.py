#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        tmp = [root]
        res = []
        add = True
        while tmp:
            while add and root.left:
                tmp.append(root.left)
                root = root.left
            root = tmp.pop()
            res.append(root.val)
            
            if root.right:
                tmp.append(root.right)
                root = root.right
                add = True
            else:
                add = False

                
                
        return res
# @lc code=end

