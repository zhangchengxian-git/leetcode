#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        '''
        根节点放入以后，将其子树放入，将最左依次放入，直到需要输出的第一个
        节点，之后将第一个节点拿出来，root设为tmp中最后一个，如果root和拿
        出的节点有父子关系，说明root子节点已经全部遍历过，下一个输出应该是
        root，否则考虑加入root子节点
        '''
        
        '''
        tmp = [root]
        while tmp:
            while root:
                if root.right:
                    tmp.append(root.right)
                if root.left:
                    tmp.append(root.left)
                if root == tmp[-1]:
                    break
                else:
                    root = tmp[-1]
            node = tmp.pop()
            res.append(node.val)
            if tmp:
                root = tmp[-1]
            while root.left == node or root.right == node:
                node = tmp.pop()
                res.append(node.val)
                if tmp:
                    root = tmp[-1]'''
        res = [root.val]
        if root.right:
            res = self.postorderTraversal(root.right) + res
        if root.left:
            res = self.postorderTraversal(root.left) + res
        return res

            

# @lc code=end

