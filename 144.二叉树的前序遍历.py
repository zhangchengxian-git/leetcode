#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]):
        '''
        res = []
        tmp = []
        while root:
            if root.right:
                tmp.append(root.right)
            res.append(root.val)
            if root.left:
                root = root.left
            elif tmp != []:
                root = tmp.pop()
            else:
                root = None
        return res
        '''
        res = []
        if not root:
            return res
        res.append(root.val)
        if root.left:
            res = res + self.preorderTraversal(root.left)
        if root.right:
            res = res + self.preorderTraversal(root.right)
        return res
    # @lc code=end

