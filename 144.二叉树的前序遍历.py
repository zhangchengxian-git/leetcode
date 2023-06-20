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
        中左右，每个结点操作一样：输出结点，保存右节点，
        便于接下来遍历，将当前结点变为左节点。直到当前
        结点没有子节点，数组中最后一个保存的是其兄弟右
        结点，将兄弟右结点当作当前结点，
        '''
        
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

