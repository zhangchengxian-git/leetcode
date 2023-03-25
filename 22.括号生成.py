#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        tmp = ''
        self.generate(1, 0, res, tmp+'(', n)
        return res


    def generate(self, left: int, right: int, res: List[str], tmp: str, n: int):
        if left == right and left == n:
            res.append(tmp)
            return
        if left < n:
            self.generate(left+1, right, res, tmp+'(', n)
        if left > right:
            self.generate(left, right+1, res, tmp+')', n)

# @lc code=end

