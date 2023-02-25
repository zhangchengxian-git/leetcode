#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional
import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
        return self.buildTree(1, n)

    def buildTree(self, begin, end):
        res = []
        if begin > end:
            return [None, ]
        
        for i in range(begin, end+1):
            left =  self.buildTree(begin, i-1)
            right =  self.buildTree(i+1, end)
            for l in left:
                for r in right:
                    res.append(TreeNode(i, l, r))
        return res


if __name__ == "__main__":
    So = Solution()
    a = So.generateTrees(3)
    print(str(a[2].left))

                
# @lc code=end

